# Results & Analysis Benchmarks

This repository contains the raw results, logs, and analysis scripts for the LTLf Reactive Synthesis benchmarks.

## Directory Structure

- `src/`: Python scripts for data processing and visualization.
- `data/`:
    - `results/`: Sharded CSV files organized by SLURM Job ID.
    - `logs/`: SLURM output/error logs.
    - `snapshots/`: Snapshot CSV files for specific tool versions.
- `reports/`:
    - `figures/`: Generated performance graphs (.png).
    - `text/`: Error lists, inconsistency reports, and quantitative summaries.
    - `analysis_runs/`: Deep-dive analysis for specific high-interest jobs.
- `archive/`: Deprecated or backup files.

## Common Operations

### 1. Basic Analysis (Consistency & Success Rates)
To see a summary of performance and check if tools agree on realizability for a specific job:
```bash
python src/analyze_shards.py --job-id <JOB_ID>
```

### 2. Generate Plots
To generate performance comparison graphs (saved to `reports/figures/`):
```bash
python src/plot_results.py --job-id <JOB_ID>
```

### 3. Collect Errors
To extract a list of all failing tests (Status -1):
```bash
python src/extract_errors.py
```

### 4. Compare Results
To compare one job against a "Source of Truth" (configurable inside the script):
```bash
python src/compare_results.py
```

## Note on Status Codes
- `1`: Realizable
- `0`: Unrealizable
- `-1`: Error (Infrastructure, Parser, etc.)
- `-2`: Timeout
