#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import re
import argparse

# Config
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPTS_DIR)
RESULTS_DIR = os.path.join(BASE_DIR, "data/results")
OUTPUT_DIR = os.path.join(BASE_DIR, "reports/figures")
TIMEOUT_PENALTY_MS = 300000

def get_job_label(job_id):
    import json
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    label_file = os.path.join(os.path.dirname(scripts_dir), "data", "job_labels.json")
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

def load_data(job_identifiers=None, custom_labels=None):
    all_data = []
    
    # If no job_identifiers provided, scan for all directories in RESULTS_DIR that are numeric
    if not job_identifiers:
        if os.path.exists(RESULTS_DIR):
            job_identifiers = [d for d in os.listdir(RESULTS_DIR) if os.path.isdir(os.path.join(RESULTS_DIR, d)) and d.isdigit()]
            job_identifiers.sort()
        else:
            return pd.DataFrame()

    for i, ident in enumerate(job_identifiers):
        # Format: JOB_ID-FILTER (e.g., 3114465-spot:ltlf)
        if '-' in ident:
            job_id, filter_str = ident.split('-', 1)
            filter_dir = filter_str.replace(':', '_')
        else:
            job_id = ident
            filter_str = None
            filter_dir = "**"
            
        # Determine label for this run
        if custom_labels and i < len(custom_labels):
            label = custom_labels[i]
        else:
            base_label = get_job_label(job_id)
            label = f"{base_label} [{filter_str}]" if filter_str else base_label
        
        path_pattern = os.path.join(RESULTS_DIR, str(job_id), filter_dir, "shard_*.csv")
        files = glob.glob(path_pattern, recursive=True)
        
        if not files:
            print(f"Warning: No data found for identifier {ident}")
            continue

        for filepath in files:
            impl, mode = parse_tool(filepath)
            try:
                df = pd.read_csv(filepath, comment='#')
                for _, row in df.iterrows():
                    benchmark, val = parse_test_name(row['test'])
                    if benchmark:
                        all_data.append({
                            'job_id': ident, # Store the full identifier as unique ID for this 'run'
                            'run_label': label,
                            'impl': impl,
                            'mode': mode,
                            'benchmark': benchmark,
                            'value': val,
                            'time': float(row['time']),
                            'status': int(float(row['status']))
                        })
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
            
    return pd.DataFrame(all_data)

def setup_plot_style():
    plt.rcParams.update({'font.size': 12})
    return {
        'colors': {
            'belief-states': 'blue', 'direct': 'red', 'projection-based': 'red', 
            'belief': 'blue', 'mso': 'green', 'ltl': 'black', 'ltlf': 'purple', 
            'ltlfilt': 'orange', 'ltlf-fo': 'brown'
        },
        'markers': {'christian': 'o', 'lucas': 'x', 'spot': 's'},
        'linestyles': {'christian': '-', 'lucas': '--', 'spot': ':'}
    }

def generate_plots(df, job_identifiers=None):
    # Create job-specific subdirectory
    if not job_identifiers:
        job_folder = "combined"
    elif isinstance(job_identifiers, list):
        # Sanitize name: replace colons and hyphens with underscores
        job_folder = "_".join(job_identifiers).replace(':', '_').replace('-', '_')
    else:
        job_folder = str(job_identifiers).replace(':', '_').replace('-', '_')

    target_dir = os.path.join(OUTPUT_DIR, job_folder)
    os.makedirs(target_dir, exist_ok=True)
    
    style = setup_plot_style()
    
    # Penalize timeouts for plotting
    df.loc[df['status'] == -2, 'time'] = TIMEOUT_PENALTY_MS
    plot_df = df[df['status'].isin([0, 1, -2])].copy()
    
    # Create a compound label for legends if comparing multiple job entries
    multi_job = len(plot_df['job_id'].unique()) > 1
    
    def make_legend_label(row):
        if multi_job:
            # Format: Run Label (Mode)
            return f"{row['run_label']} ({row['mode']})"
        return row['mode']
        
    plot_df['legend_label'] = plot_df.apply(make_legend_label, axis=1)
    
    # Pre-select colors/markers for each legend_label to ensure consistency across plots
    unique_legend_labels = sorted(plot_df['legend_label'].unique())
    import numpy as np
    
    # Use a standard color cycle if multi-job, otherwise use the fixed mode colors
    if multi_job:
        color_list = plt.rcParams['axes.prop_cycle'].by_key()['color']
        label_to_color = {label: color_list[i % len(color_list)] for i, label in enumerate(unique_legend_labels)}
    else:
        label_to_color = {label: style['colors'].get(label, 'gray') for label in unique_legend_labels}

    # Map for styling based on legend_label (using original mode/impl)
    label_to_mode = plot_df.drop_duplicates('legend_label').set_index('legend_label')['mode'].to_dict()
    label_to_impl = plot_df.drop_duplicates('legend_label').set_index('legend_label')['impl'].to_dict()

    # 1. Generate charts for each implementation
    for impl in plot_df['impl'].unique():
        if impl == 'unknown': continue
        filename = os.path.join(target_dir, f"results_{impl}.png")
        fig = plt.figure(figsize=(15, 12))
        
        title_info = "Comparison of Specified Runs" if multi_job else f"Job: {job_identifiers}"
        fig.suptitle(f"Performance: {impl.capitalize()} ({title_info})", fontsize=16, fontweight='bold')
        
        # (a) Moving-Target
        ax1 = fig.add_subplot(221)
        sub_mt = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == 'Moving-Target')]
        if not sub_mt.empty:
            pivot = sub_mt.groupby(['value', 'legend_label'])['time'].mean().unstack()
            for label in pivot.columns:
                ax1.plot(pivot.index, pivot[label], label=label, marker='o', 
                         color=label_to_color[label], alpha=0.8)
            ax1.set_yscale('log'); ax1.set_xlabel("n"); ax1.set_ylabel("Time (ms)")
            ax1.set_title("Moving-Target"); ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

        # (b) Coin-Game
        ax2 = fig.add_subplot(222)
        sub_cg = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == 'Coin-Game')]
        if not sub_cg.empty:
            pivot = sub_cg.groupby(['value', 'legend_label'])['time'].mean().unstack()
            for label in pivot.columns:
                ax2.plot(pivot.index, pivot[label], label=label, marker='o', 
                         color=label_to_color[label], alpha=0.8)
            ax2.set_yscale('log'); ax2.set_xlabel("n"); ax2.set_ylabel("Time (ms)")
            ax2.set_title("Coin-Game"); ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

        # (c) Private-Peek (Spanning bottom row)
        ax3 = fig.add_subplot(212)
        sub_pp = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == 'Private-Peek')].copy()
        if not sub_pp.empty:
            sub_pp['x_label'] = sub_pp['value'].apply(lambda x: f"n={x[0]},m={x[1]}")
            sub_pp['sort_col'] = sub_pp['value'].apply(lambda x: x[0]*100 + x[1])
            pivot = sub_pp.sort_values('sort_col').groupby(['x_label', 'legend_label'], sort=False)['time'].mean().unstack()
            pivot.plot(kind='bar', ax=ax3, logy=True, width=0.8, color=[label_to_color[col] for col in pivot.columns])
            ax3.set_ylabel("Time (ms)")
            ax3.set_title("Private-Peek (log)"); plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')
            ax3.legend(fontsize=8, ncol=2)
            
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.subplots_adjust(hspace=0.5)
        plt.savefig(filename, dpi=300)
        plt.close(fig)
        print(f"Saved: {filename}")

    # 2. Generate Comparison Plot (Direct Comparison layout)
    if len(unique_legend_labels) > 1:
        comp_file = os.path.join(target_dir, "comparison.png")
        fig = plt.figure(figsize=(15, 12))
        fig.suptitle(f"Direct Comparison of Results: {job_folder}", fontsize=18, fontweight='bold')
        
        m_map = {
            'belief-states': 'Belief States', 'projection-based': 'Projection-Based', 
            'mso': 'MSO', 'belief': 'Belief', 'direct': 'Direct', 
            'ltl': 'LTL', 'ltlf': 'LTLf', 'ltlfilt': 'LTLfilt', 'ltlf-fo': 'LTLf-FO'
        }

        # (a) Moving-Target
        ax1 = fig.add_subplot(221)
        sub_mt = plot_df[plot_df['benchmark'] == 'Moving-Target']
        if not sub_mt.empty:
            pivot = sub_mt.groupby(['value', 'legend_label'])['time'].mean().unstack()
            for label in pivot.columns:
                impl = label_to_impl[label]
                mode = label_to_mode[label]
                
                # If multi-job, the label is already descriptive. 
                # Otherwise, we add the impl name for clarity.
                display_label = label if multi_job else f"{impl.capitalize()} {m_map.get(mode, mode)}"
                
                ax1.plot(pivot.index, pivot[label], label=display_label, 
                         marker=style['markers'].get(impl, 'o'), 
                         linestyle=style['linestyles'].get(impl, '-'), 
                         color=label_to_color[label], alpha=0.8)
        ax1.set_yscale('log'); ax1.set_xlabel("n"); ax1.set_ylabel("Time (ms)")
        ax1.legend(fontsize=8, ncol=2); ax1.grid(True, alpha=0.3)
        ax1.set_title("(a) Moving-Target")

        # (b) Coin-Game
        ax2 = fig.add_subplot(222)
        sub_cg = plot_df[plot_df['benchmark'] == 'Coin-Game']
        if not sub_cg.empty:
            pivot = sub_cg.groupby(['value', 'legend_label'])['time'].mean().unstack()
            for label in pivot.columns:
                impl = label_to_impl[label]
                mode = label_to_mode[label]
                display_label = label if multi_job else f"{impl.capitalize()} {m_map.get(mode, mode)}"

                ax2.plot(pivot.index, pivot[label], label=display_label, 
                         marker=style['markers'].get(impl, 'o'), 
                         linestyle=style['linestyles'].get(impl, '-'), 
                         color=label_to_color[label], alpha=0.8)
        ax2.set_yscale('log'); ax2.set_xlabel("n"); ax2.set_ylabel("Time (ms)")
        ax2.legend(fontsize=8, ncol=2); ax2.grid(True, alpha=0.3)
        ax2.set_title("(b) Coin-Game")

        # (c) Private-Peek (Spanning bar chart)
        ax3 = fig.add_subplot(212)
        sub_pp = plot_df[plot_df['benchmark'] == 'Private-Peek'].copy()
        if not sub_pp.empty:
            sub_pp['x_label'] = sub_pp['value'].apply(lambda x: f"n={x[0]},m={x[1]}")
            sub_pp['sort_col'] = sub_pp['value'].apply(lambda x: x[0]*10 + x[1])
            summary = sub_pp.sort_values('sort_col').groupby(['x_label', 'legend_label'], sort=False)['time'].mean().unstack()
            summary.plot(kind='bar', ax=ax3, logy=True, width=0.8, alpha=0.9, color=[label_to_color[col] for col in summary.columns])
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
    parser.add_argument("--job-id", nargs='+', help="Job ID(s) or Identifier(s) to plot. Format for specific filtering: JOB_ID-tool:mode")
    parser.add_argument("--label", nargs='+', help="Custom label(s) for the job entries")
    args = parser.parse_args()

    data = load_data(args.job_id, args.label)
    if not data.empty:
        generate_plots(data, args.job_id)
    else:
        print("No data to plot.")
