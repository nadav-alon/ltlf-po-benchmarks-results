import csv
import re
from collections import defaultdict

errors_file = '/home/cowclaw/results_shards/analysis_3097478/errors.csv'
output_report = '/home/cowclaw/results_shards/analysis_3097478/lucas_spot_error_report.md'

def normalize_error(msg):
    # Remove temp paths like /tmp/tmp.../
    msg = re.sub(r'/tmp/tmp[^/ ]+/', '/tmp/REDACTED/', msg)
    # Remove specific test paths to group by error type
    msg = re.sub(r'/RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/([^: ]+)', '[TEST_FILE]', msg)
    # Standardize whitespace
    msg = ' '.join(msg.split())
    return msg

def main():
    stats = defaultdict(lambda: defaultdict(int))
    examples = defaultdict(lambda: defaultdict(list))
    
    with open(errors_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tool = row['tool']
            if not (tool.startswith('lucas') or tool.startswith('spot')):
                continue
            
            raw_msg = row['error_message']
            status = row['status']
            
            if status == '-2':
                norm_msg = "Timeout"
            else:
                norm_msg = normalize_error(raw_msg)
            
            stats[tool][norm_msg] += 1
            if len(examples[tool][norm_msg]) < 5:
                examples[tool][norm_msg].append(row['test'])

    with open(output_report, 'w') as f:
        f.write("# Error Analysis for Lucas and Spot Tools (Job 3097478)\n\n")
        
        for tool in sorted(stats.keys()):
            f.write(f"## {tool}\n\n")
            f.write("| Error Type | Count |\n")
            f.write("| --- | --- |\n")
            
            # Sort by count descending
            sorted_errors = sorted(stats[tool].items(), key=lambda x: x[1], reverse=True)
            for msg, count in sorted_errors:
                f.write(f"| {msg} | {count} |\n")
            
            f.write("\n### Examples for major error types:\n")
            for msg, count in sorted_errors:
                if count > 0:
                    f.write(f"- **{msg}**:\n")
                    for ex in examples[tool][msg]:
                        f.write(f"  - `{ex}`\n")
            f.write("\n---\n\n")

    print(f"Report generated: {output_report}")

if __name__ == "__main__":
    main()
