import pandas as pd
import os
import glob

# Config
RESULTS_DIR = "/home/cowclaw/results_shards/data/results"
JOBS = {
    "FO": "3116131",
    "PO": "3104998",
    "FU": "3116117"
}

TOOLS = ["lucas_belief-states", "lucas_mso", "spot_ltlf"]

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

# Load all data
dfs = []
for label, job_id in JOBS.items():
    for tool in TOOLS:
        dfs.append(load_tool_data(job_id, tool))

# Merge all on test
final_df = dfs[0]
for next_df in dfs[1:]:
    final_df = pd.merge(final_df, next_df, on='test', how='outer')

status_map = {1: "Real", 0: "Unreal", -2: "TO", -1: "Err"}

def get_status(row, tool, job_key):
    val = row.get(f"{tool}_{JOBS[job_key]}")
    if pd.isna(val): return "N/A"
    return status_map.get(int(val), str(val))

results = []

# Transitions to check
transitions = [("FO", "PO"), ("PO", "FU"), ("FO", "FU")]

print(f"{'Test':<40} | {'Tool':<20} | {'From':<5} | {'To':<6}")
print("-" * 80)

inconsistencies = []

for _, row in final_df.iterrows():
    test_name = os.path.basename(row['test'])
    
    for start_key, end_key in transitions:
        has_transition = False
        tool_statuses = {}
        
        for tool in TOOLS:
            s_start = get_status(row, tool, start_key)
            s_end = get_status(row, tool, end_key)
            tool_statuses[tool] = (s_start, s_end)
            
            if s_start == "Real" and s_end == "Unreal":
                has_transition = True
        
        if has_transition:
            # Check for inconsistencies between tools for this transition
            # All tools that have data should agree on the result at each level
            # If Tool A says Real->Unreal and Tool B says Real->Real, that's an inconsistency.
            
            real_starts = [t for t, s in tool_statuses.items() if s[0] == "Real"]
            unreal_starts = [t for t, s in tool_statuses.items() if s[0] == "Unreal"]
            
            real_ends = [t for t, s in tool_statuses.items() if s[1] == "Real"]
            unreal_ends = [t for t, s in tool_statuses.items() if s[1] == "Unreal"]
            
            # Transition Table for this test
            print(f"\n{test_name} ({start_key} -> {end_key}):")
            print(f"  {'Tool':<20} | {'From':<6} | {'To':<6}")
            for tool, (s_start, s_end) in tool_statuses.items():
                print(f"  {tool:<20} | {s_start:<6} | {s_end:<6}")
            
            # Semantic cross-check
            if (real_starts and unreal_starts) or (real_ends and unreal_ends):
                inconsistencies.append({
                    "test": test_name,
                    "level": f"{start_key} or {end_key}",
                    "details": tool_statuses
                })

print("\n=== Inconsistency Analysis ===")
if not inconsistencies:
    print("No realizability inconsistencies found between tools for these transitions.")
else:
    for inc in inconsistencies:
        print(f"Inconsistency in {inc['test']} at {inc['level']}:")
        for tool, stats in inc['details'].items():
            print(f"  {tool}: {stats[0]} -> {stats[1]}")

# Also check for "Impossible" transitions (Unreal -> Real when decreasing observability)
print("\n=== Checking for Impossible Transitions (Unreal -> Real) ===")
impossible = []
for _, row in final_df.iterrows():
    test_name = os.path.basename(row['test'])
    for start_key, end_key in transitions:
        for tool in TOOLS:
            s_start = get_status(row, tool, start_key)
            s_end = get_status(row, tool, end_key)
            if s_start == "Unreal" and s_end == "Real":
                impossible.append(f"{test_name} ({tool}): {s_start} ({start_key}) -> {s_end} ({end_key})")

if not impossible:
     print("No impossible Unreal->Real transitions found.")
else:
    for imp in impossible:
        print(imp)
