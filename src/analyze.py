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
        elif mode == 'mso': return "l_mso"
        elif mode == 'belief': return "l_bel"
        elif mode == 'direct': return "l_dir"
        return f"l_{mode}"
    elif impl == 'christian':
        if mode == 'belief': return "c_bel"
        elif mode == 'direct': return "c_dir"
        elif mode == 'mso': return "c_mso"
        return f"c_{mode}"
    elif impl == 'spot':
        if mode == 'ltl': return "s_ltl"
        elif mode == 'ltlf': return "s_ltf"
        elif mode == 'ltlfilt': return "s_flt"
        return f"s_{mode}"
    return f"{impl[0]}_{mode}" if impl else f"?_{mode}"

def get_job_label(job_id):
    import json
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    label_file = os.path.join(os.path.dirname(scripts_dir), "data", "job_labels.json")
    if os.path.exists(label_file):
        try:
            with open(label_file, 'r') as f:
                labels = json.load(f)
                return labels.get(job_id, job_id)
        except: pass
    return job_id

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
                # Skip comment lines
                non_comments = (line for line in f if not line.strip().startswith('#'))
                reader = csv.DictReader(non_comments)
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

def run_analysis(grouped_results, job_id=None, output_inconsistent=None):
    """Calculates summary stats and checks for semantic consistency."""
    test_data = defaultdict(dict)
    summary = []
    
    label_text = get_job_label(job_id) if job_id else "All Background Data"

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
    print(f"\nAnalysis for: {label_text}")
    print("="*70)
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
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    default_results_dir = os.path.join(os.path.dirname(scripts_dir), "data", "results")
    parser.add_argument("--job-id", help="Job ID to analyze")
    parser.add_argument("--results-dir", default=default_results_dir)
    parser.add_argument("--output-inconsistent", help="Save conflict details to file")
    args = parser.parse_args()

    results = load_shards(args.results_dir, args.job_id)
    if results:
        run_analysis(results, job_id=args.job_id, output_inconsistent=args.output_inconsistent)
    else:
        print("No results found.")
