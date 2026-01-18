#!/usr/bin/env python3
import os
import csv
import glob
import argparse
from collections import defaultdict

def report_errors(results_dir, job_id=None, output_csv=None, detail=False):
    if job_id:
        path_pattern = os.path.join(results_dir, job_id, "**", "shard_*.csv")
    else:
        path_pattern = os.path.join(results_dir, "**", "shard_*.csv")

    # tool -> error_type -> [rows]
    errors = defaultdict(lambda: defaultdict(list))
    total_found = 0

    for filepath in glob.glob(path_pattern, recursive=True):
        dir_name = os.path.basename(os.path.dirname(filepath))
        
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    status = int(float(row['status']))
                    if status < 0:
                        err_type = "Timeout" if status == -2 else "Error"
                        errors[dir_name][err_type].append({
                            'test': row['test'],
                            'time': row['time'],
                            'status': status,
                            'shard': os.path.basename(filepath)
                        })
                        total_found += 1
                except (ValueError, KeyError, TypeError): continue

    if not errors:
        print("No errors or timeouts found.")
        return

    # 1. Print Summary
    print(f"\nFound {total_found} failed instances across {len(errors)} tools.\n")
    print(f"{'Tool Path':<40} {'Errors':<10} {'Timeouts':<10}")
    print("-" * 65)
    for tool, types in sorted(errors.items()):
        e_count = len(types['Error'])
        t_count = len(types['Timeout'])
        print(f"{tool:<40} {e_count:<10} {t_count:<10}")

    # 2. Print Detailed List (if requested)
    if detail:
        print("\n" + "="*80)
        print("DETAILED ERROR LIST (Status -1)")
        print("="*80)
        for tool, types in sorted(errors.items()):
            if types['Error']:
                print(f"\n### {tool}")
                for item in sorted(types['Error'], key=lambda x: x['test']):
                    print(f"  - {item['test']}")

    # 3. Export to CSV (if requested)
    if output_csv:
        with open(output_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['tool', 'type', 'status', 'test', 'time', 'shard'])
            for tool, types in errors.items():
                for etype, items in types.items():
                    for item in items:
                        writer.writerow([tool, etype, item['status'], item['test'], item['time'], item['shard']])
        print(f"\n[+] Exported all failed instances to: {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolidated Error Reporting Tool")
    parser.add_argument("--job-id", help="Filter by Job ID")
    parser.add_argument("--results-dir", default="/home/cowclaw/results_shards/data/results")
    parser.add_argument("--csv", help="Export failures to this CSV file")
    parser.add_argument("--list", action="store_true", help="Print full list of erroring test names")
    args = parser.parse_args()

    # Determine default CSV output if none provided but we want to save
    report_errors(args.results_dir, job_id=args.job_id, output_csv=args.csv, detail=args.list)
