import pandas as pd
import os
import glob

# Config
RESULTS_DIR = "/home/cowclaw/results_shards/data/results"
JOBS = {
    "FO": "3116131",
    "PO (Orig)": "3104998",
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
    return pd.concat(all_rows).drop_duplicates(subset=['test'])

report = []
report.append("# Observability Analysis: FO vs PO (Orig) vs FU")
report.append("Comparing Full Observability (FO), Original Partial Observability (PO), and Full Unobservability (FU).")
report.append(f"- **FO ({JOBS['FO']})**: All inputs observable (`po-part-0`)")
report.append(f"- **PO ({JOBS['PO (Orig)']})**: Original benchmarks (`part`) - *Source of Truth*")
report.append(f"- **FU ({JOBS['FU']})**: All inputs unobservable (`po-part-all`)")

for tool in TOOLS:
    report.append(f"\n## Tool: {tool}")
    
    df_fo = load_tool_data(JOBS["FO"], tool)
    df_po = load_tool_data(JOBS["PO (Orig)"], tool)
    df_fu = load_tool_data(JOBS["FU"], tool)
    
    if df_fo.empty or df_po.empty or df_fu.empty:
        report.append("Missing data for one of the jobs.")
        continue
    
    # Summary Table
    stats = []
    for label, df in [("FO", df_fo), ("PO (Orig)", df_po), ("FU", df_fu)]:
        total = len(df)
        realizable = len(df[df['status'] == 1])
        unrealizable = len(df[df['status'] == 0])
        timeouts = len(df[df['status'] == -2])
        errors = len(df[df['status'] == -1])
        avg_time = df[df['status'] >= 0]['time'].mean()
        
        stats.append({
            "Mode": label,
            "Total": total,
            "Realizable": realizable,
            "Unrealizable": unrealizable,
            "Timeouts": timeouts,
            "Errors": errors,
            "Avg Time (ms)": round(avg_time, 2)
        })
    
    report.append("| Mode | Total | Realizable | Unrealizable | Timeouts | Errors | Avg Time (ms) |")
    report.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    for s in stats:
        report.append(f"| {s['Mode']} | {s['Total']} | {s['Realizable']} | {s['Unrealizable']} | {s['Timeouts']} | {s['Errors']} | {s['Avg Time (ms)']} |")
    
    # Transitions
    merged = pd.merge(df_fo, df_po, on="test", suffixes=("_fo", "_po"))
    merged = pd.merge(merged, df_fu, on="test")
    # Columns now: status_fo, status_po, status (fu)
    merged.rename(columns={"status": "status_fu", "time": "time_fu"}, inplace=True)
    
    report.append("\n### Realizability Transitions")
    
    # 1. FO (Real) -> PO (Unreal)
    fo_to_po = merged[(merged['status_fo'] == 1) & (merged['status_po'] == 0)]
    report.append(f"- **FO (Real) -> PO (Unreal)**: {len(fo_to_po)} benchmarks")
    
    # 2. PO (Real) -> FU (Unreal)
    po_to_fu = merged[(merged['status_po'] == 1) & (merged['status_fu'] == 0)]
    report.append(f"- **PO (Real) -> FU (Unreal)**: {len(po_to_fu)} benchmarks")

    # 3. FO (Real) -> FU (Unreal)
    fo_to_fu = merged[(merged['status_fo'] == 1) & (merged['status_fu'] == 0)]
    report.append(f"- **FO (Real) -> FU (Unreal)**: {len(fo_to_fu)} benchmarks")

    # Runtime Comparison
    # Compare PO vs FO
    both_fo_po = merged[(merged['status_fo'] == 1) & (merged['status_po'] == 1)].copy()
    if not both_fo_po.empty:
        both_fo_po['slowdown'] = both_fo_po['time_po'] / both_fo_po['time_fo']
        report.append(f"\n### Runtime: FO vs PO (Orig)")
        report.append(f"- Count (Realizable in both): {len(both_fo_po)}")
        report.append(f"- Median Slowdown (FO -> PO): {both_fo_po['slowdown'].median():.2f}x")

    # Compare FU vs PO
    both_po_fu = merged[(merged['status_po'] == 1) & (merged['status_fu'] == 1)].copy()
    if not both_po_fu.empty:
        both_po_fu['slowdown'] = both_po_fu['time_fu'] / both_po_fu['time_po']
        report.append(f"\n### Runtime: PO (Orig) vs FU")
        report.append(f"- Count (Realizable in both): {len(both_po_fu)}")
        report.append(f"- Median Slowdown (PO -> FU): {both_po_fu['slowdown'].median():.2f}x")

    # Visualizations
    report.append("\n### Performance Comparison Graph")
    tool_slug = tool.replace(':', '_').replace('-', '_')
    fo_po_dir = f"{JOBS['FO']}_{tool_slug}_{JOBS['PO (Orig)']}_{tool_slug}"
    po_fu_dir = f"{JOBS['PO (Orig)']}_{tool_slug}_{JOBS['FU']}_{tool_slug}"
    
    report.append(f"| FO vs PO (Orig) | PO (Orig) vs FU |")
    report.append(f"| :---: | :---: |")
    report.append(f"| ![{tool} FO vs PO](figures/{fo_po_dir}/scatter_fo_vs_po_all.png) | ![{tool} PO vs FU](figures/{po_fu_dir}/scatter_fo_vs_po_all.png) |")

    report.append("\n---")

with open("/home/cowclaw/results_shards/reports/OBSERVABILITY_ANALYSIS.md", "w") as f:
    f.write("\n".join(report))

print("Report generated successfully.")
