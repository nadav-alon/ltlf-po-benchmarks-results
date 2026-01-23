#!/usr/bin/env python3
import csv
import os
import argparse
from collections import defaultdict

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPTS_DIR)
RESULTS_DIR = os.path.join(BASE_DIR, "data/results")

def load_tool_results(job_id, tool_name):
    """Loads results for a specific tool in a specific job."""
    results = {}
    path = os.path.join(RESULTS_DIR, job_id, tool_name, "shard_*.csv")
    files = glob_import_hack(path)
    
    for f in files:
        with open(f, 'r') as fd:
            # Skip comment lines
            non_comments = (line for line in fd if not line.strip().startswith('#'))
            reader = csv.DictReader(non_comments)
            for row in reader:
                try:
                    results[row['test']] = int(float(row['status']))
                except: pass
    return results

def glob_import_hack(pattern):
    import glob
    return glob.glob(pattern, recursive=True)

def compare_tools(job_a, tool_a, job_b, tool_b, output_csv=None):
    print(f"\nComparing [{tool_a}] (Job {job_a}) vs [{tool_b}] (Job {job_b})")
    
    res_a = load_tool_results(job_a, tool_a)
    res_b = load_tool_results(job_b, tool_b)
    
    common = set(res_a.keys()) & set(res_b.keys())
    print(f"Found {len(common)} common tests.")
    
    conflicts = []
    for test in sorted(common):
        sa, sb = res_a[test], res_b[test]
        if sa in [0, 1] and sb in [0, 1] and sa != sb:
            # Allow discrepancy if one tool is in full observability mode
            # and it finds the problem realizable (1) while the other (PO) found it unrealizable (0).
            is_fo_a = "ltlf-fo" in tool_a
            is_fo_b = "ltlf-fo" in tool_b
            
            if is_fo_a and sa == 1 and sb == 0:
                continue
            if is_fo_b and sb == 1 and sa == 0:
                continue
                
            conflicts.append({'test': test, 'val_a': sa, 'val_b': sb})

    if not conflicts:
        print("[+] No semantic conflicts found.")
    else:
        print(f"[!] Found {len(conflicts)} CONFLICTS!")
        for c in conflicts[:10]:
            print(f"  - {c['test']}: {c['val_a']} vs {c['val_b']}")
        if len(conflicts) > 10: print(f"  ... and {len(conflicts)-10} more.")
        
        if output_csv:
            with open(output_csv, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['test', 'val_a', 'val_b'])
                writer.writeheader()
                writer.writerows(conflicts)
            print(f"Saved conflicts to: {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cross-check tools for semantic consistency.")
    parser.add_argument("--job-a", required=True)
    parser.add_argument("--tool-a", required=True, help="e.g. lucas_mso")
    parser.add_argument("--job-b", required=True)
    parser.add_argument("--tool-b", required=True)
    parser.add_argument("--output", help="Save conflicts to CSV")
    args = parser.parse_args()

    compare_tools(args.job_a, args.tool_a, args.job_b, args.tool_b, args.output)
