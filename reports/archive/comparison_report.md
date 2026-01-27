# Synthesis Tool Performance Report

This report compares multiple synthesis tools across Moore and Mealy semantics using the latest benchmark runs.

## Moore Semantics Comparison (Job 3104998)
*Reference: Job 3091259 (lucas_mso)*

| Tool | Success | Timeouts | Errors | Error % | Avg Time (ms) | Correctness |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| c_bel | 1219 | 396 | 2 | 0.1% | 5459.61 | ❌ 2 conflicts |
| c_dir | 430 | 1182 | 5 | 0.3% | 159.03 | ❌ 48 conflicts |
| c_mso | 1611 | 0 | 6 | 0.4% | 1707.28 | ✅ Perfect |
| l_bst | 840 | 775 | 2 | 0.1% | 5121.36 | ✅ Perfect |
| l_mso | 1611 | 6 | 0 | 0.0% | 463.19 | ✅ Perfect |
| l_prj | 432 | 1183 | 2 | 0.1% | 367.64 | ❌ 50 conflicts |
| s_ltf | 1615 | 2 | 0 | 0.0% | 20.05 | ✅ Perfect |

### Moore Error Details
<details><summary>Errors for c_bel (2)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
</details>
<details><summary>Errors for c_dir (5)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_1_2_22.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_1_2_51.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_71.ltlf
</details>
<details><summary>Errors for c_mso (6)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_7.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_8.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_9.ltlf
</details>
<details><summary>Errors for l_bst (2)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
</details>
<details><summary>Errors for l_prj (2)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
</details>

---

## Mealy Semantics Comparison (Job 3105085 & 3109241)
*Reference: Job 3104284 (lucas_mso)*

| Tool | Success | Timeouts | Errors | Error % | Avg Time (ms) | Correctness |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| c_bel | 1194 | 421 | 2 | 0.1% | 8372.36 | ✅ Perfect |
| c_dir | 433 | 1182 | 2 | 0.1% | 261.34 | ❌ 43 conflicts |
| c_mso | 1611 | 0 | 6 | 0.4% | 1767.28 | ✅ Perfect |
| l_bst | 863 | 752 | 2 | 0.1% | 5395.40 | ✅ Perfect |
| l_mso | 1611 | 6 | 0 | 0.0% | 449.13 | ✅ Perfect |
| l_prj | 437 | 1178 | 2 | 0.1% | 430.77 | ❌ 45 conflicts |
| s_ltl | 1002 | 407 | 208 | 12.9% | 3518.94 | ✅ Perfect |
| s_ltf | 1617 | 0 | 0 | 0.0% | 41.89 | ✅ Perfect |
| s_flt (PO-Fix) | 807 | 810 | 0 | 0.0% | 1283.72 | ✅ Perfect |

### Mealy Error Details
<details><summary>Errors for c_bel (2)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
</details>
<details><summary>Errors for c_dir (2)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
</details>
<details><summary>Errors for c_mso (6)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_7.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_8.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_9.ltlf
</details>
<details><summary>Errors for l_bst (2)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
</details>
<details><summary>Errors for l_prj (2)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf
</details>
<details><summary>Errors for s_ltl (208)</summary>

- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_24.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_39.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_53.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_61.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_68.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_76.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_82.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_1.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_10.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_100.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_11.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_12.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_13.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_14.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_15.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_16.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_17.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_18.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_19.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_2.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_20.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_21.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_22.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_23.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_24.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_25.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_26.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_27.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_28.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_29.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_3.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_30.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_31.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_32.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_33.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_34.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_35.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_36.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_37.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_38.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_39.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_4.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_40.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_41.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_42.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_43.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_44.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_45.ltlf
- /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_46.ltlf
- ...
</details>

## Key Findings
1. **Correctness**: MSO-based tools (christian_mso, lucas_mso) and Spot (ltlf, ltl, ltlfilt after fix) show perfect correctness across their supported semantics.
2. **Performance**: Spot tools remain the fastest, though MSO tools are highly reliable.
3. **Partial Observability**: The latest run (Job 3109241) for `spot_ltlfilt` confirms it now matches the Mealy source of truth perfectly, resolving previous PO handling issues.