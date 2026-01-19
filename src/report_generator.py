#!/usr/bin/env python3
import subprocess
import os
import sys
import argparse
import json
import re
from pathlib import Path

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def get_semantics(job_id):
    """Detect semantics (mealy/moore) from job logs. Defaults to moore."""
    logs_dir = Path(__file__).parent.parent / "data" / "logs" / str(job_id)
    if not logs_dir.exists():
        return "moore"
    
    # Try the first few logs to find the semantics line
    for log_file in sorted(logs_dir.glob("*.out"))[:5]:
        with open(log_file, 'r') as f:
            content = f.read()
            m = re.search(r'Semantics:\s*(\w+)', content)
            if m:
                return m.group(1).lower()
    
    return "moore"

def generate_report_for_job(job_id, scripts_dir, config=None):
    report = []
    report.append(f"# Analysis Report for Job {job_id}")
    
    semantics = get_semantics(job_id)
    report.append(f"Detected Semantics: **{semantics}**")
    
    truth_tool = "lucas_mso"
    truth_job_id = None
    
    if config and semantics in config:
        truth_tool = config[semantics].get("source_of_truth", truth_tool)
        truth_job_id = config[semantics].get("job_id")
        
    if truth_job_id and truth_job_id != job_id:
        report.append(f"Comparing against Source of Truth from **Job {truth_job_id}** ({semantics})")
    
    report.append("")

    # 1. Run analyze.py
    analyze_script = scripts_dir / "analyze.py"
    inconsistent_file = f"inconsistent_{job_id}.txt"
    res = run_command([sys.executable, str(analyze_script), "--job-id", job_id, "--output-inconsistent", inconsistent_file])
    report.append("## Summary Statistics")
    report.append("```")
    report.append(res.stdout)
    report.append("```")
    
    if os.path.exists(inconsistent_file):
        report.append("### 🚨 Semantic Inconsistencies")
        with open(inconsistent_file, 'r') as f:
            report.append("```")
            report.append(f.read())
            report.append("```")
        os.remove(inconsistent_file)

    # 2. Run sanity_check.py
    sanity_script = scripts_dir / "sanity_check.py"
    res = run_command([sys.executable, str(sanity_script), "--job-id", job_id, "--all-tools"])
    report.append("## Sanity Check Results")
    report.append("```")
    report.append(res.stdout)
    report.append("```")

    # 3. Run analyze_logs.py
    logs_script = scripts_dir / "analyze_logs.py"
    res = run_command([sys.executable, str(logs_script), "--job-id", job_id])
    if res.returncode == 0:
        report.append("## Log Analysis")
        report.append("```")
        report.append(res.stdout)
        report.append("```")

    # 4. Run report_errors.py
    errors_script = scripts_dir / "report_errors.py"
    res = run_command([sys.executable, str(errors_script), "--job-id", job_id, "--list"])
    report.append("## Error and Timeout Details")
    report.append("```")
    report.append(res.stdout)
    report.append("```")

    # 5. Cross-check against Source of Truth
    actual_truth_job = str(truth_job_id) if truth_job_id else job_id
    results_base = Path(__file__).parent.parent / "data" / "results"
    truth_path = results_base / actual_truth_job / truth_tool
    
    if truth_path.exists():
        report.append(f"## Cross-check against Source of Truth: {truth_tool} (Job {actual_truth_job})")
        
        # Tools in the CURRENT job to check
        current_job_results = results_base / job_id
        if current_job_results.exists():
            tools = [d.name for d in current_job_results.iterdir() if d.is_dir()]
            
            cross_check_script = scripts_dir / "cross_check.py"
            
            found_cross_issues = False
            for tool in sorted(tools):
                # Don't compare a tool with itself if it's the exact same job and tool
                if actual_truth_job == job_id and tool == truth_tool:
                    continue
                    
                res = run_command([
                    sys.executable, str(cross_check_script),
                    "--job-a", actual_truth_job, "--tool-a", truth_tool,
                    "--job-b", job_id, "--tool-b", tool
                ])
                if "CONFLICTS!" in res.stdout:
                    found_cross_issues = True
                    report.append(f"### Conflict with {tool}")
                    report.append("```")
                    report.append(res.stdout)
                    report.append("```")
            
            if not found_cross_issues:
                report.append(f"✅ All tools match reference {truth_tool} results.")
    else:
        report.append(f"## Cross-check Result")
        report.append(f"⚠️ Source of truth `{truth_tool}` for job `{actual_truth_job}` not found in results directory.")

    # 6. Visualizations
    visualize_script = scripts_dir / "visualize.py"
    run_command([sys.executable, str(visualize_script), "--job-id", job_id])
    
    figures_dir = Path(__file__).parent.parent / "reports" / "figures" / job_id
    if figures_dir.exists():
        report.append("## Visualizations")
        for img in sorted(figures_dir.glob("*.png")):
            # Use relative path for markdown if possible, but artifact upload will handle files
            # For GitHub comments, we usually need hosted images, but for artifacts we can just list them
            report.append(f"### {img.stem}")
            report.append(f"![{img.name}](reports/figures/{job_id}/{img.name})")

    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Generate consolidated reports for jobs")
    parser.add_argument("--job-ids", nargs="+", required=True, help="Job IDs to analyze")
    parser.add_argument("--truth", default="lucas_mso", help="Source of truth tool name")
    parser.add_argument("--output", help="Path to save the markdown report")
    
    args = parser.parse_args()
    scripts_dir = Path(__file__).parent.resolve()
    base_dir = scripts_dir.parent
    
    config = {}
    config_path = base_dir / "data" / "ci_config.json"
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
        except Exception as e:
            print(f"Warning: Could not read config from {config_path}: {e}")

    full_report = []
    for job_id in args.job_ids:
        full_report.append(generate_report_for_job(job_id, scripts_dir, config))
        full_report.append("\n---\n")
    
    final_text = "\n".join(full_report)
    print(final_text)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(final_text)

if __name__ == "__main__":
    main()
