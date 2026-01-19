#!/usr/bin/env python3
"""
Log analyzer for SLURM job logs.
Analyzes logs to find:
- Common error patterns
- Timeout patterns
- Job completion status
- Performance statistics
"""

import argparse
import re
from pathlib import Path
from collections import defaultdict, Counter
import sys

def parse_log_file(log_path):
    """Parse a single log file and extract key information."""
    info = {
        'job_id': None,
        'task_id': None,
        'node': None,
        'tool': None,
        'shard': None,
        'total_tests': 0,
        'passed': 0,
        'failed': 0,
        'timeout': 0,
        'error': 0,
        'other': 0,
        'inconsistent': 0,
        'exit_status': None,
        'timeouts': [],
        'errors': [],
        'failures': []
    }
    
    try:
        with open(log_path, 'r') as f:
            content = f.read()
            
            # Extract header information
            if m := re.search(r'SLURM Job ID: (\d+)', content):
                info['job_id'] = m.group(1)
            if m := re.search(r'Array Task ID: (\d+)', content):
                info['task_id'] = m.group(1)
            if m := re.search(r'Running on node: (.+)', content):
                info['node'] = m.group(1).strip()
            if m := re.search(r'Testing: (.+)', content):
                info['tool'] = m.group(1).strip()
            if m := re.search(r'Shard: (\d+) of (\d+)', content):
                info['shard'] = f"{m.group(1)}/{m.group(2)}"
            if m := re.search(r'Running (\d+) out of (\d+) tests', content):
                info['total_tests'] = int(m.group(1))
            
            # Extract statistics
            if m := re.search(r'Passed: (\d+)', content):
                info['passed'] = int(m.group(1))
            if m := re.search(r'Failed: (\d+)', content):
                info['failed'] = int(m.group(1))
            if m := re.search(r'Timeout: (\d+)', content):
                info['timeout'] = int(m.group(1))
            if m := re.search(r'Error: (\d+)', content):
                info['error'] = int(m.group(1))
            if m := re.search(r'Other: (\d+)', content):
                info['other'] = int(m.group(1))
            if m := re.search(r'Inconsistent: (\d+)', content):
                info['inconsistent'] = int(m.group(1))
            
            # Check exit status
            if '✓ Test completed successfully' in content:
                info['exit_status'] = 'success'
            elif '✗ Test failed' in content:
                info['exit_status'] = 'failed'
            
            # Extract timeout/error/failure messages
            for line in content.split('\n'):
                if line.startswith('Timeout for '):
                    test = line.replace('Timeout for ', '').strip()
                    info['timeouts'].append(test)
                elif line.startswith('Failed to run '):
                    test = re.search(r'Failed to run (.+?):', line)
                    if test:
                        info['failures'].append(test.group(1))
                elif ('Error:' in line or 'error' in line.lower()) and 'Error: 0' not in line and 'Statistics:' not in line:
                    info['errors'].append(line.strip())
    
    except Exception as e:
        print(f"Warning: Error parsing {log_path}: {e}")
    
    return info

def analyze_job_logs(job_id, tool=None):
    """Analyze all logs for a given job."""
    logs_dir = Path(__file__).parent.parent / "data" / "logs" / str(job_id)
    
    if not logs_dir.exists():
        print(f"Error: Logs directory not found: {logs_dir}")
        return None
    
    log_files = sorted(logs_dir.glob("*.out"))
    
    if not log_files:
        print(f"Error: No log files found in {logs_dir}")
        return None
    
    all_logs = []
    tool_stats = defaultdict(lambda: {
        'total_shards': 0,
        'total_tests': 0,
        'passed': 0,
        'failed': 0,
        'timeout': 0,
        'error': 0,
        'other': 0,
        'success_count': 0,
        'failed_count': 0,
        'common_timeouts': Counter(),
        'common_errors': Counter()
    })
    
    for log_file in log_files:
        info = parse_log_file(log_file)
        all_logs.append(info)
        
        # Skip if tool filter is specified and doesn't match
        if tool and info['tool'] != tool:
            continue
        
        t = info['tool'] or 'unknown'
        stats = tool_stats[t]
        
        stats['total_shards'] += 1
        stats['total_tests'] += info['total_tests']
        stats['passed'] += info['passed']
        stats['failed'] += info['failed']
        stats['timeout'] += info['timeout']
        stats['error'] += info['error']
        stats['other'] += info['other']
        
        if info['exit_status'] == 'success':
            stats['success_count'] += 1
        elif info['exit_status'] == 'failed':
            stats['failed_count'] += 1
        
        # Track common timeouts and errors
        for timeout in info['timeouts']:
            stats['common_timeouts'][timeout] += 1
        for error in info['errors']:
            stats['common_errors'][error] += 1
    
    return tool_stats, all_logs

def print_analysis(tool_stats, job_id):
    """Print analysis results."""
    print(f"\n{'='*70}")
    print(f"Log Analysis for Job {job_id}")
    print(f"{'='*70}\n")
    
    for tool, stats in sorted(tool_stats.items()):
        print(f"Tool: {tool}")
        print(f"{'─'*70}")
        print(f"  Shards completed: {stats['success_count']}/{stats['total_shards']}")
        if stats['failed_count'] > 0:
            print(f"  ⚠️  Shards failed: {stats['failed_count']}")
        
        print(f"\n  Test Results:")
        print(f"    Total tests:  {stats['total_tests']}")
        print(f"    Passed:       {stats['passed']:4d} ({stats['passed']/stats['total_tests']*100:5.1f}%)")
        print(f"    Failed:       {stats['failed']:4d} ({stats['failed']/stats['total_tests']*100:5.1f}%)")
        print(f"    Timeout:      {stats['timeout']:4d} ({stats['timeout']/stats['total_tests']*100:5.1f}%)")
        print(f"    Error:        {stats['error']:4d} ({stats['error']/stats['total_tests']*100:5.1f}%)")
        print(f"    Other:        {stats['other']:4d} ({stats['other']/stats['total_tests']*100:5.1f}%)")
        
        # Show most common timeouts
        if stats['common_timeouts']:
            print(f"\n  Most common timeouts (top 5):")
            for test, count in stats['common_timeouts'].most_common(5):
                test_name = Path(test).name
                print(f"    {count:3d}x {test_name}")
        
        # Show common errors
        if stats['common_errors']:
            print(f"\n  Common errors:")
            for error, count in stats['common_errors'].most_common(3):
                if len(error) > 60:
                    error = error[:57] + "..."
                print(f"    {count:3d}x {error}")
        
        print(f"\n{'='*70}\n")

def main():
    parser = argparse.ArgumentParser(description='Analyze SLURM job logs')
    parser.add_argument('--job-id', type=str, required=True, help='Job ID to analyze')
    parser.add_argument('--tool', type=str, help='Filter by specific tool (e.g., lucas_mso)')
    parser.add_argument('--show-failures', action='store_true', help='Show detailed failure information')
    
    args = parser.parse_args()
    
    result = analyze_job_logs(args.job_id, args.tool)
    
    if result is None:
        sys.exit(1)
    
    tool_stats, all_logs = result
    
    if not tool_stats:
        print(f"No logs found for job {args.job_id}")
        if args.tool:
            print(f"(filtered by tool: {args.tool})")
        sys.exit(1)
    
    print_analysis(tool_stats, args.job_id)
    
    # Show failures if requested
    if args.show_failures:
        print("\nFailed Shards:")
        print("="*70)
        for log in all_logs:
            if log['exit_status'] == 'failed':
                print(f"  Task {log['task_id']}: {log['tool']} on {log['node']}")
                if log['errors']:
                    for error in log['errors'][:3]:
                        print(f"    - {error}")

if __name__ == '__main__':
    main()
