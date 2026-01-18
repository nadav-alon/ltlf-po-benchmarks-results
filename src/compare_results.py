import csv
import os
from collections import defaultdict

BASE_DIR = "/home/cowclaw/results_shards"
RESULTS_BASE = os.path.join(BASE_DIR, "data/results")

TRUTH_JOB_ID = "3104284"
TRUTH_TOOL = "lucas_mso"

COMPARE_JOB_ID = "3097478"
COMPARE_TOOLS = ["spot_ltl", "spot_ltlfilt"]

def load_results(job_id, tool_name):
    """
    Loads results for a given job_id and tool.
    Returns a dict: {test_name: status}
    """
    results = {}
    tool_dir = os.path.join(RESULTS_BASE, job_id, tool_name)
    
    if not os.path.exists(tool_dir):
        print(f"Warning: Directory not found: {tool_dir}")
        return results

    print(f"Loading results from {tool_dir}...")
    
    shard_files = [f for f in os.listdir(tool_dir) if f.startswith("shard_") and f.endswith(".csv")]
    
    for shard in shard_files:
        path = os.path.join(tool_dir, shard)
        try:
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    test = row['test']
                    try:
                        status = int(row['status'])
                        results[test] = status
                    except ValueError:
                        pass # Skip invalid status
        except Exception as e:
            print(f"Error reading {path}: {e}")
            
    return results

def main():
    print(f"Loading Source of Truth ({TRUTH_TOOL}) from Job {TRUTH_JOB_ID}...")
    truth_results = load_results(TRUTH_JOB_ID, TRUTH_TOOL)
    print(f"Loaded {len(truth_results)} results for Source of Truth.")
    
    inconsistencies = []

    for tool in COMPARE_TOOLS:
        print(f"\nComparing {tool} (Job {COMPARE_JOB_ID}) against Source of Truth...")
        tool_results = load_results(COMPARE_JOB_ID, tool)
        print(f"Loaded {len(tool_results)} results for {tool}.")
        
        common_tests = set(truth_results.keys()) & set(tool_results.keys())
        print(f"Found {len(common_tests)} common tests.")
        
        tool_inconsistencies = 0
        for test in common_tests:
            truth_status = truth_results[test]
            tool_status = tool_results[test]
            
            # We are looking for inconsistencies in realizability (0 vs 1)
            # Ignoring errors/timeouts (-1, -2) for inconsistency checks unless strictly specified otherwise.
            # Usually, inconsistency means one says Realizable (1) and the other says Unrealizable (0).
            
            if truth_status in [0, 1] and tool_status in [0, 1]:
                if truth_status != tool_status:
                    inc = {
                        'test': test,
                        'truth_tool': TRUTH_TOOL,
                        'truth_status': truth_status,
                        'compare_tool': tool,
                        'compare_status': tool_status
                    }
                    inconsistencies.append(inc)
                    tool_inconsistencies += 1
                    # print(f"Inconsistency: {test} | {TRUTH_TOOL}: {truth_status} vs {tool}: {tool_status}")

        print(f"Found {tool_inconsistencies} inconsistencies for {tool}.")

    # Report
    if inconsistencies:
        print("\n=== Inconsistencies Found ===")
        print(f"{'Test':<60} | {'Truth (' + TRUTH_TOOL + ')':<20} | {'Compared Tool':<20} | {'Status'}")
        print("-" * 120)
        for inc in inconsistencies:
            print(f"{inc['test']:<60} | {inc['truth_status']:<20} | {inc['compare_tool']:<20} | {inc['compare_status']}")
            
        # Also save to file
        out_file = os.path.join(BASE_DIR, "reports/text/inconsistencies.csv")
        print(f"\nSaving inconsistencies to {out_file}...")
        with open(out_file, 'w', newline='') as f:
            fieldnames = ['test', 'truth_tool', 'truth_status', 'compare_tool', 'compare_status']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(inconsistencies)
    else:
        print("\nNo inconsistencies found between valid results (0/1).")

if __name__ == "__main__":
    main()
