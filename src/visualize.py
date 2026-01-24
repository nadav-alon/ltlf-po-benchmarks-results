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
    elif 'amba' in test_path.lower(): return 'AMBA', 0
    elif 'ltl2dba' in test_path.lower(): return 'LTL2DBA', 0
    elif 'workstation_resupply' in test_path.lower(): return 'Workstation-Resupply', 0
    elif 'simple_arbiter' in test_path.lower(): return 'Simple-Arbiter', 0
    elif 'lilydemo' in test_path.lower(): return 'Lily', 0
    elif 'arbiter' in test_path.lower(): return 'Arbiter-Zoo', 0
    elif 'generalized_buffer' in test_path.lower(): return 'Gen-Buffer', 0
    elif 'load_balancer' in test_path.lower(): return 'Load-Balancer', 0
    elif 'lift' in test_path.lower(): return 'Lift', 0
    elif 'robot_grid' in test_path.lower(): return 'Robot-Grid', 0
    elif 'tsl_smart_home' in test_path.lower() or any(x in test_path for x in ['Alarm', 'Morning', 'Demo1', 'Check']): return 'TSL-Home', 0
    elif 'collector' in test_path.lower(): return 'Collector', 0
    elif 'mux' in test_path.lower(): return 'Mux', 0
    
    # Default to filename
    return 'Other', os.path.basename(test_path).replace('.ltlf', '')

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
                            'test_path': row['test'],
                            'test_name': os.path.basename(row['test']).replace('.ltlf', ''),
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
        
        benchmarks = sorted(plot_df[plot_df['impl'] == impl]['benchmark'].unique())
        if not benchmarks: continue
        
        num_plots = len(benchmarks)
        cols = 2
        rows = (num_plots + 1) // 2
        
        fig = plt.figure(figsize=(15, 6 * rows))
        
        title_info = "Comparison" if multi_job else f"Job: {job_identifiers}"
        fig.suptitle(f"Performance: {impl.capitalize()} ({title_info})", fontsize=16, fontweight='bold')
        
        for i, b_name in enumerate(benchmarks):
            ax = fig.add_subplot(rows, cols, i + 1)
            sub = plot_df[(plot_df['impl'] == impl) & (plot_df['benchmark'] == b_name)]
            
            if b_name == 'Private-Peek':
                # Special handling for tuple values
                sub = sub.copy()
                sub = sub[sub['value'].apply(lambda x: isinstance(x, (list, tuple)) and len(x) == 2)]
                if sub.empty: continue
                sub['x_label'] = sub['value'].apply(lambda x: f"n={x[0]},m={x[1]}")
                sub['sort_col'] = sub['value'].apply(lambda x: x[0]*100 + x[1])
                pivot = sub.sort_values('sort_col').groupby(['x_label', 'legend_label'], sort=False)['time'].mean().unstack()
                pivot.plot(kind='bar', ax=ax, logy=True, width=0.8, color=[label_to_color.get(col, 'gray') for col in pivot.columns])
                plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
            elif sub['value'].apply(lambda x: isinstance(x, (int, float))).all():
                pivot = sub.groupby(['value', 'legend_label'])['time'].mean().unstack()
                for label in pivot.columns:
                    ax.plot(pivot.index, pivot[label], label=label, marker='o', 
                             color=label_to_color.get(label, 'gray'), alpha=0.8)
                ax.set_yscale('log')
                ax.set_xlabel("Scale/Parameter")
            else:
                pivot = sub.groupby(['value', 'legend_label'])['time'].mean().unstack()
                pivot.plot(kind='bar', ax=ax, logy=True, width=0.8, color=[label_to_color.get(col, 'gray') for col in pivot.columns])
                plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

            ax.set_ylabel("Time (ms)")
            ax.set_title(b_name)
            ax.legend(fontsize=8)
            ax.grid(True, alpha=0.3)
            
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.subplots_adjust(hspace=0.4)
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

def generate_scatter_plot(df, target_dir, job_identifiers):
    """Generate multiple scatter plots (All, Realizable, Unrealizable)."""
    unique_ids = df['job_id'].unique()
    if len(unique_ids) != 2:
        print(f"Scatter plot requires exactly 2 jobs to compare, found {len(unique_ids)}")
        return

    # Use first job as the baseline for filtering
    id1 = unique_ids[0]
    
    # 1. All benchmarks
    _do_scatter(df, target_dir, "scatter_fo_vs_po_all.png")
    
    # 2. Benchmarks that were Realizable in the first job
    realizable_tests = df[(df['job_id'] == id1) & (df['status'] == 1)]['test_name'].unique()
    if len(realizable_tests) > 0:
        sub_real = df[df['test_name'].isin(realizable_tests)]
        _do_scatter(sub_real, target_dir, "scatter_fo_vs_po_realizable.png", title_suffix="(Realizable at Baseline)")
        
    # 3. Benchmarks that were Unrealizable in the first job
    unrealizable_tests = df[(df['job_id'] == id1) & (df['status'] == 0)]['test_name'].unique()
    if len(unrealizable_tests) > 0:
        sub_unreal = df[df['test_name'].isin(unrealizable_tests)]
        _do_scatter(sub_unreal, target_dir, "scatter_fo_vs_po_unrealizable.png", title_suffix="(Unrealizable at Baseline)")

def _do_scatter(df, target_dir, filename, title_suffix=""):
    """Internal helper to render a single scatter plot."""
    unique_ids = df['job_id'].unique()
    # If filtered to empty, skip
    if df.empty: return

    comp_file = os.path.join(target_dir, filename)
    pivot = df.pivot_table(index=['benchmark', 'test_name'], columns='job_id', values='time', aggfunc='mean')
    
    id1, id2 = unique_ids[0], unique_ids[1]
    label1 = df[df['job_id'] == id1]['run_label'].iloc[0]
    label2 = df[df['job_id'] == id2]['run_label'].iloc[0]
    
    plt.figure(figsize=(10, 10))
    plt.suptitle(f"Performance Comparison {title_suffix}: {label1} vs {label2}", fontsize=16, fontweight='bold')
    
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    benchmarks = sorted(df['benchmark'].unique())
    b_to_color = {b: colors[i % len(colors)] for i, b in enumerate(benchmarks)}
    
    for b in benchmarks:
        if b not in pivot.index.get_level_values(0): continue
        sub = pivot.loc[b]
        plt.scatter(sub[id1], sub[id2], label=b, color=b_to_color[b], alpha=0.7, s=80, edgecolors='k')

    all_times_raw = df['time']
    has_timeouts = (df['status'] == -2).any()
    real_times = all_times_raw[df['status'] != -2]
    
    if real_times.empty:
        min_val, max_val = 1, TIMEOUT_PENALTY_MS
    else:
        min_val = max(min(real_times.min() / 2, 1), 0.01)
        max_val = TIMEOUT_PENALTY_MS * 1.5 if has_timeouts else real_times.max() * 2
    
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', alpha=0.5, label='Equal Performance')
    plt.xscale('log'); plt.yscale('log')
    plt.xlim(min_val, max_val); plt.ylim(min_val, max_val)
    plt.xlabel(f"{label1} Time (ms)"); plt.ylabel(f"{label2} Time (ms)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    
    plt.text(max_val * 0.1, max_val * 0.01, f"{label2} Faster", color='green', fontweight='bold', alpha=0.3, fontsize=15, rotation=45)
    plt.text(max_val * 0.01, max_val * 0.1, f"{label1} Faster", color='red', fontweight='bold', alpha=0.3, fontsize=15, rotation=45)

    plt.tight_layout()
    plt.savefig(comp_file, dpi=300)
    plt.close()
    print(f"Saved: {comp_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolidated Visualization Tool")
    parser.add_argument("--job-id", nargs='+', help="Job ID(s) or Identifier(s) to plot. Format for specific filtering: JOB_ID-tool:mode")
    parser.add_argument("--label", nargs='+', help="Custom label(s) for the job entries")
    parser.add_argument("--scatter", action="store_true", help="Generate FO vs PO scatter plot comparison")
    args = parser.parse_args()

    data = load_data(args.job_id, args.label)
    if not data.empty:
        generate_plots(data, args.job_id)
        if args.scatter:
            # For scatter plot, we might need a specific output dir
            job_folder = "_".join(args.job_id).replace(':', '_').replace('-', '_')
            target_dir = os.path.join(OUTPUT_DIR, job_folder)
            generate_scatter_plot(data, target_dir, args.job_id)
    else:
        print("No data to plot.")
