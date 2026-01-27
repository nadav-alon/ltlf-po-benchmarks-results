# Observability Analysis: FO vs PO (Orig) vs FU
Comparing Full Observability (FO), Original Partial Observability (PO), and Full Unobservability (FU).
- **FO (3116131)**: All inputs observable (`po-part-0`)
- **PO (3104998)**: Original benchmarks (`part`) - *Source of Truth*
- **FU (3116117)**: All inputs unobservable (`po-part-all`)

## Tool: lucas_belief-states
| Mode | Total | Realizable | Unrealizable | Timeouts | Errors | Avg Time (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FO | 1617 | 704 | 112 | 799 | 2 | 13445.54 |
| PO (Orig) | 1617 | 721 | 119 | 775 | 2 | 5121.36 |
| FU | 1617 | 1012 | 428 | 175 | 2 | 15321.09 |

### Realizability Transitions
- **FO (Real) -> PO (Unreal)**: 1 benchmarks
- **PO (Real) -> FU (Unreal)**: 1 benchmarks
- **FO (Real) -> FU (Unreal)**: 2 benchmarks

### Runtime: FO vs PO (Orig)
- Count (Realizable in both): 703
- Median Slowdown (FO -> PO): 0.94x

### Runtime: PO (Orig) vs FU
- Count (Realizable in both): 720
- Median Slowdown (PO -> FU): 0.83x

### Performance Comparison Graph
| FO vs PO (Orig) | PO (Orig) vs FU |
| :---: | :---: |
| ![lucas_belief-states FO vs PO](figures/3116131_lucas_belief_states_3104998_lucas_belief_states/scatter_fo_vs_po_all.png) | ![lucas_belief-states PO vs FU](figures/3104998_lucas_belief_states_3116117_lucas_belief_states/scatter_fo_vs_po_all.png) |

---

## Tool: lucas_mso
| Mode | Total | Realizable | Unrealizable | Timeouts | Errors | Avg Time (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FO | 1617 | 1181 | 434 | 2 | 0 | 226.74 |
| PO (Orig) | 1617 | 1176 | 435 | 6 | 0 | 463.19 |
| FU | 1617 | 1023 | 338 | 256 | 0 | 10.52 |

### Realizability Transitions
- **FO (Real) -> PO (Unreal)**: 1 benchmarks
- **PO (Real) -> FU (Unreal)**: 3 benchmarks
- **FO (Real) -> FU (Unreal)**: 4 benchmarks

### Runtime: FO vs PO (Orig)
- Count (Realizable in both): 1176
- Median Slowdown (FO -> PO): 0.86x

### Runtime: PO (Orig) vs FU
- Count (Realizable in both): 1023
- Median Slowdown (PO -> FU): 0.43x

### Performance Comparison Graph
| FO vs PO (Orig) | PO (Orig) vs FU |
| :---: | :---: |
| ![lucas_mso FO vs PO](figures/3116131_lucas_mso_3104998_lucas_mso/scatter_fo_vs_po_all.png) | ![lucas_mso PO vs FU](figures/3104998_lucas_mso_3116117_lucas_mso/scatter_fo_vs_po_all.png) |

---

## Tool: spot_ltlf
| Mode | Total | Realizable | Unrealizable | Timeouts | Errors | Avg Time (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FO | 1617 | 1183 | 434 | 0 | 0 | 36.24 |
| PO (Orig) | 1617 | 1180 | 435 | 2 | 0 | 20.05 |
| FU | 1617 | 1172 | 440 | 5 | 0 | 7.69 |

### Realizability Transitions
- **FO (Real) -> PO (Unreal)**: 1 benchmarks
- **PO (Real) -> FU (Unreal)**: 5 benchmarks
- **FO (Real) -> FU (Unreal)**: 6 benchmarks

### Runtime: FO vs PO (Orig)
- Count (Realizable in both): 1180
- Median Slowdown (FO -> PO): 1.00x

### Runtime: PO (Orig) vs FU
- Count (Realizable in both): 1172
- Median Slowdown (PO -> FU): 1.00x

### Performance Comparison Graph
| FO vs PO (Orig) | PO (Orig) vs FU |
| :---: | :---: |
| ![spot_ltlf FO vs PO](figures/3116131_spot_ltlf_3104998_spot_ltlf/scatter_fo_vs_po_all.png) | ![spot_ltlf PO vs FU](figures/3104998_spot_ltlf_3116117_spot_ltlf/scatter_fo_vs_po_all.png) |

---