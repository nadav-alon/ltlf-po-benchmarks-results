import csv
import os
import argparse
from collections import defaultdict

def analyze_file(filepath):
    results = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    results.append({
                        'test': os.path.basename(row['test']),
                        'time': float(row['time']),
                        'status': int(row['status'])
                    })
                except (ValueError, KeyError, TypeError):
                    continue
    except FileNotFoundError:
        return None
    return results

files = [
    'results_christian_belief.csv',
    'results_christian_direct.csv',
    'results_christian_mso.csv',
    'results_lucas_belief-states.csv',
    'results_lucas_projection-based.csv',
    'results_lucas_mso.csv',
    # Legacy names
    'test_christian_belief.csv',
    'test_christian_direct.csv',
    'test_christian_mso.csv',
    'test_lucas_belief.csv',
    'test_lucas_direct.csv',
    'test_lucas_mso.csv'
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze consolidated benchmark results.")
    parser.add_argument("--job-id", help="Specific job ID folder to analyze (results/<job_id>)")
    parser.add_argument("--base-dir", default="/home/cowclaw/results_shards", help="Base directory")
    args = parser.parse_args()

    results_path = args.base_dir
    if args.job_id:
        results_path = os.path.join(args.base_dir, "results", args.job_id)

    test_data = defaultdict(dict)
    summary = []

    for f in files:
        path = os.path.join(results_path, f)
        data = analyze_file(path)
        if data is None: continue
    
    parts = f.replace('results_', '').replace('test_', '').replace('.csv', '').split('_')
    impl = parts[0]
    mode = "_".join(parts[1:])
    
    # Create a descriptive label
    if impl == 'lucas':
        if mode == 'belief-states': lbl = f"{impl[0]}_bst"
        elif mode == 'projection-based': lbl = f"{impl[0]}_prj"
        elif mode == 'belief': lbl = f"{impl[0]}_prj" # legacy mapping fix
        elif mode == 'direct': lbl = f"{impl[0]}_bst" # legacy mapping fix
        else: lbl = f"{impl[0]}_{mode[:3]}"
    else:
        # Christian's naming
        if mode == 'belief': lbl = f"{impl[0]}_bel"
        elif mode == 'direct': lbl = f"{impl[0]}_dir"
        else: lbl = f"{impl[0]}_{mode[:3]}"
    
    succ = [r for r in data if r['status'] == 1 or r['status'] == 0]
    actually_succ = [r for r in data if r['status'] in [0, 1]]
    
    avg_time = sum(r['time'] for r in actually_succ) / len(actually_succ) if actually_succ else 0
    
    summary.append({
        'label': lbl,
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

print("\nRealizability Consistency Check:")
print(f"{'Test':<20}", end="")
for s in summary:
    print(f" {s['label']:<6}", end="")
print(" | Consensus")
print("-" * (25 + len(summary) * 7))

inconsistent_tests = []
for test, results in sorted(test_data.items()):
    outcomes = [res[0] for res in results.values() if res[0] in [0, 1]]
    if not outcomes:
        consensus = "N/A"
    else:
        counts = {o: outcomes.count(o) for o in set(outcomes)}
        consensus = max(counts, key=counts.get)
        if len(counts) > 1:
            inconsistent_tests.append(test)
            consensus = f"CONFLICT ({consensus}?)"

    print(f"{test:<20}", end="")
    for s in summary:
        val = results.get(s['label'])
        if val:
            status = val[0]
            if status in [0, 1]:
                print(f" {status:<6}", end="")
            elif status == -2:
                print(f" {'TO':<6}", end="")
            elif status == -1:
                print(f" {'ERR':<6}", end="")
            else:
                print(f" {status:<6}", end="")
        else:
            print(f" {'-':<6}", end="")
    print(f" | {consensus}")

if inconsistent_tests:
    print("\nWARNING: Inconsistencies found in the following tests:")
    for t in inconsistent_tests:
        print(f"  - {t}")
        # Show detail for inconsistent test
        for s in summary:
            res = test_data[t].get(s['label'])
            if res and res[0] in [0, 1]:
                 print(f"    {s['label']}: {res[0]}")
else:
    print("\nAll successful runs agreed on realizability.")
