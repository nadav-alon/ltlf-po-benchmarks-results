import os
import csv
import glob
import argparse

def save_errors(results_dir, output_csv, job_id=None):
    if job_id:
        path_pattern = os.path.join(results_dir, job_id, "*.csv")
    else:
        path_pattern = os.path.join(results_dir, "**", "*.csv")

    with open(output_csv, 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['implementation', 'method', 'status', 'test', 'time', 'shard_file'])
        
        for filepath in sorted(glob.glob(path_pattern, recursive=True)):
            filename = os.path.basename(filepath)
            if filename.endswith('.csv'):
                parts = filename.replace('.csv', '').split('_')
                if len(parts) < 3: continue
                impl = parts[1]
                method = parts[2]
                
                with open(filepath, 'r') as f_in:
                    reader = csv.DictReader(f_in)
                    for row in reader:
                        status = int(float(row['status']))
                        if status < 0:
                            writer.writerow([impl, method, status, row['test'], row['time'], filename])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save error instances to CSV.")
    parser.add_argument("--job-id", help="Specific job ID folder to analyze")
    parser.add_argument("--results-dir", default="/home/cowclaw/results_shards/results", help="Directory containing results")
    parser.add_argument("--output", default="/home/cowclaw/results_shards/collected_errors.csv", help="Output CSV file")
    args = parser.parse_args()

    save_errors(args.results_dir, args.output, job_id=args.job_id)
    print(f"Collected error instances saved to {args.output}")
