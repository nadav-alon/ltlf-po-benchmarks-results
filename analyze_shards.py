import csv
import os
import glob
import argparse
from collections import defaultdict

def analyze_shards(results_dir, job_id=None):
    if job_id:
        path_pattern = os.path.join(results_dir, job_id, "**", "shard_*.csv")
    else:
        path_pattern = os.path.join(results_dir, "**", "shard_*.csv")
    
    shard_files = glob.glob(path_pattern, recursive=True)
    
    # Group shards by their implementation and mode
    grouped_results = defaultdict(list)
    for filepath in shard_files:
        parts = os.path.dirname(filepath).split("/")[-1].split("_")
        if len(parts) < 2:
            continue
        group_key = "_".join(parts)
        
        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        grouped_results[group_key].append({
                            'test': os.path.basename(row['test']),
                            'time': float(row['time']),
                            'status': int(row['status'])
                        })
                    except (ValueError, KeyError, TypeError):
                        continue
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    return grouped_results

def print_analysis(grouped_results, inconsistent_output=None):
    test_data = defaultdict(dict)
    summary = []

    # Sort groups for consistent display
    sorted_groups = sorted(grouped_results.keys())

    for group_key in sorted_groups:
        data = grouped_results[group_key]
        
        # Create a short label like c_bel, l_dir
        parts = group_key.split('_')
        impl = parts[0]
        mode = "_".join(parts[1:]) # Handle modes with underscores if any, though we have hyphens
        
        # Create a short label
        if impl == 'lucas':
            if mode == 'belief-states': lbl = f"{impl[0]}_bst"
            elif mode == 'projection-based': lbl = f"{impl[0]}_prj"
            else: lbl = f"{impl[0]}_{mode}"
        elif impl == 'christian':
            # Christian's naming
            if mode == 'belief': lbl = f"{impl[0]}_bel"
            elif mode == 'direct': lbl = f"{impl[0]}_dir"
            else: lbl = f"{impl[0]}_{mode}"
        elif impl == 'spot':
            lbl = f"{impl[0]}_{mode}"
        else:
            raise ValueError(f"Unknown implementation: {impl}")
        
        actually_succ = [r for r in data if r['status'] in [0, 1]]
        avg_time = sum(r['time'] for r in actually_succ) / len(actually_succ) if actually_succ else 0
        
        summary.append({
            'label': lbl,
            'group': group_key,
            'total': len(data),
            'success': len(actually_succ),
            'timeouts': len([r for r in data if r['status'] == -2]),
            'errors': len([r for r in data if r['status'] == -1]),
            'avg_time': avg_time
        })
        
        for r in data:
            test_data[r['test']][lbl] = (r['status'], r['time'])

    print("Performance Summary:")
    print(f"{'Method':<8} {'Total':<6} {'Succ':<6} {'TO':<6} {'Err':<6} {'Avg Time (ms)':<15}")
    print("-" * 55)
    for s in summary:
        print(f"{s['label']:<8} {s['total']:<6} {s['success']:<6} {s['timeouts']:<6} {s['errors']:<6} {s['avg_time']:<15.2f}")

    print("\nRealizability Consistency Check (Successes Only):")
    headers = [s['label'] for s in summary]
    header_str = " ".join(f"{h:<6}" for h in headers)
    print(f"{'Test':<30} {header_str} | Consensus")
    print("-" * (40 + len(headers) * 7))

    inconsistent_tests = []
    insufficient_tests = []
    
    for test, results in sorted(test_data.items()):
        outcomes = [res[0] for res in results.values() if res[0] in [0, 1]]
        if not outcomes:
            consensus = "N/A"
        elif len(set(outcomes)) > 1:
            inconsistent_tests.append(test)
            consensus = "!!! CONFLICT !!!"
        elif len(outcomes) < 2:
            insufficient_tests.append(test)
            consensus = "SINGLE RUN"
        else:
            consensus_val = outcomes[0]
            consensus = "REALIZABLE" if consensus_val == 1 else "UNREALIZABLE"

        # (Existing loop logic continues...)

    # Actually, let's just print the summary and any inconsistencies first.
    # If the user wants the full table, they can ask.
    
    if inconsistent_tests:
        print(f"\nWARNING: {len(inconsistent_tests)} Inconsistencies found! (Showing first 20)")
        for t in inconsistent_tests[:20]:
            print(f"  - {t}")
            for s in summary:
                res = test_data[t].get(s['label'])
                if res and res[0] in [0, 1]:
                     print(f"    {s['label']}: {'R' if res[0] == 1 else 'U'}")
        
        if inconsistent_output:
            try:
                with open(inconsistent_output, 'w') as f:
                    f.write(f"Inconsistent Tests ({len(inconsistent_tests)} total):\n")
                    f.write("=" * 30 + "\n")
                    for t in inconsistent_tests:
                        f.write(f"\nTest: {t}\n")
                        for s in summary:
                            res = test_data[t].get(s['label'])
                            if res and res[0] in [0, 1]:
                                f.write(f"  {s['label']}: {'REALIZABLE' if res[0] == 1 else 'UNREALIZABLE'}\n")
                            elif res:
                                status_map = {-1: 'ERROR', -2: 'TIMEOUT'}
                                f.write(f"  {s['label']}: {status_map.get(res[0], res[0])}\n")
                            else:
                                f.write(f"  {s['label']}: -\n")
                    
                    if insufficient_tests:
                        f.write(f"\n\nInsufficient Data ({len(insufficient_tests)} tests with single success):\n")
                        f.write("=" * 30 + "\n")
                        for t in insufficient_tests:
                             f.write(f"  - {t}\n")

                print(f"\nFull report of inconsistencies and single runs written to: {inconsistent_output}")
            except Exception as e:
                print(f"Error writing to {inconsistent_output}: {e}")
    else:
        if insufficient_tests:
            print(f"\nNOTICE: {len(insufficient_tests)} tests have only one successful run (cannot cross-verify).")
        print("\nAll successful runs agreed on realizability.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze benchmark shards.")
    parser.add_argument("--job-id", help="Specific job ID folder to analyze (results/<job_id>)")
    parser.add_argument("--results-dir", default="/home/cowclaw/results_shards/results", help="Directory containing results")
    parser.add_argument("--output-inconsistent", help="File to write the full list of inconsistencies to")
    args = parser.parse_args()

    results = analyze_shards(args.results_dir, job_id=args.job_id)
    if not results:
        if args.job_id:
            print(f"No results found for job {args.job_id} in {args.results_dir}/{args.job_id}")
        else:
            print(f"No results found in {args.results_dir}")
    else:
        print_analysis(results, inconsistent_output=args.output_inconsistent)
