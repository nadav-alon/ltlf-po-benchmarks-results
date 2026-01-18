import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('/home/cowclaw/results_shards/analysis_3097478/consolidated_results.csv')

# Tools to EXCLUDE from the "Best Other" aggregate:
# 1. spot_ltlf (Comparing against this)
# 2. spot_ltlfilt (Invalid results due to high timeouts/incorrectness)
# 3. spot_ltl (Requested to disregard)
excluded_tools = ['spot_ltlf', 'spot_ltlfilt', 'spot_ltl']


# Filter for valid solves only (Status 0 or 1)
df = df[df['status'].isin([0, 1])]

# separate spot_ltlf
spot_df = df[df['tool'] == 'spot_ltlf'].set_index('test')['time']

# Get "Best Other" time
# We group by test and take the MIN time across all non-excluded tools
others_df = df[~df['tool'].isin(excluded_tools)]
best_others = others_df.groupby('test')['time'].min()

# Align the series (inner join on test/index)
# We only compare instances solved by Spot AND at least one valid other tool
aligned = pd.concat([spot_df, best_others], axis=1, join='inner')
aligned.columns = ['spot_ltlf', 'best_other']

# Calculate speedup (Best Other / Spot)
# If Spot is faster than the BEST other tool, ratio > 1.
aligned['speedup'] = aligned['best_other'] / aligned['spot_ltlf']

print(f"Comparison on {len(aligned)} mutually solved instances.")
print(f"(Comparing against aggregate best of: {', '.join(others_df['tool'].unique())})\n")

print("--- Aggregate Runtime (seconds) ---")
print(f"Total Time Spot:       {aligned['spot_ltlf'].sum():.2f} s")
print(f"Total Time Best Other: {aligned['best_other'].sum():.2f} s")
print(f"Factor: Spot is {aligned['best_other'].sum() / aligned['spot_ltlf'].sum():.2f}x faster than the VIRTUAL BEST other tool.\n")

print("--- Average/Median Runtime per Instance ---")
print(f"Spot       | Mean: {aligned['spot_ltlf'].mean():.4f}s, Median: {aligned['spot_ltlf'].median():.4f}s")
print(f"Best Other | Mean: {aligned['best_other'].mean():.4f}s, Median: {aligned['best_other'].median():.4f}s\n")

print("--- Speedup Stats (Best Other Time / Spot Time) ---")
print(f"Ratio > 1 means Spot is faster than the BEST alternative.")
print(f"Mean Speedup:   {aligned['speedup'].mean():.2f}x")
print(f"Median Speedup: {aligned['speedup'].median():.2f}x")
print(f"Max Speedup:    {aligned['speedup'].max():.2f}x")
print(f"Min Speedup:    {aligned['speedup'].min():.2f}x")
print(f"Spot Faster:    {(aligned['speedup'] > 1).sum()} instances ({(aligned['speedup'] > 1).mean()*100:.1f}%)")
print(f"Other Faster:   {(aligned['speedup'] < 1).sum()} instances ({(aligned['speedup'] < 1).mean()*100:.1f}%)\n")

# Binning logic for distribution
bins = [0, 0.5, 0.9, 1.1, 2, 10, 100, 1000, float('inf')]
labels = ['Other >2x Faster', 'Other 1.1x-2x Faster', 'Comparable (within 10%)', 'Spot 1.1x-2x Faster', 'Spot 2x-10x Faster', 'Spot 10x-100x Faster', 'Spot 100x-1000x Faster', 'Spot >1000x Faster']
binned = pd.cut(aligned['speedup'], bins=bins, labels=labels)

print("--- Distribution of Performance vs Virtual Best ---")
counts = binned.value_counts().sort_index()
for label, count in counts.items():
    print(f"{label:<30} | {count}")
