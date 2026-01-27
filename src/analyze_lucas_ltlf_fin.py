import pandas as pd
import os
from pathlib import Path

def load_results(job_id, tool, results_base="/home/cowclaw/results_shards/data/results"):
    job_path = Path(results_base) / job_id / tool
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
    
    def parse_mona(row):
        path = row['mona_file']
        name = Path(path).name
        if name.startswith("po-mso-0_"):
            return "FO", name.replace("po-mso-0_", "").split(".")[0]
        elif name.startswith("po-mso-1-2_"):
            return "PO 50%", name.replace("po-mso-1-2_", "").split(".")[0]
        elif name.startswith("po-mso-all_"):
            return "PO 100%", name.replace("po-mso-all_", "").split(".")[0]
        elif "_" not in name: 
            return "MSO", name.split(".")[0]
        return None, None

    df[['level', 'bench']] = df.apply(lambda r: pd.Series(parse_mona(r)), axis=1)
    return df.dropna(subset=['level'])

def analyze_tool(tool, job_mapping, df_mona):
    print(f"\n{'='*20}\nAnalyzing {tool}\n{'='*20}")
    
    combined = []
    for job_id, label in job_mapping.items():
        df = load_results(job_id, tool)
        if df.empty:
            continue
        df['level'] = label
        df['bench'] = df['test'].apply(lambda x: Path(x).stem)
        combined.append(df)
    
    if not combined:
        print(f"No data found for {tool}.")
        return None
        
    df_all = pd.concat(combined)
    
    def normalize_time(row):
        if row['status'] == -2:
            return row['time'] # already in seconds
        return row['time'] / 1000.0 # convert ms to seconds
        
    df_all['time'] = df_all.apply(normalize_time, axis=1)
    
    if not df_mona.empty:
        # Deduplicate MONA results before merge
        df_mona_clean = df_mona[['bench', 'level', 'runtime_mona', 'status_mona']].drop_duplicates(subset=['bench', 'level'])
        df_all = df_all.merge(df_mona_clean, 
                             on=['bench', 'level'], 
                             how='left')

    # Analysis 1: Realizability Impact
    pivot_real = df_all.groupby(['bench', 'level'])['status'].first().unstack()
    
    print(f"### Realizability Changes ({tool})")
    print("Total Benchmarks:", len(pivot_real))
    
    for start, end in [("FO", "PO 50%"), ("PO 50%", "PO 100%"), ("FO", "PO 100%")]:
        if start in pivot_real.columns and end in pivot_real.columns:
            # We assume status 0 is realizable, status 1 is unrealizable
            valid = pivot_real[(pivot_real[start].isin([0, 1])) & (pivot_real[end].isin([0, 1]))]
            became_unreal = valid[(valid[start] == 0) & (valid[end] == 1)]
            became_real = valid[(valid[start] == 1) & (valid[end] == 0)]
            print(f"\n{start} -> {end}:")
            print(f"  {len(became_unreal)} benchmarks became unrealizable.")
            if len(became_real) > 0:
                print(f"  WARNING: {len(became_real)} benchmarks became realizable (INCONSISTENCY).")
            print(f"  (Based on {len(valid)} benchmarks with valid status at both levels)")

    # Analysis 2: Runtime Impact
    print(f"\n### {tool} Synthesis Runtime (Mean)")
    print(df_all.groupby('level')['time'].mean())

    if not df_mona.empty:
        print("\n### Mona Automaton Generation Runtime (Mean)")
        print(df_all.groupby('level')['runtime_mona'].mean())
        
        print(f"\n### Total Runtime ({tool} + Mona Generation)")
        df_all['total_time'] = df_all['time'] + df_all['runtime_mona'].fillna(0)
        print(df_all.groupby('level')['total_time'].mean())

    # Comparison factors
    pivot_time = df_all.groupby(['bench', 'level'])['time'].mean().unstack()
    print(f"\n### {tool} Mean Runtime Factor vs FO")
    for lvl in ["PO 50%", "PO 100%"]:
        if lvl in pivot_time.columns and "FO" in pivot_time.columns:
            # Filter to cases where FO synthesis was successful/timeout (not error)
            success_both = pivot_time[(pivot_time[lvl] > 0) & (pivot_time['FO'] > 0)]
            if not success_both.empty:
                ratios = success_both[lvl] / success_both['FO']
                print(f"{lvl} Mean Factor: {ratios.mean():.2f}x (n={len(success_both)})")
                print(f"{lvl} Median Factor: {ratios.median():.2f}x")
            else:
                print(f"{lvl}: No overlapping successful runs found.")

    # Check for timeouts (status != 0)
    print("\n### Status Breakdown")
    # Status codes: 0: Realizable, 1: Unrealizable, -1: Error, -2: Timeout
    status_summary = df_all.groupby(['level', 'status']).size().unstack(fill_value=0)
    print(status_summary)
    
    return df_all

def main():
    df_mona = load_mona_results()
    if not df_mona.empty:
        df_mona = df_mona.rename(columns={'runtime': 'runtime_mona', 'status': 'status_mona'})
    else:
        print("Warning: Mona results dataframe is empty or missing.")

    job_configs = {
        "lucas_mso": {
            "3116823": "FO",
            "3116850": "PO 50%",
            "3116862": "PO 100%"
        },
        "lucas_belief-states": {
            "3116823": "FO",
            "3116857": "PO 50%",
            "3116862": "PO 100%"
        }
    }

    for tool, mapping in job_configs.items():
        analyze_tool(tool, mapping, df_mona)

if __name__ == "__main__":
    main()
