# Benchmark Dataset Summary

This snapshot provides a human-readable guide to the benchmark results and logs stored in this repository.

## Key Datasets (Tags)

| Tag | Jobs Included | Description |
| :-- | :--- | :--- |
| **`baseline_moore`** | 3104998 | Base results for Moore semantics (all tools). |
| **`baseline_mealy`** | 3105085 | Base results for Mealy semantics (all tools). |
| **`po_*_unobs`** | Multiple | Variations of partial observability (0% to 100% unobservable variables). |
| **`ltlf_fin_*_unobs`** | Multiple | PO study specifically for the `ltlf-fin` benchmark set. |

## Quick Navigation

Navigate to the following directories to find logically grouped results:

- **Results:** [data/results/tags/](file:///home/cowclaw/results_shards/data/results/tags/)
- **Logs:** [data/logs/tags/](file:///home/cowclaw/results_shards/data/logs/tags/)

## How to use Tags

The tagging system maps these descriptive names to numeric Job IDs via symlinks. You can use these tags with the visualization scripts:

```bash
python3 src/visualize.py --job-id tags/po_0_unobs tags/po_50_unobs tags/po_100_unobs --scatter
```

## Management

- **Configuration:** [data/tags.json](file:///home/cowclaw/results_shards/data/tags.json)
- **Update Script:** [src/update_tags.py](file:///home/cowclaw/results_shards/src/update_tags.py)
- **Job Descriptions:** [data/job_labels.json](file:///home/cowclaw/results_shards/data/job_labels.json)
