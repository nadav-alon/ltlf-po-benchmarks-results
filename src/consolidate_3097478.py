import csv
import os
import re
from collections import defaultdict

JOB_ID = "3097478"
BASE_DIR = "/home/cowclaw/results_shards"
RESULTS_DIR = os.path.join(BASE_DIR, "results", JOB_ID)
LOGS_DIR = os.path.join(BASE_DIR, "logs", JOB_ID)
OUTPUT_DIR = os.path.join(BASE_DIR, f"analysis_{JOB_ID}")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_error_message(test_path, log_content):
    # Escape test_path for regex if needed, but simple search might be enough
    # Look for "Failed to run <test_path>: <message>"
    # Or "Error for <test_path>: <message>"
    
    # Try to find the line starting with "Failed to run " + test_path
    lines = log_content.splitlines()
    for i, line in enumerate(lines):
        if test_path in line and ("Failed to run" in line or "Error for" in line):
            return line.strip()
    return "Unknown error (message not found in log)"

def main():
    consolidated_results = []
    error_results = []
    
    # Mapping from (tool, shard) to log file path
    tool_shard_to_log = {}
    
    print("Mapping logs to shards...")
    if os.path.exists(LOGS_DIR):
        for log_file in os.listdir(LOGS_DIR):
            if not log_file.endswith(".out"): continue
            log_path = os.path.join(LOGS_DIR, log_file)
            try:
                with open(log_path, 'r', errors='ignore') as f:
                    content = f.read(2000) # Read enough to see header
                    tool_match = re.search(r"Testing: (.*)", content)
                    shard_match = re.search(r"Shard: (\d+)", content)
                    if tool_match and shard_match:
                        tool = tool_match.group(1).strip().replace(":", "_")
                        shard = shard_match.group(1).strip()
                        tool_shard_to_log[(tool, shard)] = log_path
            except Exception as e:
                print(f"Error reading log {log_file}: {e}")

    print("Consolidating CSV results...")
    tools = [d for d in os.listdir(RESULTS_DIR) if os.path.isdir(os.path.join(RESULTS_DIR, d))]
    
    for tool in tools:
        tool_dir = os.path.join(RESULTS_DIR, tool)
        shards = [f for f in os.listdir(tool_dir) if f.startswith("shard_") and f.endswith(".csv")]
        
        for shard_file in shards:
            shard_num = shard_file.replace("shard_", "").replace(".csv", "")
            filepath = os.path.join(tool_dir, shard_file)
            
            log_path = tool_shard_to_log.get((tool, shard_num))
            log_content = None
            if log_path and os.path.exists(log_path):
                with open(log_path, 'r', errors='ignore') as f:
                    log_content = f.read()
            
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    test = row['test']
                    time = row['time']
                    status = int(row['status'])
                    
                    res_row = {
                        'tool': tool,
                        'test': test,
                        'time': time,
                        'status': status
                    }
                    consolidated_results.append(res_row)
                    
                    if status == -1:
                        err_msg = "N/A"
                        if log_content:
                            err_msg = get_error_message(test, log_content)
                        
                        error_results.append({
                            'tool': tool,
                            'test': test,
                            'time': time,
                            'status': status,
                            'error_message': err_msg
                        })
                    elif status == -2:
                        # Timeout is also a kind of error, but usually "expected"
                        error_results.append({
                            'tool': tool,
                            'test': test,
                            'time': time,
                            'status': status,
                            'error_message': 'Timeout'
                        })

    # Write consolidated CSV
    consolidated_file = os.path.join(OUTPUT_DIR, "consolidated_results.csv")
    with open(consolidated_file, 'w', newline='') as f:
        fieldnames = ['tool', 'test', 'time', 'status']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(consolidated_results)
    
    # Write error CSV
    error_file = os.path.join(OUTPUT_DIR, "errors.csv")
    with open(error_file, 'w', newline='') as f:
        fieldnames = ['tool', 'test', 'time', 'status', 'error_message']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(error_results)
    
    # Generate Report
    report_file = os.path.join(OUTPUT_DIR, "report.md")
    with open(report_file, 'w') as f:
        f.write(f"# Analysis Report for Job {JOB_ID}\n\n")
        
        # Summary statistics
        f.write("## Summary Statistics\n\n")
        tool_stats = defaultdict(lambda: {'total': 0, 'success': 0, 'unrealizable': 0, 'error': 0, 'timeout': 0})
        for r in consolidated_results:
            tool = r['tool']
            tool_stats[tool]['total'] += 1
            if r['status'] == 1: tool_stats[tool]['success'] += 1
            elif r['status'] == 0: tool_stats[tool]['unrealizable'] += 1
            elif r['status'] == -1: tool_stats[tool]['error'] += 1
            elif r['status'] == -2: tool_stats[tool]['timeout'] += 1
            
        f.write("| Tool | Total | Success (1) | Unrealizable (0) | Error (-1) | Timeout (-2) |\n")
        f.write("| --- | --- | --- | --- | --- | --- |\n")
        for tool, stats in sorted(tool_stats.items()):
            f.write(f"| {tool} | {stats['total']} | {stats['success']} | {stats['unrealizable']} | {stats['error']} | {stats['timeout']} |\n")
        
        f.write("\n## Error Analysis\n\n")
        
        # Categorize errors
        # Expected errors: Timeout
        # Unexpected errors: status -1
        
        f.write("### Unexpected Errors (Status -1)\n\n")
        unexpected_errors = [e for e in error_results if e['status'] == -1]
        if not unexpected_errors:
            f.write("No unexpected errors found.\n")
        else:
            # Group by error message
            msg_to_tests = defaultdict(list)
            for e in unexpected_errors:
                msg_to_tests[e['error_message']].append(e)
            
            for msg, tests in sorted(msg_to_tests.items()):
                f.write(f"#### {msg}\n")
                f.write(f"Count: {len(tests)}\n\n")
                f.write("| Tool | Test |\n")
                f.write("| --- | --- |\n")
                # Show only first 10 for each to keep report concise? 
                # Or all if not too many. Let's do all for now but capped.
                for t in tests[:20]:
                    f.write(f"| {t['tool']} | {t['test']} |\n")
                if len(tests) > 20:
                    f.write(f"| ... | and {len(tests)-20} more |\n")
                f.write("\n")

        f.write("### Expected Errors (Timeouts - Status -2)\n\n")
        timeout_counts = defaultdict(int)
        for e in error_results:
            if e['status'] == -2:
                timeout_counts[e['tool']] += 1
        
        if not timeout_counts:
            f.write("No timeouts found.\n")
        else:
            f.write("| Tool | Timeout Count |\n")
            f.write("| --- | --- |\n")
            for tool, count in sorted(timeout_counts.items()):
                f.write(f"| {tool} | {count} |\n")

    print(f"Consolidation complete. Results in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
