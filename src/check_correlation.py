import csv
import os
from collections import defaultdict
import pandas as pd
import numpy as np

JOB_ID = "3097478"
BASE_DIR = "/home/cowclaw/results_shards"
ANALYSIS_DIR = os.path.join(BASE_DIR, f"analysis_{JOB_ID}")
CONSOLIDATED_FILE = os.path.join(ANALYSIS_DIR, "consolidated_results.csv")

def main():
    if not os.path.exists(CONSOLIDATED_FILE):
        print(f"Error: {CONSOLIDATED_FILE} not found.")
        return

    df = pd.read_csv(CONSOLIDATED_FILE)
    
    # We only care about outcomes 0 and 1 for agreement check
    # status 1 = realizable, 0 = unrealizable
    results_df = df[df['status'].isin([0, 1])].copy()
    
    # Pivot to have tools as columns and tests as rows
    pivot_df = results_df.pivot(index='test', columns='tool', values='status')
    
    tools = sorted(pivot_df.columns.tolist())
    num_tools = len(tools)
    
    agreement_matrix = np.zeros((num_tools, num_tools))
    conflict_matrix = np.zeros((num_tools, num_tools))
    common_coverage_matrix = np.zeros((num_tools, num_tools))
    
    for i in range(num_tools):
        for j in range(num_tools):
            t1 = tools[i]
            t2 = tools[j]
            
            # Tests where both tools have a result
            mask = pivot_df[t1].notna() & pivot_df[t2].notna()
            common_tests = pivot_df[mask]
            
            common_count = len(common_tests)
            common_coverage_matrix[i, j] = common_count
            
            if common_count > 0:
                # Agreement: both have same status
                agree = (common_tests[t1] == common_tests[t2]).sum()
                agreement_matrix[i, j] = agree / common_count
                conflict_matrix[i, j] = common_count - agree
            else:
                agreement_matrix[i, j] = np.nan

    # Print Summary Report
    print(f"Tool Agreement Analysis for Job {JOB_ID}")
    print("=" * 40)
    print("\nAgreement % between tools (on tests where both succeeded):")
    
    # Create a nice table for the output
    header = f"{'Tool':<25}" + "".join([f"{t[:6]:>8}" for t in tools])
    print(header)
    print("-" * len(header))
    
    for i in range(num_tools):
        row = f"{tools[i]:<25}"
        for j in range(num_tools):
            val = agreement_matrix[i, j]
            if np.isnan(val):
                row += f"{'N/A':>8}"
            else:
                row += f"{val*100:>7.1f}%"
        print(row)

    print("\nConflict count (where tools disagreed on realizability):")
    print(header)
    print("-" * len(header))
    for i in range(num_tools):
        row = f"{tools[i]:<25}"
        for j in range(num_tools):
            val = conflict_matrix[i, j]
            row += f"{int(val):>8}"
        print(row)

    print("\nCommon coverage (number of tests both tools solved):")
    print(header)
    print("-" * len(header))
    for i in range(num_tools):
        row = f"{tools[i]:<25}"
        for j in range(num_tools):
            val = common_coverage_matrix[i, j]
            row += f"{int(val):>8}"
        print(row)

    # Specific check requested by user: spot_ltlf vs lucas_mso
    target1 = 'spot_ltlf'
    target2 = 'lucas_mso'
    
    if target1 in tools and target2 in tools:
        idx1 = tools.index(target1)
        idx2 = tools.index(target2)
        agree_pct = agreement_matrix[idx1, idx2] * 100
        conflicts = int(conflict_matrix[idx1, idx2])
        common = int(common_coverage_matrix[idx1, idx2])
        
        print(f"\nDetailed check: {target1} vs {target2}")
        print(f"  Shared solved tests: {common}")
        print(f"  Agreement: {agree_pct:.2f}%")
        print(f"  Conflicts: {conflicts}")
        
        if conflicts > 0:
            print(f"\nList of conflict tests between {target1} and {target2}:")
            mask = pivot_df[target1].notna() & pivot_df[target2].notna() & (pivot_df[target1] != pivot_df[target2])
            conflict_tests = pivot_df[mask]
            for test, row in conflict_tests.iterrows():
                print(f"  - {test}: {target1}={int(row[target1])}, {target2}={int(row[target2])}")

if __name__ == "__main__":
    main()
