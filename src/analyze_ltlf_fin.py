import pandas as pd
import os
from pathlib import Path

def load_results(job_id, results_base="/home/cowclaw/results_shards/data/results"):
    job_path = Path(results_base) / job_id / "spot_ltlf"
    all_data = []
    if not job_path.exists():
        return pd.DataFrame()
    for shard in job_path.glob("*.csv"):
        # Skipping comment lines
        df = pd.read_csv(shard, comment='#')
        all_data.append(df)
    return pd.concat(all_data) if all_data else pd.DataFrame()

def load_mona_results(mona_csv="/home/cowclaw/ltlf-po-benchmarks/ltlf-fin-benchmarks/mona_results.csv"):
    if not os.path.exists(mona_csv):
        return pd.DataFrame()
    df = pd.read_csv(mona_csv)
    # Extract benchmark name and level from mona_file
    # Examples:
    # hpc-mona/uright_pb_07_pe_.mona -> level: FO, bench: uright_pb_07_pe_
    # hpc-mona/po-mso-1-2_uright_pb_07_pe_.mona -> level: PO 50%, bench: uright_pb_07_pe_
    # hpc-mona/po-mso-all_uright_pb_07_pe_.mona -> level: PO 100%, bench: uright_pb_07_pe_
    
    def parse_mona(row):
        path = row['mona_file']
        name = Path(path).name
        if name.startswith("po-mso-0_"):
            return "FO", name.replace("po-mso-0_", "").split(".")[0]
        elif name.startswith("po-mso-1-2_"):
            return "PO 50%", name.replace("po-mso-1-2_", "").split(".")[0]
        elif name.startswith("po-mso-all_"):
            return "PO 100%", name.replace("po-mso-all_", "").split(".")[0]
        elif "_" not in name: # fallback for structured paths if they were used
            return "MSO", name.split(".")[0]
        return None, None

    df[['level', 'bench']] = df.apply(lambda r: pd.Series(parse_mona(r)), axis=1)
    return df.dropna(subset=['level'])

def analyze():
    # Job mappings
    jobs = {
        "3116651": "FO",
        "3116652": "PO 50%",
        "3116666": "PO 100%"
    }
    
    combined = []
    for job_id, label in jobs.items():
        df = load_results(job_id)
        if df.empty:
            continue
        df['level'] = label
        # Clean up test name to just the stem
        df['bench'] = df['test'].apply(lambda x: Path(x).stem)
        combined.append(df)
    
    if not combined:
        print("No data found.")
        return
        
    df_all = pd.concat(combined)
    
    # Normalize units:
    # runTests.py BUG: It records 'timeout' (seconds) for timeouts (status -2)
    # but records 'time_ms' (milliseconds) for successes/errors.
    # We normalize everything to seconds.
    def normalize_time(row):
        if row['status'] == -2:
            return row['time'] # already in seconds
        return row['time'] / 1000.0 # convert ms to seconds
        
    df_all['time'] = df_all.apply(normalize_time, axis=1)
    
    # Load Mona data
    df_mona = load_mona_results()
    if not df_mona.empty:
        # Renaming columns before merge to avoid matching issues and suffixes confusion
        df_mona = df_mona.rename(columns={'runtime': 'runtime_mona', 'status': 'status_mona'})
        # Merge with Spot results
        df_all = df_all.merge(df_mona[['bench', 'level', 'runtime_mona', 'status_mona']], 
                             on=['bench', 'level'], 
                             how='left')
    else:
        print("Warning: Mona results dataframe is empty or missing.")

    # Analysis 1: Realizability Impact
    pivot_real = df_all.groupby(['bench', 'level'])['status'].first().unstack()
    
    print("### Realizability Changes (Spot)")
    print("Total Benchmarks:", len(pivot_real))
    
    for start, end in [("FO", "PO 50%"), ("PO 50%", "PO 100%"), ("FO", "PO 100%")]:
        if start in pivot_real.columns and end in pivot_real.columns:
            became_unreal = pivot_real[(pivot_real[start] == 0) & (pivot_real[end] == 1)]
            print(f"\n{start} -> {end}: {len(became_unreal)} benchmarks became unrealizable.")

    # Analysis 2: Runtime Impact
    print("\n### Spot Synthesis Runtime (Mean)")
    print(df_all.groupby('level')['time'].mean())

    if not df_mona.empty:
        print("\n### Mona Automaton Generation Runtime (Mean)")
        print(df_all.groupby('level')['runtime_mona'].mean())
        
        print("\n### Total Runtime (Spot + Mona Generation)")
        df_all['total_time'] = df_all['time'] + df_all['runtime_mona'].fillna(0)
        print(df_all.groupby('level')['total_time'].mean())

    # Comparison factors
    pivot_time = df_all.groupby(['bench', 'level'])['time'].mean().unstack()
    print("\n### Spot Mean Runtime Factor vs FO")
    for lvl in ["PO 50%", "PO 100%"]:
        if lvl in pivot_time.columns and "FO" in pivot_time.columns:
            ratios = pivot_time[lvl] / pivot_time['FO']
            print(f"{lvl} Mean Factor: {ratios.mean():.2f}x")
            print(f"{lvl} Median Factor: {ratios.median():.2f}x")
            print(f"{lvl} Top 5 Outliers (Ratio):")
            print(ratios.sort_values(ascending=False).head(5))

    # Check for timeouts (status != 0)
    print("\n### Status Breakdown")
    print(df_all.groupby(['level', 'status']).size().unstack(fill_value=0))

if __name__ == "__main__":
    analyze()
