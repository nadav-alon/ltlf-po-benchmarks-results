import pandas as pd
import os
import glob
import sys

# Config
RESULTS_DIR = "/home/cowclaw/results_shards/data/results"
JOBS = {
    "FO": "3116131",
    "PO": "3104998",
    "FU": "3116117"
}

TOOLS = ["lucas_belief-states", "lucas_mso", "spot_ltlf"]
STATUS_MAP = {1: "Real", 0: "Unreal", -2: "TO", -1: "Err"}

def load_tool_data(job_id, tool):
    path_pattern = os.path.join(RESULTS_DIR, job_id, tool, "shard_*.csv")
    files = glob.glob(path_pattern)
    all_rows = []
    for f in files:
        try:
            df = pd.read_csv(f, comment='#')
            all_rows.append(df)
        except Exception as e:
            pass
    if not all_rows: return pd.DataFrame()
    df = pd.concat(all_rows).drop_duplicates(subset=['test'])
    # Keep only test and status
    return df[['test', 'status']].rename(columns={'status': f"{tool}_{job_id}"})

print("Loading all results...")
dfs = []
for label, job_id in JOBS.items():
    for tool in TOOLS:
        print(f"  Loading {tool} from Job {job_id} ({label})")
        dfs.append(load_tool_data(job_id, tool))

# Merge all on test
print("Merging data...")
final_df = dfs[0]
for next_df in dfs[1:]:
    final_df = pd.merge(final_df, next_df, on='test', how='outer')

# Normalize column names for easier access
# tool_FO, tool_PO, tool_FU
col_map = {}
for tool in TOOLS:
    for label, job_id in JOBS.items():
        old_col = f"{tool}_{job_id}"
        new_col = f"{tool}_{label}"
        if old_col in final_df.columns:
            # Map status codes to labels
            final_df[new_col] = final_df[old_col].map(lambda x: STATUS_MAP.get(int(x), str(x)) if pd.notnull(x) else "N/A")
            final_df.drop(columns=[old_col], inplace=True)

# Add consistency check columns
print("Adding analysis columns...")

def check_consistency(row):
    for label in JOBS.keys():
        statuses = [row[f"{tool}_{label}"] for tool in TOOLS if f"{tool}_{label}" in row]
        real = "Real" in statuses
        unreal = "Unreal" in statuses
        if real and unreal:
            return f"Conflict in {label}"
    return "Check"

final_df['Consistency_Status'] = final_df.apply(check_consistency, axis=1)

# Sort by test name
final_df['test_basename'] = final_df['test'].apply(os.path.basename)
final_df.sort_values('test_basename', inplace=True)
cols = ['test_basename', 'Consistency_Status'] + [c for c in final_df.columns if c not in ['test', 'test_basename', 'Consistency_Status']]
final_df = final_df[cols]

# Output
output_path = "/home/cowclaw/results_shards/reports/FULL_CROSS_CHECK.csv"
final_df.to_csv(output_path, index=False)
print(f"\nSaved full cross-check report to: {output_path}")

# Try to save to Excel if possible
try:
    import openpyxl
    excel_path = "/home/cowclaw/results_shards/reports/FULL_CROSS_CHECK.xlsx"
    final_df.to_excel(excel_path, index=False)
    print(f"Also saved Excel report to: {excel_path}")
except ImportError:
    print("Note: 'openpyxl' not found, skipping Excel output. CSV is available.")

# Print summary
print("\n=== Summary ===")
total_tests = len(final_df)
conflicts = len(final_df[final_df['Consistency_Status'].str.startswith("Conflict")])
print(f"Total benchmarks: {total_tests}")
print(f"Benchmarks with tool conflicts: {conflicts}")

if conflicts > 0:
    print("\nSample conflicts:")
    print(final_df[final_df['Consistency_Status'].str.startswith("Conflict")].head(10).to_string(index=False))
