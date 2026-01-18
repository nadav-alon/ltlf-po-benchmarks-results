#!/usr/bin/env python3
import csv
import os
import glob
import argparse
from collections import defaultdict

def get_label(impl, mode):
    """Mapping for short, readable tool labels."""
    if impl == 'lucas':
        if mode == 'belief-states': return "l_bst"
        elif mode == 'projection-based': return "l_prj"
        elif mode in ['belief', 'direct']: return f"l_{mode[0]}*" # Handle legacy
        return f"l_{mode[:3]}"
    elif impl == 'christian':
        if mode == 'belief': return "c_bel"
        elif mode == 'direct': return "c_dir"
        return f"c_{mode[:3]}"
    elif impl == 'spot':
        return f"s_{mode[:3]}"
    return f"{impl[0]}_{mode[:3]}"

def load_shards(results_dir, job_id=None):
    """Loads all CSV shards and groups them by tool (impl_mode)."""
    if job_id:
        path_pattern = os.path.join(results_dir, job_id, "**", "shard_*.csv")
    else:
        path_pattern = os.path.join(results_dir, "**", "shard_*.csv")
    
    shard_files = glob.glob(path_pattern, recursive=True)
    grouped_results = defaultdict(list)
    
    for filepath in shard_files:
        # Extract tool name from directory: results/<job_id>/<impl>_<mode>/shard_N.csv
        dir_name = os.path.basename(os.path.dirname(filepath))
        parts = dir_name.split('_', 1)
        if len(parts) == 2:
            tool_key = dir_name # impl_mode
        else:
            tool_key = f"unknown_{dir_name}"
        
        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        grouped_results[tool_key].append({
                            'test': row['test'],
                            'time': float(row['time']),
                            'status': int(float(row['status']))
                        })
                    except (ValueError, KeyError, TypeError): continue
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            
    return grouped_results

def run_analysis(grouped_results, output_inconsistent=None):
    """Calculates summary stats and checks for semantic consistency."""
    test_data = defaultdict(dict)
    summary = []

    for tool_key, data in sorted(grouped_results.items()):
        impl, mode = (tool_key.split('_', 1) + [""])[:2]
        lbl = get_label(impl, mode)
        
        actually_succ = [r for r in data if r['status'] in [0, 1]]
        avg_time = sum(r['time'] for r in actually_succ) / len(actually_succ) if actually_succ else 0
        
        summary.append({
            'label': lbl,
            'key': tool_key,
            'total': len(data),
            'success': len(actually_succ),
            'timeouts': len([r for r in data if r['status'] == -2]),
            'errors': len([r for r in data if r['status'] == -1]),
            'avg_time': avg_time
        })
        
        for r in data:
            test_data[r['test']][lbl] = (r['status'], r['time'])

    # 1. Print Performance Table
    print("\n" + "="*70)
    print(f"{'Tool':<10} {'Total':<8} {'Succ':<8} {'TO':<8} {'Err':<8} {'Avg Time (ms)':<15}")
    print("-" * 70)
    for s in summary:
        print(f"{s['label']:<10} {s['total']:<8} {s['success']:<8} {s['timeouts']:<8} {s['errors']:<8} {s['avg_time']:<15.2f}")
    print("="*70)

    # 2. Consistency Check
    inconsistent_tests = []
    for test, results in sorted(test_data.items()):
        outcomes = [res[0] for res in results.values() if res[0] in [0, 1]]
        if len(set(outcomes)) > 1:
            inconsistent_tests.append(test)

    if inconsistent_tests:
        print(f"\n[!] WARNING: {len(inconsistent_tests)} semantic inconsistencies found!")
        if output_inconsistent:
            with open(output_inconsistent, 'w') as f:
                for t in inconsistent_tests:
                    f.write(f"\nTest: {t}\n")
                    for s in summary:
                        res = test_data[t].get(s['label'])
                        status = {1: 'REALIZABLE', 0: 'UNREALIZABLE', -1: 'ERROR', -2: 'TIMEOUT'}.get(res[0] if res else None, '-')
                        f.write(f"  {s['label']:<10}: {status}\n")
            print(f"Details written to: {output_inconsistent}")
        else:
            print("Run with --output-inconsistent <file> for details.")
    else:
        print("\n[+] All tools agreed on results (0/1).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolidated Analysis Tool")
    parser.add_argument("--job-id", help="Job ID to analyze")
    parser.add_argument("--results-dir", default="/home/cowclaw/results_shards/data/results")
    parser.add_argument("--output-inconsistent", help="Save conflict details to file")
    args = parser.parse_args()

    results = load_shards(args.results_dir, args.job_id)
    if results:
        run_analysis(results, args.output_inconsistent)
    else:
        print("No results found.")
