# LTLf Benchmark Analysis Suite

This directory contains the tools for processing and visualizing reactive synthesis benchmark results.

## Folder Structure

- `src/`: Core analysis scripts (**the primary tools listed below**).
- `data/`:
    - `results/`: Sharded CSV output from SLURM jobs (organized by Job ID).
    - `logs/`: SLURM output/error logs.
- `reports/`:
    - `figures/`: Generated performance plots (.png).
    - `text/`: Comprehensive error lists and consistency reports.
- `archive/`: Old scripts and deprecated results.

---

## 🛠 The "Power Tools" (in `src/`)

### 1. `python3 src/analyze.py`
**Purpose:** High-level summary of success rates and semantic consistency.
- **Usage:** `python3 src/analyze.py --job-id <ID>`
- **Output:** Performance table (Total, Success, Timeout, Error, Avg Time) and a conflict warning if tools disagree on realizability.
- **Detail:** Use `--output-inconsistent <file>` to save a list of tests where tools disagreed.

### 2. `python3 src/report_errors.py`
**Purpose:** Deep dive into why tests failed.
- **Usage:** `python3 src/report_errors.py --job-id <ID> --list`
- **Output:** Summary of errors/timeouts per tool.
- **Options:** 
    - `--list`: Prints the full path of every file that hit an "Error" (Status -1).
    - `--csv <file>`: Exports every failure to a flat CSV for further filtering.

### 3. `python3 src/visualize.py`
**Purpose:** Generate all performance graphs.
- **Usage:** `python3 src/visualize.py --job-id <ID>`
- **Output:** Saves multiple `.png` files to `reports/figures/`, including individual tool scaling and cross-tool comparisons.

### 4. `python3 src/cross_check.py`
**Purpose:** Compare two different specific runs (e.g., comparing a new version of Lucas against a stable Spot run).
- **Usage:** `python3 src/cross_check.py --job-a <ID1> --tool-a <NAME1> --job-b <ID2> --tool-b <NAME2>`
- **Output:** Lists only the specific tests where the two tools disagreed on realizability.

---

## Tool Naming Mapping (for `analyze.py`)
- `l_bst`: Lucas Belief States
- `l_prj`: Lucas Projection-Based
- `l_mso`: Lucas MSO
- `c_bel`: Christian Belief
- `c_dir`: Christian Direct
- `s_ltl`: Spot LTL
- `s_ltl`: Spot LTLf

---

## ⚡️ Zsh Autocomplete (Job IDs)

To enable tab-completion for `--job-id` (so it automatically suggests Job IDs found in `data/results/`), add the following to your `.zshrc`:

```zsh
source /home/cowclaw/results_shards/src/completion.zsh
```

Now you can type `src/analyze.py --job-id [TAB]` and see your results folders!
