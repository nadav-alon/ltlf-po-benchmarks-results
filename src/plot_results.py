import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import re
import argparse

def parse_filename(filepath):
    # expect /.../<impl>_<mode>/shard_<n>.csv
    dir_name = os.path.basename(os.path.dirname(filepath))
    parts = dir_name.split('_', 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    
    # Fallback to old format just in case
    filename = os.path.basename(filepath)
    match = re.search(r'test_([^_]+)_([^_]+)_shard', filename)
    if match:
        return match.group(1), match.group(2)
    return None, None

def parse_test_name(test_path):
    # /.../ltlf/seek_10.ltlf
    # /.../ltlf/coins_10.ltlf
    # /.../ltlf/peek/peek_1_1_16.ltlf
    
    if 'seek_' in test_path:
        match = re.search(r'seek_(\d+)', test_path)
        if match:
            return 'Moving-Target', int(match.group(1))
    elif 'coins_' in test_path:
        match = re.search(r'coins_(\d+)', test_path)
        if match:
            return 'Coin-Game', int(match.group(1))
    elif 'peek_' in test_path:
        match = re.search(r'peek_(\d+)_(\d+)', test_path)
        if match:
            return 'Private-Peek', (int(match.group(1)), int(match.group(2)))
    return None, None

def load_data(results_dir, job_id=None):
    all_data = []
    if job_id:
        path_pattern = os.path.join(results_dir, job_id, "**", "shard_*.csv")
    else:
        path_pattern = os.path.join(results_dir, "**", "shard_*.csv")
    
    shard_files = glob.glob(path_pattern, recursive=True)
    
    for filepath in shard_files:
        impl, mode = parse_filename(filepath)
        if not impl:
            continue
            
        try:
            df = pd.read_csv(filepath)
            for _, row in df.iterrows():
                benchmark, value = parse_test_name(row['test'])
                if benchmark:
                    all_data.append({
                        'implementation': impl,
                        'benchmark': benchmark,
                        'value': value,
                        'mode': mode,
                        'time': float(row['time']),
                        'status': int(row['status'])
                    })
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            
    return pd.DataFrame(all_data)

def generate_implementation_graph(df, implementation, filename):
    # Filter for specific implementation
    impl_df = df[df['implementation'] == implementation].copy()
    
    if impl_df.empty:
        print(f"No data found for {implementation}")
        return

    # Penalty for timeouts (status -2)
    # Most timeouts in the data are ~180s. Setting a penalty of 300s (300,000ms)
    TIMEOUT_PENALTY_MS = 300000
    impl_df.loc[impl_df['status'] == -2, 'time'] = TIMEOUT_PENALTY_MS
    
    # Filter for successful runs OR timeouts
    # We exclude errors (status -1) as they are often infrastructure/syntax issues
    plot_df = impl_df[impl_df['status'].isin([0, 1, -2])]

    if implementation == 'lucas':
        mode_map = {
            'belief-states': 'Belief States',
            'projection-based': 'Projection-Based',
            'mso': 'MSO',
            'belief': 'Projection-Based',
            'direct': 'Belief States'
        }
    elif implementation == 'christian':
        mode_map = {
            'belief': 'Belief',
            'direct': 'Direct',
            'mso': 'MSO'
        }
    elif implementation == 'spot':
        mode_map = {
            'ltl': 'LTL',
            'ltlf': 'LTLf',
            'ltlfilt': 'LTLfilt'
        }
    else:
        mode_map = {}
    
    colors = {
        'belief-states': 'blue', 'direct': 'blue',
        'projection-based': 'red', 'belief': 'red',
        'mso': 'green', 'ltl': 'black', 'ltlf': 'purple', 'ltlfilt': 'orange'
    }
    markers = {
        'belief-states': 'o', 'direct': 'o',
        'projection-based': 'x', 'belief': 'x',
        'mso': '^', 'ltl': 's', 'ltlf': 'd', 'ltlfilt': '*'
    }
    mode_order = ['belief-states', 'direct', 'projection-based', 'belief', 'mso', 'ltl', 'ltlf', 'ltlfilt']

    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(12, 10))
    fig.suptitle(f"Performance: {implementation.capitalize()} Implementation (Timeouts included as {TIMEOUT_PENALTY_MS/1000}s)", fontsize=16, fontweight='bold')
    
    # (a) Moving-Target
    ax1 = fig.add_subplot(221)
    b_df = plot_df[plot_df['benchmark'] == 'Moving-Target']
    if not b_df.empty:
        pivot_df = b_df.groupby(['value', 'mode'])['time'].mean().unstack()
        cols = [m for m in mode_order if m in pivot_df.columns]
        
        for mode in cols:
            ax1.plot(pivot_df.index, pivot_df[mode], label=mode_map.get(mode, mode), marker=markers.get(mode, 'o'), color=colors.get(mode, 'gray'))
        ax1.set_yscale('log')
        ax1.set_xlabel("Number of positions (n)")
        ax1.set_ylabel("Strategy computation time (ms)")
        ax1.legend()
        ax1.grid(True, which="both", ls="-", alpha=0.3)
    ax1.text(0.5, -0.2, "(a) Moving-Target", transform=ax1.transAxes, ha='center', fontweight='bold', style='italic')

    # (b) Coin-Game
    ax2 = fig.add_subplot(222)
    b_df = plot_df[plot_df['benchmark'] == 'Coin-Game']
    if not b_df.empty:
        pivot_df = b_df.groupby(['value', 'mode'])['time'].mean().unstack()
        cols = [m for m in mode_order if m in pivot_df.columns]
        for mode in cols:
            ax2.plot(pivot_df.index, pivot_df[mode], label=mode_map.get(mode, mode), marker=markers.get(mode, 'o'), color=colors.get(mode, 'gray'))
        ax2.set_yscale('log')
        ax2.set_xlabel("Number of coins (n)")
        ax2.set_ylabel("Strategy computation time (ms)")
        ax2.legend()
        ax2.grid(True, which="both", ls="-", alpha=0.3)
    ax2.text(0.5, -0.2, "(b) Coin-Game", transform=ax2.transAxes, ha='center', fontweight='bold', style='italic')

    # (c) Private-Peek
    ax3 = fig.add_subplot(212)
    b_df = plot_df[plot_df['benchmark'] == 'Private-Peek'].copy()
    if not b_df.empty:
        b_df['label'] = b_df['value'].apply(lambda x: f"n={x[0]},m={x[1]}")
        b_df['sort_key'] = b_df['value'].apply(lambda x: x[0]*10 + x[1])
        b_df = b_df.sort_values('sort_key')
        
        pivot_df = b_df.groupby(['label', 'mode'], sort=False)['time'].mean().unstack()
        # Order for bar chart
        mode_order = ['mso', 'belief-states', 'direct', 'projection-based', 'belief', 'ltl', 'ltlf', 'ltlfilt']
        cols = [m for m in mode_order if m in pivot_df.columns]
        pivot_df = pivot_df[cols]
        
        # Define bar colors
        bar_colors = [colors.get(c, 'gray') for c in cols]
        pivot_df.plot(kind='bar', ax=ax3, logy=True, color=bar_colors, width=0.8)
        ax3.set_xlabel("Configurations (n, m)")
        ax3.set_ylabel("Strategy computation time (ms)")
        ax3.legend([mode_map[c] for c in cols], loc='upper left')
        plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')
    ax3.text(0.5, -0.4, "(c) Private-Peek", transform=ax3.transAxes, ha='center', fontweight='bold', style='italic')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.subplots_adjust(hspace=0.5)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Graph saved as {filename}")

def generate_comparison_graph(df, filename):
    # Filter for both implementations and include timeouts
    TIMEOUT_PENALTY_MS = 300000
    df = df.copy()
    df.loc[df['status'] == -2, 'time'] = TIMEOUT_PENALTY_MS
    plot_df = df[df['status'].isin([0, 1, -2])]

    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(15, 12))
    fig.suptitle("Direct Comparison: Christian (Solid), Lucas (Dashed), Spot (Dotted)", fontsize=18, fontweight='bold')

    lucas_map = {
        'belief-states': 'Belief States',
        'projection-based': 'Projection-Based',
        'mso': 'MSO',
        'belief': 'Projection-Based',
        'direct': 'Belief States'
    }
    christian_map = {
        'belief': 'Belief',
        'direct': 'Direct',
        'mso': 'MSO'
    }
    spot_map = {
        'ltl': 'LTL',
        'ltlf': 'LTLf',
        'ltlfilt': 'LTLfilt'
    }
    
    # Define styles
    colors = {
        'belief-states': 'blue', 'direct': 'red',
        'projection-based': 'red', 'belief': 'blue',
        'mso': 'green', 'ltl': 'black', 'ltlf': 'purple', 'ltlfilt': 'orange'
    }
    markers = {'christian': 'o', 'lucas': 'x', 'spot': 's'}
    linestyles = {'christian': '-', 'lucas': '--', 'spot': ':'}

    # (a) Moving-Target
    ax1 = fig.add_subplot(221)
    for impl in df['implementation'].unique():
        b_df = plot_df[(plot_df['benchmark'] == 'Moving-Target') & (plot_df['implementation'] == impl)]
        if not b_df.empty:
            pivot_df = b_df.groupby(['value', 'mode'])['time'].mean().unstack()
            if impl == 'lucas': m_map = lucas_map
            elif impl == 'christian': m_map = christian_map
            elif impl == 'spot': m_map = spot_map
            else: m_map = {}
            
            for mode in pivot_df.columns:
                label = f"{impl.capitalize()} {m_map.get(mode, mode)}"
                ax1.plot(pivot_df.index, pivot_df[mode], label=label, 
                         marker=markers.get(impl, 'o'), linestyle=linestyles.get(impl, '-'), color=colors.get(mode, 'gray'), alpha=0.8)
    
    ax1.set_yscale('log')
    ax1.set_xlabel("Number of positions (n)")
    ax1.set_ylabel("Strategy computation time (ms)")
    ax1.legend(fontsize=8, ncol=2)
    ax1.grid(True, which="both", ls="-", alpha=0.3)
    ax1.text(0.5, -0.2, "(a) Moving-Target", transform=ax1.transAxes, ha='center', fontweight='bold', style='italic')

    # (b) Coin-Game
    ax2 = fig.add_subplot(222)
    for impl in df['implementation'].unique():
        b_df = plot_df[(plot_df['benchmark'] == 'Coin-Game') & (plot_df['implementation'] == impl)]
        if not b_df.empty:
            pivot_df = b_df.groupby(['value', 'mode'])['time'].mean().unstack()
            if impl == 'lucas': m_map = lucas_map
            elif impl == 'christian': m_map = christian_map
            elif impl == 'spot': m_map = spot_map
            else: m_map = {}
            
            for mode in pivot_df.columns:
                label = f"{impl.capitalize()} {m_map.get(mode, mode)}"
                ax2.plot(pivot_df.index, pivot_df[mode], label=label, 
                         marker=markers.get(impl, 'o'), linestyle=linestyles.get(impl, '-'), color=colors.get(mode, 'gray'), alpha=0.8)
    
    ax2.set_yscale('log')
    ax2.set_xlabel("Number of coins (n)")
    ax2.set_ylabel("Strategy computation time (ms)")
    ax2.legend(fontsize=8, ncol=2)
    ax2.grid(True, which="both", ls="-", alpha=0.3)
    ax2.text(0.5, -0.2, "(b) Coin-Game", transform=ax2.transAxes, ha='center', fontweight='bold', style='italic')

    # (c) Private-Peek
    ax3 = fig.add_subplot(212)
    # For private peek, we use a grouped bar chart
    b_df = plot_df[plot_df['benchmark'] == 'Private-Peek'].copy()
    b_df['label'] = b_df['value'].apply(lambda x: f"n={x[0]},m={x[1]}")
    b_df['sort_key'] = b_df['value'].apply(lambda x: x[0]*10 + x[1])
    b_df = b_df.sort_values('sort_key')
    
    # Group by label, implementation, and mode
    summary = b_df.groupby(['label', 'implementation', 'mode'], sort=False)['time'].mean().unstack(level=[1, 2])
    
    # This creates a lot of columns. Let's simplify and just show MSO and Belief for both
    # to keep it readable, OR use small groups.
    # Actually, let's just plot it and see.
    summary.plot(kind='bar', ax=ax3, logy=True, width=0.8, alpha=0.9)
    
    ax3.set_xlabel("Configurations (n, m)")
    ax3.set_ylabel("Strategy computation time (ms)")
    ax3.legend(fontsize=7, ncol=3, loc='upper left')
    plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')
    ax3.text(0.5, -0.4, "(c) Private-Peek (All methods/implementations)", transform=ax3.transAxes, ha='center', fontweight='bold', style='italic')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.subplots_adjust(hspace=0.6)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Graph saved as {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot benchmark results.")
    parser.add_argument("--job-id", help="Specific job ID folder to plot (results/<job_id>)")
    parser.add_argument("--results-dir", default="/home/cowclaw/results_shards/data/results", help="Directory containing results")
    args = parser.parse_args()

    data = load_data(args.results_dir, job_id=args.job_id)
    if not data.empty:
        BASE_DIR = "/home/cowclaw/results_shards"
        suffix = f"_{args.job_id}" if args.job_id else ""
        
        output_dir = os.path.join(BASE_DIR, "reports/figures")
        os.makedirs(output_dir, exist_ok=True)
        
        generate_implementation_graph(data, 'christian', os.path.join(output_dir, f'results_graph_christian{suffix}.png'))
        generate_implementation_graph(data, 'lucas', os.path.join(output_dir, f'results_graph_lucas{suffix}.png'))
        generate_implementation_graph(data, 'spot', os.path.join(output_dir, f'results_graph_spot{suffix}.png'))
        generate_comparison_graph(data, os.path.join(output_dir, f'results_comparison{suffix}.png'))
    else:
        if args.job_id:
            print(f"No data found for job {args.job_id} in {args.results_dir}/{args.job_id}")
        else:
            print("No data found.")
