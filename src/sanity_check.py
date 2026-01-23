#!/usr/bin/env python3
"""
Sanity check for benchmark results to detect obvious mistakes.
Checks for:
- All tests being realizable (status=1)
- All tests being unrealizable (status=0)
- All tests having errors/timeouts
- Unusually high error rates
"""

import argparse
import csv
from pathlib import Path
from collections import defaultdict
import sys

def load_results(job_id, tool):
    """Load all results for a given job and tool."""
    results_dir = Path(__file__).parent.parent / "data" / "results" / str(job_id) / tool
    
    if not results_dir.exists():
        print(f"Error: Results directory not found: {results_dir}")
        return None
    
    all_results = []
    shard_files = sorted(results_dir.glob("shard_*.csv"))
    
    if not shard_files:
        print(f"Error: No shard files found in {results_dir}")
        return None
    
    for shard_file in shard_files:
        try:
            with open(shard_file, 'r') as f:
                # Skip comment lines
                non_comments = (line for line in f if not line.strip().startswith('#'))
                reader = csv.DictReader(non_comments)
                for row in reader:
                    all_results.append({
                        'test': row['test'],
                        'status': int(float(row['status'])),
                        'time': float(row['time'])
                    })
        except Exception as e:
            print(f"Warning: Error reading {shard_file}: {e}")
    
    return all_results

def analyze_results(results, job_id, tool):
    """Analyze results for obvious mistakes."""
    if not results:
        return
    
    total = len(results)
    status_counts = defaultdict(int)
    
    for r in results:
        status_counts[r['status']] += 1
    
    realizable = status_counts.get(1, 0)
    unrealizable = status_counts.get(0, 0)
    timeout = status_counts.get(-2, 0)
    error = status_counts.get(-1, 0)
    na_count = status_counts.get(-3, 0)
    
    print(f"\n{'='*60}")
    print(f"Job {job_id} - Tool: {tool}")
    print(f"{'='*60}")
    print(f"Total tests: {total}")
    print(f"  Realizable (1):   {realizable:4d} ({realizable/total*100:5.1f}%)")
    print(f"  Unrealizable (0): {unrealizable:4d} ({unrealizable/total*100:5.1f}%)")
    print(f"  Timeout (-2):     {timeout:4d} ({timeout/total*100:5.1f}%)")
    print(f"  Error (-1):       {error:4d} ({error/total*100:5.1f}%)")
    print(f"  N/A (-3):         {na_count:4d} ({na_count/total*100:5.1f}%)")
    
    # Check for obvious mistakes
    issues = []
    
    if realizable == total:
        issues.append("⚠️  ALL tests are REALIZABLE - likely a bug!")
    
    if unrealizable == total:
        issues.append("⚠️  ALL tests are UNREALIZABLE - likely a bug!")
    
    if timeout == total:
        issues.append("⚠️  ALL tests TIMED OUT - check timeout settings!")
    
    if error == total:
        issues.append("⚠️  ALL tests had ERRORS - check tool configuration!")
    
    if realizable + unrealizable == 0:
        issues.append("⚠️  NO successful results - all tests failed!")
    
    if error / total > 0.5:
        issues.append(f"⚠️  High error rate ({error/total*100:.1f}%) - investigate!")
    
    if timeout / total > 0.5:
        issues.append(f"⚠️  High timeout rate ({timeout/total*100:.1f}%) - consider increasing timeout!")
    
    # Check for suspicious patterns in SUCCESSFUL results only (status 0 or 1)
    successful = realizable + unrealizable
    
    if successful > 0:
        # Check if ALL successful tests have the same result
        if realizable > 0 and unrealizable == 0:
            issues.append(f"⚠️  All {realizable} successful tests are REALIZABLE (0 unrealizable) - suspicious!")
        
        if unrealizable > 0 and realizable == 0:
            issues.append(f"⚠️  All {unrealizable} successful tests are UNREALIZABLE (0 realizable) - suspicious!")
        
        # Check for highly skewed results (>95% one way)
        if successful > 10:  # Only check if we have enough successful results
            if realizable / successful > 0.95:
                issues.append(f"⚠️  {realizable/successful*100:.1f}% of successful tests are realizable - highly skewed!")
            elif unrealizable / successful > 0.95:
                issues.append(f"⚠️  {unrealizable/successful*100:.1f}% of successful tests are unrealizable - highly skewed!")
    
    if issues:
        print(f"\n🚨 ISSUES DETECTED:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print(f"\n✅ No obvious issues detected")
    
    print(f"{'='*60}\n")
    
    return len(issues) > 0

def main():
    parser = argparse.ArgumentParser(description='Sanity check for benchmark results')
    parser.add_argument('--job-id', type=str, required=True, help='Job ID to check')
    parser.add_argument('--tool', type=str, help='Specific tool to check (e.g., lucas_mso)')
    parser.add_argument('--all-tools', action='store_true', help='Check all tools in the job')
    
    args = parser.parse_args()
    
    if not args.tool and not args.all_tools:
        print("Error: Must specify either --tool or --all-tools")
        sys.exit(1)
    
    results_base = Path(__file__).parent.parent / "data" / "results" / args.job_id
    
    if not results_base.exists():
        print(f"Error: Job {args.job_id} not found in results directory")
        sys.exit(1)
    
    tools_to_check = []
    
    if args.all_tools:
        # Find all tool directories
        tools_to_check = [d.name for d in results_base.iterdir() if d.is_dir()]
        if not tools_to_check:
            print(f"Error: No tool directories found in {results_base}")
            sys.exit(1)
    else:
        tools_to_check = [args.tool]
    
    any_issues = False
    
    for tool in sorted(tools_to_check):
        results = load_results(args.job_id, tool)
        if results:
            has_issues = analyze_results(results, args.job_id, tool)
            any_issues = any_issues or has_issues
    
    if any_issues:
        print("\n⚠️  Some tools have issues - review the output above")
        sys.exit(1)
    else:
        print("\n✅ All checked tools look reasonable")
        sys.exit(0)

if __name__ == '__main__':
    main()
