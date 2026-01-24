import pandas as pd
import os
import glob
import re

# Config
RESULTS_DIR = "/home/cowclaw/results_shards/data/results"
JOBS = {
    "0%": "3114671",
    "25%": "3114682",
    "50%": "3114703",
    "75%": "3114714",
    "100%": "3114729"
}

def load_job_data(job_id):
    path_pattern = os.path.join(RESULTS_DIR, job_id, "spot_ltlf", "shard_*.csv")
    files = glob.glob(path_pattern)
    all_rows = []
    for f in files:
        df = pd.read_csv(f, comment='#')
        all_rows.append(df)
    if not all_rows: return pd.DataFrame()
    return pd.concat(all_rows)

summary = []

for label, job_id in JOBS.items():
    df = load_job_data(job_id)
    if df.empty: continue
    
    # Realizable = 1, Unrealizable = 0, Timeout = -2, Error = -1
    total = len(df)
    realizable = len(df[df['status'] == 1])
    unrealizable = len(df[df['status'] == 0])
    timeouts = len(df[df['status'] == -2])
    errors = len(df[df['status'] == -1])
    
    avg_time = df[df['status'] >= 0]['time'].mean()
    median_time = df[df['status'] >= 0]['time'].median()
    
    summary.append({
        "Observability": label,
        "Total": total,
        "Realizable": realizable,
        "Unrealizable": unrealizable,
        "Timeouts": timeouts,
        "Avg Time (ms)": round(avg_time, 2),
        "Median Time (ms)": round(median_time, 2),
        "Realizability %": round((realizable / total) * 100, 1) if total > 0 else 0
    })

summary_df = pd.DataFrame(summary)
print("=== Summary Analysis across Observability Levels ===")
print(summary_df.to_string(index=False))

# Detailed comparison: FO (0%) vs PO (100%)
df0 = load_job_data(JOBS["0%"])
df100 = load_job_data(JOBS["100%"])

if not df0.empty and not df100.empty:
    merged = pd.merge(df0, df100, on="test", suffixes=("_0", "_100"))
    # Filter for cases where both finished
    finished = merged[(merged['status_0'] >= 0) & (merged['status_100'] >= 0)].copy()
    finished['slowdown'] = finished['time_100'] / finished['time_0']
    
    print("\n=== Performance Trend (Realizable only in FO and 100% PO) ===")
    still_real = merged[(merged['status_0'] == 1) & (merged['status_100'] == 1)].copy()
    print(f"Num Benchmarks still Realizable at 100% PO: {len(still_real)}")
    
    # Load all jobs to check the trend for THESE SPECIFIC benchmarks
    trend_data = []
    for test in still_real['test']:
        row = {'test': os.path.basename(test)}
        for label, job_id in JOBS.items():
            df = load_job_data(job_id)
            row[label] = df[df['test'] == test]['time'].iloc[0]
        trend_data.append(row)
    
    trend_df = pd.DataFrame(trend_data)
    print("\nTrend of Median execution time for Benchmarks that remain Realizable:")
    print(trend_df[list(JOBS.keys())].median().to_string())

    print("\n=== Slowdown Analysis (0% -> 100%) ===")
    print(f"Max Slowdown: {finished['slowdown'].max():.2f}x")
    print(f"Mean Slowdown: {finished['slowdown'].mean():.2f}x")
    print(f"Median Slowdown: {finished['slowdown'].median():.2f}x")
    
    print("\n=== Benchmarks that changed Realizability (0% -> 100%) ===")
    changed = merged[merged['status_0'] != merged['status_100']]
    print(f"Count: {len(changed)}")
    for _, row in changed.head(10).iterrows():
        status_map = {1: "Real", 0: "Unreal", -2: "TO", -1: "Err"}
        name = os.path.basename(row['test'])
        print(f"  {name}: {status_map.get(row['status_0'])} -> {status_map.get(row['status_100'])}")
