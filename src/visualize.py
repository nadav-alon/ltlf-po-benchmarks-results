#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import re
import argparse

# Config
BASE_DIR = "/home/cowclaw/results_shards"
RESULTS_DIR = os.path.join(BASE_DIR, "data/results")
OUTPUT_DIR = os.path.join(BASE_DIR, "reports/figures")
TIMEOUT_PENALTY_MS = 300000

def parse_tool(filepath):
    """Extract implementation and mode from directory name."""
    dir_name = os.path.basename(os.path.dirname(filepath))
    parts = dir_name.split('_', 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return "unknown", dir_name

def parse_test_name(test_path):
    """Identify benchmark family and scale."""
    if 'seek_' in test_path:
        match = re.search(r'seek_(\d+)', test_path)
        if match: return 'Moving-Target', int(match.group(1))
    elif 'coins_' in test_path:
        match = re.search(r'coins_(\d+)', test_path)
        if match: return 'Coin-Game', int(match.group(1))
    elif 'peek_' in test_path:
        match = re.search(r'peek_(\d+)_(\d+)', test_path)
        if match: return 'Private-Peek', (int(match.group(1)), int(match.group(2)))
    return None, None

def load_data(job_id=None):
    all_data = []
    path_pattern = os.path.join(RESULTS_DIR, job_id if job_id else "**", "**", "shard_*.csv")
    
    for filepath in glob.glob(path_pattern, recursive=True):
        impl, mode = parse_tool(filepath)
        try:
            df = pd.read_csv(filepath)
            for _, row in df.iterrows():
                benchmark, val = parse_test_name(row['test'])
                if benchmark:
                    all_data.append({
                        'impl': impl, 'mode': mode, 'benchmark': benchmark, 'value': val,
                        'time': float(row['time']), 'status': int(float(row['status']))
                    })
        except Exception as e: print(f"Error reading {filepath}: {e}")
            
    return pd.DataFrame(all_data)

def setup_plot_style():
    plt.rcParams.update({'font.size': 12})
    return {
        'colors': {'belief-states': 'blue', 'direct': 'blue', 'projection-based': 'red', 'belief': 'red', 'mso': 'green', 'ltl': 'black', 'ltlf': 'purple'},
        'markers': {'christian': 'o', 'lucas': 'x', 'spot': 's'},
        'lines': {'christian': '-', 'lucas': '--', 'spot': ':'}
    }

def generate_plots(df, job_id=None):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    suffix = f"_{job_id}" if job_id else ""
    style = setup_plot_style()
    
    # Penalize timeouts for plotting
    df.loc[df['status'] == -2, 'time'] = TIMEOUT_PENALTY_MS
    plot_df = df[df['status'].isin([0, 1, -2])] # Exclude errors
    
    # Generate charts for each implementation
    for impl in df['impl'].unique():
        if impl == 'unknown': continue
        filename = os.path.join(OUTPUT_DIR, f"results_{impl}{suffix}.png")
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle(f"Performance: {impl.capitalize()} ({job_id if job_id else 'All Data'})", fontsize=16, fontweight='bold')
        
        # (a) Moving-Target & (b) Coin-Game (Line Plots)
        for i, (bench, title) in enumerate([('Moving-Target', 'n'), ('Coin-Game', 'n')]):
            ax = axes[0, i]
            sub = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == bench)]
            if not sub.empty:
                pivot = sub.groupby(['value', 'mode'])['time'].mean().unstack()
                for mode in pivot.columns:
                    ax.plot(pivot.index, pivot[mode], label=mode, marker='o', alpha=0.7)
                ax.set_yscale('log'); ax.set_xlabel(title); ax.set_ylabel("Time (ms)")
                ax.set_title(bench); ax.legend(); ax.grid(True, alpha=0.3)

        # (c) Private-Peek (Bar Chart)
        ax = axes[1, 0]
        sub = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == 'Private-Peek')].copy()
        if not sub.empty:
            sub['label'] = sub['value'].apply(lambda x: f"{x[0]},{x[1]}")
            sub['sort'] = sub['value'].apply(lambda x: x[0]*100 + x[1])
            pivot = sub.sort_values('sort').groupby(['label', 'mode'], sort=False)['time'].mean().unstack()
            pivot.plot(kind='bar', ax=ax, logy=True, width=0.8)
            ax.set_title("Private-Peek (log)"); plt.setp(ax.get_xticklabels(), rotation=45)
            
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(filename, dpi=300)
        print(f"Saved: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolidated Visualization Tool")
    parser.add_argument("--job-id", help="Filter by Job ID")
    args = parser.parse_args()

    data = load_data(args.job_id)
    if not data.empty:
        generate_plots(data, args.job_id)
    else:
        print("No data to plot.")
