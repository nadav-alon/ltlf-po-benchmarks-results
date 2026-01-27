# Analysis Report: TLSF-FIN Benchmarks

This report summarizes the performance and realizability impact of partial observability on the `ltlf-fin` benchmark set.

## 1. Overview
The analysis covers **99 benchmarks** with three levels of observability:
*   **FO (Full Observability)**: Job ID `3116651`
*   **PO 50% (50% unobservables)**: Job ID `3116652`
*   **PO 100% (All unobservable)**: Job ID `3116666`

## 2. Realizability Impact
In this benchmark set, **no changes in realizability** were detected across all three levels. All benchmarks that were realizable in the fully observable case remained realizable even with 100% of the input variables being unobservable.

| Transition | Count of benchmarks becoming Unrealizable |
| :--- | :--- |
| FO -> PO 50% | 0 |
| PO 50% -> PO 100% | 0 |
| FO -> PO 100% | 0 |

## 3. Runtime Analysis

The following table shows the mean runtimes for the synthesis step (Spot) and the automaton generation step (Mona).

### Step-wise Mean Runtimes (seconds)
| Level | Spot Synthesis (Mean) | Spot Synthesis (Median) | Mona Generation (Mean) |
| :--- | :---: | :---: | :---: |
| **FO** | 12.15s | 0.002s | 0.0021s |
| **PO 50%** | 12.50s | 0.002s | 0.0020s |
| **PO 100%** | 11.40s | 0.002s | 0.0020s |

### Runtime Factor Comparison (vs FO)
After correcting for a unit bug in the source results (some entries were in milliseconds while timeouts were in seconds), we found that **Partial Observability has a negligible impact on synthesis performance** for this benchmark set.

*   **PO 50% vs FO**: **1.00x** mean factor.
*   **PO 100% vs FO**: **0.94x** mean factor.

The synthesis time is consistently around **12 seconds** on average across all levels. This confirms the visual observation that the vast majority of benchmarks lie on the identity line in the scatter plots.

---

## 4. Visualizations

### FO vs PO 50% Comparison
![FO vs PO 50% Scatter](figures/3116651_3116652/scatter_fo_vs_po_all.png)

### FO vs PO 100% Comparison
![FO vs PO 100% Scatter](figures/3116651_3116666/scatter_fo_vs_po_all.png)

### Synthesis Time Distribution
![Comparison Plot](figures/3116651_3116652_3116666/results_spot.png)
