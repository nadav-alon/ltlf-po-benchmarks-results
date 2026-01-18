import os
import csv
import glob
import argparse

def collect_errors(results_dir, job_id=None):
    error_instances = []
    unrealizable_instances = []

    if job_id:
        path_pattern = os.path.join(results_dir, job_id, "**", "shard_*.csv")
    else:
        path_pattern = os.path.join(results_dir, "**", "shard_*.csv")

    for filepath in glob.glob(path_pattern, recursive=True):
        dir_name = os.path.basename(os.path.dirname(filepath))
        parts = dir_name.split('_', 1)
        if len(parts) == 2:
            impl, method = parts[0], parts[1]
        else:
            impl, method = "unknown", dir_name
            
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    status = int(float(row['status']))
                    if status < 0:
                        error_instances.append({
                            'implementation': impl,
                            'method': method,
                            'test': row['test'],
                            'time': row['time'],
                            'status': status,
                            'file': os.path.basename(filepath)
                        })
                    elif status == 0:
                        unrealizable_instances.append({
                            'implementation': impl,
                            'method': method,
                            'test': row['test'],
                            'time': row['time'],
                            'status': status,
                            'file': os.path.basename(filepath)
                        })
                except (ValueError, KeyError, TypeError):
                    continue

    error_instances.sort(key=lambda x: (x['implementation'], x['method'], x['test']))
    return error_instances, unrealizable_instances

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect error instances from shards.")
    parser.add_argument("--job-id", help="Specific job ID folder to analyze")
    parser.add_argument("--results-dir", default="/home/cowclaw/results_shards/data/results", help="Directory containing results")
    args = parser.parse_args()

    error_instances, unrealizable_instances = collect_errors(args.results_dir, job_id=args.job_id)

    print(f"Total error instances (status < 0): {len(error_instances)}")
    print(f"Total unrealizable instances (status = 0): {len(unrealizable_instances)}")

    # Group by implementation and method for errors
    summary_errors = {}
    for inst in error_instances:
        key = (inst['implementation'], inst['method'], inst['status'])
        summary_errors[key] = summary_errors.get(key, 0) + 1

    print("\nError Summary by (Implementation, Method, Status):")
    print("(Status -1: Error, -2: Timeout)")
    for key, count in sorted(summary_errors.items()):
        print(f"{key}: {count}")

    # Print detailed error instances
    print("\nDetailed Error Instances:")
    for inst in error_instances:
        print(f"{inst['implementation']},{inst['method']},{inst['status']},{inst['test']}")
