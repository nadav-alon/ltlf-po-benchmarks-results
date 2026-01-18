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

def get_job_label(job_id):
    import json
    label_file = "/home/cowclaw/results_shards/data/job_labels.json"
    if not job_id: return "Combined Data"
    if os.path.exists(label_file):
        try:
            with open(label_file, 'r') as f:
                labels = json.load(f)
                return labels.get(job_id, job_id)
        except: pass
    return job_id

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
    # Create job-specific subdirectory
    job_folder = job_id if job_id else "combined"
    target_dir = os.path.join(OUTPUT_DIR, job_folder)
    os.makedirs(target_dir, exist_ok=True)
    
    style = setup_plot_style()
    
    # Penalize timeouts for plotting
    df.loc[df['status'] == -2, 'time'] = TIMEOUT_PENALTY_MS
    plot_df = df[df['status'].isin([0, 1, -2])] # Exclude errors
    
    # 1. Generate charts for each implementation
    for impl in df['impl'].unique():
        if impl == 'unknown': continue
        filename = os.path.join(target_dir, f"results_{impl}.png")
        fig = plt.figure(figsize=(15, 12))
        label_text = get_job_label(job_id)
        fig.suptitle(f"Performance: {impl.capitalize()} ({label_text})", fontsize=16, fontweight='bold')
        
        # (a) Moving-Target
        ax1 = fig.add_subplot(221)
        sub_mt = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == 'Moving-Target')]
        if not sub_mt.empty:
            pivot = sub_mt.groupby(['value', 'mode'])['time'].mean().unstack()
            for mode in pivot.columns:
                ax1.plot(pivot.index, pivot[mode], label=mode, marker='o', alpha=0.7)
            ax1.set_yscale('log'); ax1.set_xlabel("n"); ax1.set_ylabel("Time (ms)")
            ax1.set_title("Moving-Target"); ax1.legend(); ax1.grid(True, alpha=0.3)

        # (b) Coin-Game
        ax2 = fig.add_subplot(222)
        sub_cg = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == 'Coin-Game')]
        if not sub_cg.empty:
            pivot = sub_cg.groupby(['value', 'mode'])['time'].mean().unstack()
            for mode in pivot.columns:
                ax2.plot(pivot.index, pivot[mode], label=mode, marker='o', alpha=0.7)
            ax2.set_yscale('log'); ax2.set_xlabel("n"); ax2.set_ylabel("Time (ms)")
            ax2.set_title("Coin-Game"); ax2.legend(); ax2.grid(True, alpha=0.3)

        # (c) Private-Peek (Spanning bottom row)
        ax3 = fig.add_subplot(212)
        sub_pp = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == 'Private-Peek')].copy()
        if not sub_pp.empty:
            sub_pp['label'] = sub_pp['value'].apply(lambda x: f"n={x[0]},m={x[1]}")
            sub_pp['sort'] = sub_pp['value'].apply(lambda x: x[0]*100 + x[1])
            pivot = sub_pp.sort_values('sort').groupby(['label', 'mode'], sort=False)['time'].mean().unstack()
            pivot.plot(kind='bar', ax=ax3, logy=True, width=0.8)
            ax3.set_ylabel("Time (ms)")
            ax3.set_title("Private-Peek (log)"); plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')
            
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.subplots_adjust(hspace=0.5)
        plt.savefig(filename, dpi=300)
        plt.close(fig)
        print(f"Saved: {filename}")

    # 2. Generate Comparison Plot (Direct Comparison layout)
    if len(df['impl'].unique()) > 1:
        comp_file = os.path.join(target_dir, "comparison.png")
        fig = plt.figure(figsize=(15, 12))
        label_text = get_job_label(job_id)
        fig.suptitle(f"Direct Comparison: Christian (Solid), Lucas (Dashed), Spot (Dotted) ({label_text})", fontsize=18, fontweight='bold')
        
        lucas_map = {'belief-states': 'Belief States', 'projection-based': 'Projection-Based', 'mso': 'MSO', 'belief': 'Projection-Based', 'direct': 'Belief States'}
        christian_map = {'belief': 'Belief', 'direct': 'Direct', 'mso': 'MSO'}
        spot_map = {'ltl': 'LTL', 'ltlf': 'LTLf', 'ltlfilt': 'LTLfilt'}
        
        colors = {'belief-states': 'blue', 'direct': 'red', 'projection-based': 'red', 'belief': 'blue', 'mso': 'green', 'ltl': 'black', 'ltlf': 'purple', 'ltlfilt': 'orange'}
        markers = {'christian': 'o', 'lucas': 'x', 'spot': 's'}
        linestyles = {'christian': '-', 'lucas': '--', 'spot': ':'}

        # (a) Moving-Target
        ax1 = fig.add_subplot(221)
        for impl in df['impl'].unique():
            sub = plot_df[(plot_df['benchmark'] == 'Moving-Target') & (plot_df['impl'] == impl)]
            if not sub.empty:
                pivot = sub.groupby(['value', 'mode'])['time'].mean().unstack()
                m_map = lucas_map if impl == 'lucas' else (christian_map if impl == 'christian' else spot_map)
                for mode in pivot.columns:
                    ax1.plot(pivot.index, pivot[mode], label=f"{impl.capitalize()} {m_map.get(mode, mode)}", 
                             marker=markers.get(impl, 'o'), linestyle=linestyles.get(impl, '-'), color=colors.get(mode, 'gray'), alpha=0.8)
        ax1.set_yscale('log'); ax1.set_xlabel("n"); ax1.set_ylabel("Time (ms)")
        ax1.legend(fontsize=8, ncol=2); ax1.grid(True, alpha=0.3)
        ax1.set_title("(a) Moving-Target")

        # (b) Coin-Game
        ax2 = fig.add_subplot(222)
        for impl in df['impl'].unique():
            sub = plot_df[(plot_df['benchmark'] == 'Coin-Game') & (plot_df['impl'] == impl)]
            if not sub.empty:
                pivot = sub.groupby(['value', 'mode'])['time'].mean().unstack()
                m_map = lucas_map if impl == 'lucas' else (christian_map if impl == 'christian' else spot_map)
                for mode in pivot.columns:
                    ax2.plot(pivot.index, pivot[mode], label=f"{impl.capitalize()} {m_map.get(mode, mode)}", 
                             marker=markers.get(impl, 'o'), linestyle=linestyles.get(impl, '-'), color=colors.get(mode, 'gray'), alpha=0.8)
        ax2.set_yscale('log'); ax2.set_xlabel("n"); ax2.set_ylabel("Time (ms)")
        ax2.legend(fontsize=8, ncol=2); ax2.grid(True, alpha=0.3)
        ax2.set_title("(b) Coin-Game")

        # (c) Private-Peek (Spanning bar chart)
        ax3 = fig.add_subplot(212)
        sub = plot_df[plot_df['benchmark'] == 'Private-Peek'].copy()
        if not sub.empty:
            sub['label'] = sub['value'].apply(lambda x: f"n={x[0]},m={x[1]}")
            sub['sort'] = sub['value'].apply(lambda x: x[0]*10 + x[1])
            summary = sub.sort_values('sort').groupby(['label', 'impl', 'mode'], sort=False)['time'].mean().unstack(level=[1, 2])
            summary.plot(kind='bar', ax=ax3, logy=True, width=0.8, alpha=0.9)
            ax3.set_ylabel("Time (ms)"); ax3.legend(fontsize=7, ncol=3, loc='upper left')
            plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')
            ax3.set_title("(c) Private-Peek (All methods)")

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.subplots_adjust(hspace=0.6)
        plt.savefig(comp_file, dpi=300)
        plt.close(fig)
        print(f"Saved: {comp_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolidated Visualization Tool")
    parser.add_argument("--job-id", help="Filter by Job ID")
    args = parser.parse_args()

    data = load_data(args.job_id)
    if not data.empty:
        generate_plots(data, args.job_id)
    else:
        print("No data to plot.")
