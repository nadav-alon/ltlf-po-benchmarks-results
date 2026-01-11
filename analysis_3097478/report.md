# Analysis Report for Job 3097478

## Summary Statistics

| Tool | Total | Success (1) | Unrealizable (0) | Error (-1) | Timeout (-2) |
| --- | --- | --- | --- | --- | --- |
| christian_belief | 1617 | 1615 | 0 | 2 | 0 |
| christian_direct | 1617 | 1615 | 0 | 2 | 0 |
| christian_mso | 1617 | 1617 | 0 | 0 | 0 |
| lucas_belief-states | 1617 | 718 | 119 | 7 | 773 |
| lucas_mso | 1617 | 1176 | 435 | 6 | 0 |
| lucas_projection-based | 1617 | 432 | 0 | 512 | 673 |
| spot_ltl | 1617 | 842 | 166 | 299 | 310 |
| spot_ltlf | 1617 | 1180 | 435 | 0 | 2 |
| spot_ltlfilt | 1617 | 0 | 808 | 0 | 809 |

## Error Analysis

### Unexpected Errors (Status -1)

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf: Command '"/RG/rg-fried/alnadav5/ltlf-synth-unrel-input-aaai2025/Syft/build/bin/Syft" /tmp/tmpk1w_p6fb/coins_10.ltlf.christian.ltlf /tmp/tmpk1w_p6fb/coins_10.part.christian.part 0 direct' returned non-zero exit status 1., b'./ltlf2fol NNF /tmp/tmpk1w_p6fb/coins_10.ltlf.christian.ltlf.main > /tmp/tmpk1w_p6fb/coins_10.ltlf.christian.ltlf.main.fol\n./ltlf2pfol /tmp/tmpk1w_p6fb/coins_10.ltlf.christian.ltlf.backup >/tmp/tmpk1w_p6fb/coins_10.ltlf.christian.ltlf.backup.fol\ntoken too large, exceeds YYLMAX\nError running mona for main\n'
Count: 1

| Tool | Test |
| --- | --- |
| christian_direct | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf: Command '"/RG/rg-fried/alnadav5/ltlf-synth-unrel-input-aaai2025/Syft/build/bin/Syft" /tmp/tmpnysj9_is/coins_10.ltlf.christian.ltlf /tmp/tmpnysj9_is/coins_10.part.christian.part 0 belief' returned non-zero exit status 1., b'./ltlf2fol NNF /tmp/tmpnysj9_is/coins_10.ltlf.christian.ltlf.main > /tmp/tmpnysj9_is/coins_10.ltlf.christian.ltlf.main.fol\n./ltlf2fol NNF /tmp/tmpnysj9_is/coins_10.ltlf.christian.ltlf.backup >/tmp/tmpnysj9_is/coins_10.ltlf.christian.ltlf.backup.fol\ntoken too large, exceeds YYLMAX\nError running mona for main\n'
Count: 1

| Tool | Test |
| --- | --- |
| christian_belief | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4f_abme1/coins_10.ltlf.dfa.quant /tmp/tmp4f_abme1/coins_10.part.quant 0 full dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_mso | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnqjigpmp/coins_10.ltlf.dfa /tmp/tmpnqjigpmp/coins_10.part 0 partial dfa' died with <Signals.SIGSEGV: 11>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_belief-states | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppyxf7zkb/coins_10.ltlf.dfa.rev.neg /tmp/tmppyxf7zkb/coins_10.part.rev.neg 0 partial cordfa' died with <Signals.SIGSEGV: 11>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_7.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5oue3o3a/coins_7.ltlf.dfa.quant /tmp/tmp5oue3o3a/coins_7.part.quant 0 full dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_mso | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_8.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxrowc_7u/coins_8.ltlf.dfa.quant /tmp/tmpxrowc_7u/coins_8.part.quant 0 full dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_mso | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf: Command '"/RG/rg-fried/alnadav5/ltlf-synth-unrel-input-aaai2025/Syft/build/bin/Syft" /tmp/tmp132yombq/coins_9.ltlf.christian.ltlf /tmp/tmp132yombq/coins_9.part.christian.part 0 direct' returned non-zero exit status 1., b'./ltlf2fol NNF /tmp/tmp132yombq/coins_9.ltlf.christian.ltlf.main > /tmp/tmp132yombq/coins_9.ltlf.christian.ltlf.main.fol\n./ltlf2pfol /tmp/tmp132yombq/coins_9.ltlf.christian.ltlf.backup >/tmp/tmp132yombq/coins_9.ltlf.christian.ltlf.backup.fol\ntoken too large, exceeds YYLMAX\nError running mona for main\n'
Count: 1

| Tool | Test |
| --- | --- |
| christian_direct | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf: Command '"/RG/rg-fried/alnadav5/ltlf-synth-unrel-input-aaai2025/Syft/build/bin/Syft" /tmp/tmpbnv0zm2o/coins_9.ltlf.christian.ltlf /tmp/tmpbnv0zm2o/coins_9.part.christian.part 0 belief' returned non-zero exit status 1., b'./ltlf2fol NNF /tmp/tmpbnv0zm2o/coins_9.ltlf.christian.ltlf.main > /tmp/tmpbnv0zm2o/coins_9.ltlf.christian.ltlf.main.fol\n./ltlf2fol NNF /tmp/tmpbnv0zm2o/coins_9.ltlf.christian.ltlf.backup >/tmp/tmpbnv0zm2o/coins_9.ltlf.christian.ltlf.backup.fol\ntoken too large, exceeds YYLMAX\nError running mona for main\n'
Count: 1

| Tool | Test |
| --- | --- |
| christian_belief | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1r9cyc49/coins_9.ltlf.dfa /tmp/tmp1r9cyc49/coins_9.part 0 partial dfa' died with <Signals.SIGSEGV: 11>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_belief-states | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppymvd24i/coins_9.ltlf.dfa.quant /tmp/tmppymvd24i/coins_9.part.quant 0 full dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_mso | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpzzdkil9n/coins_9.ltlf.dfa.rev.neg /tmp/tmpzzdkil9n/coins_9.part.rev.neg 0 partial cordfa' died with <Signals.SIGSEGV: 11>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/coins_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_12.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9r8hy9pe/peek_2_1_12.ltlf.dfa.rev.neg /tmp/tmp9r8hy9pe/peek_2_1_12.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_22.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkves4qkp/peek_2_1_22.ltlf.dfa.rev.neg /tmp/tmpkves4qkp/peek_2_1_22.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_22.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_30.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1nbwujgm/peek_2_1_30.ltlf.dfa.rev.neg /tmp/tmp1nbwujgm/peek_2_1_30.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_39.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2ebll1a3/peek_2_1_39.ltlf.dfa.rev.neg /tmp/tmp2ebll1a3/peek_2_1_39.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_39.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_44.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpzlu1nqtr/peek_2_1_44.ltlf.dfa.rev.neg /tmp/tmpzlu1nqtr/peek_2_1_44.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_48.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvsx7hk8h/peek_2_1_48.ltlf.dfa.rev.neg /tmp/tmpvsx7hk8h/peek_2_1_48.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_58.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcl2j3ak4/peek_2_1_58.ltlf.dfa.rev.neg /tmp/tmpcl2j3ak4/peek_2_1_58.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_59.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcg9_jxpp/peek_2_1_59.ltlf.dfa.rev.neg /tmp/tmpcg9_jxpp/peek_2_1_59.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_6.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsl50ze_7/peek_2_1_6.ltlf.dfa.rev.neg /tmp/tmpsl50ze_7/peek_2_1_6.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpn955fkmw/peek_2_1_66.ltlf.dfa.rev.neg /tmp/tmpn955fkmw/peek_2_1_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_80.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0bki80ex/peek_2_1_80.ltlf.dfa.rev.neg /tmp/tmp0bki80ex/peek_2_1_80.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_89.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8xs62eg2/peek_2_1_89.ltlf.dfa.rev.neg /tmp/tmp8xs62eg2/peek_2_1_89.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_89.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpd5nek90s/peek_2_1_93.ltlf.dfa.rev.neg /tmp/tmpd5nek90s/peek_2_1_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_95.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp50n5vwaw/peek_2_1_95.ltlf.dfa.rev.neg /tmp/tmp50n5vwaw/peek_2_1_95.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_1_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_1.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz28ahkvi/peek_2_2_1.ltlf.dfa.rev.neg /tmp/tmpz28ahkvi/peek_2_2_1.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_100.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4838esox/peek_2_2_100.ltlf.dfa.rev.neg /tmp/tmp4838esox/peek_2_2_100.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_11.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4g35r43d/peek_2_2_11.ltlf.dfa.rev.neg /tmp/tmp4g35r43d/peek_2_2_11.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_12.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbupski7b/peek_2_2_12.ltlf.dfa.rev.neg /tmp/tmpbupski7b/peek_2_2_12.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_14.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdh9o_1ru/peek_2_2_14.ltlf.dfa.rev.neg /tmp/tmpdh9o_1ru/peek_2_2_14.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_17.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0my66532/peek_2_2_17.ltlf.dfa.rev.neg /tmp/tmp0my66532/peek_2_2_17.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_18.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpzg9504r1/peek_2_2_18.ltlf.dfa.rev.neg /tmp/tmpzg9504r1/peek_2_2_18.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_20.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpj2s28xnl/peek_2_2_20.ltlf.dfa.rev.neg /tmp/tmpj2s28xnl/peek_2_2_20.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_21.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplg65b8g3/peek_2_2_21.ltlf.dfa.rev.neg /tmp/tmplg65b8g3/peek_2_2_21.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_28.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgrb2xc1j/peek_2_2_28.ltlf.dfa.rev.neg /tmp/tmpgrb2xc1j/peek_2_2_28.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_32.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_pvi4d1_/peek_2_2_32.ltlf.dfa.rev.neg /tmp/tmp_pvi4d1_/peek_2_2_32.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_34.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmptr6o25ed/peek_2_2_34.ltlf.dfa.rev.neg /tmp/tmptr6o25ed/peek_2_2_34.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_35.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpi_m30bd2/peek_2_2_35.ltlf.dfa.rev.neg /tmp/tmpi_m30bd2/peek_2_2_35.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_35.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_37.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1ky44bp1/peek_2_2_37.ltlf.dfa.rev.neg /tmp/tmp1ky44bp1/peek_2_2_37.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_38.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpuujyofa5/peek_2_2_38.ltlf.dfa.rev.neg /tmp/tmpuujyofa5/peek_2_2_38.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_39.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpalc6u353/peek_2_2_39.ltlf.dfa.rev.neg /tmp/tmpalc6u353/peek_2_2_39.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_39.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_4.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplzvtz__v/peek_2_2_4.ltlf.dfa.rev.neg /tmp/tmplzvtz__v/peek_2_2_4.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_41.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpea2hj7c9/peek_2_2_41.ltlf.dfa.rev.neg /tmp/tmpea2hj7c9/peek_2_2_41.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_43.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqzy72vk4/peek_2_2_43.ltlf.dfa.rev.neg /tmp/tmpqzy72vk4/peek_2_2_43.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_46.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2j6sfcne/peek_2_2_46.ltlf.dfa.rev.neg /tmp/tmp2j6sfcne/peek_2_2_46.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_48.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1q4hrsig/peek_2_2_48.ltlf.dfa.rev.neg /tmp/tmp1q4hrsig/peek_2_2_48.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_49.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjh5o4qrz/peek_2_2_49.ltlf.dfa.rev.neg /tmp/tmpjh5o4qrz/peek_2_2_49.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpx5ey7ygo/peek_2_2_50.ltlf.dfa.rev.neg /tmp/tmpx5ey7ygo/peek_2_2_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_51.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpf0do6_3t/peek_2_2_51.ltlf.dfa.rev.neg /tmp/tmpf0do6_3t/peek_2_2_51.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_57.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsnf7lz6z/peek_2_2_57.ltlf.dfa.rev.neg /tmp/tmpsnf7lz6z/peek_2_2_57.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_59.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5nayqvat/peek_2_2_59.ltlf.dfa.rev.neg /tmp/tmp5nayqvat/peek_2_2_59.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_6.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2qq_z7n7/peek_2_2_6.ltlf.dfa.rev.neg /tmp/tmp2qq_z7n7/peek_2_2_6.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_60.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpa7sqog_o/peek_2_2_60.ltlf.dfa.rev.neg /tmp/tmpa7sqog_o/peek_2_2_60.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_60.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_62.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpg7e3ezgy/peek_2_2_62.ltlf.dfa.rev.neg /tmp/tmpg7e3ezgy/peek_2_2_62.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_63.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0kfnmsya/peek_2_2_63.ltlf.dfa.rev.neg /tmp/tmp0kfnmsya/peek_2_2_63.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_65.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpf9qiat3g/peek_2_2_65.ltlf.dfa.rev.neg /tmp/tmpf9qiat3g/peek_2_2_65.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_68.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1kvxhoer/peek_2_2_68.ltlf.dfa.rev.neg /tmp/tmp1kvxhoer/peek_2_2_68.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_70.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmzx94h44/peek_2_2_70.ltlf.dfa.rev.neg /tmp/tmpmzx94h44/peek_2_2_70.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_71.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpylvgpgu9/peek_2_2_71.ltlf.dfa.rev.neg /tmp/tmpylvgpgu9/peek_2_2_71.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_71.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_72.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvlo5dlp3/peek_2_2_72.ltlf.dfa.rev.neg /tmp/tmpvlo5dlp3/peek_2_2_72.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_73.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpffey2et1/peek_2_2_73.ltlf.dfa.rev.neg /tmp/tmpffey2et1/peek_2_2_73.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_73.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_75.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7tppa82_/peek_2_2_75.ltlf.dfa.rev.neg /tmp/tmp7tppa82_/peek_2_2_75.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_76.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpl8dq5kkx/peek_2_2_76.ltlf.dfa.rev.neg /tmp/tmpl8dq5kkx/peek_2_2_76.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpooeswtf1/peek_2_2_77.ltlf.dfa.rev.neg /tmp/tmpooeswtf1/peek_2_2_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_80.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfauxmx45/peek_2_2_80.ltlf.dfa.rev.neg /tmp/tmpfauxmx45/peek_2_2_80.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_84.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpiw3uxsd3/peek_2_2_84.ltlf.dfa.rev.neg /tmp/tmpiw3uxsd3/peek_2_2_84.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_87.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5y89_npg/peek_2_2_87.ltlf.dfa.rev.neg /tmp/tmp5y89_npg/peek_2_2_87.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_88.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpq5fezacs/peek_2_2_88.ltlf.dfa.rev.neg /tmp/tmpq5fezacs/peek_2_2_88.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_88.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_92.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpaj83lemc/peek_2_2_92.ltlf.dfa.rev.neg /tmp/tmpaj83lemc/peek_2_2_92.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_92.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfo50h9lb/peek_2_2_93.ltlf.dfa.rev.neg /tmp/tmpfo50h9lb/peek_2_2_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_99.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfaf6n5h_/peek_2_2_99.ltlf.dfa.rev.neg /tmp/tmpfaf6n5h_/peek_2_2_99.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_2_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_1.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgpbjzmcz/peek_2_3_1.ltlf.dfa.rev.neg /tmp/tmpgpbjzmcz/peek_2_3_1.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmi_ae8m3/peek_2_3_10.ltlf.dfa.rev.neg /tmp/tmpmi_ae8m3/peek_2_3_10.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_100.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpawmrid74/peek_2_3_100.ltlf.dfa.rev.neg /tmp/tmpawmrid74/peek_2_3_100.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_11.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvnxxlpti/peek_2_3_11.ltlf.dfa.rev.neg /tmp/tmpvnxxlpti/peek_2_3_11.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_12.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpve782e6o/peek_2_3_12.ltlf.dfa.rev.neg /tmp/tmpve782e6o/peek_2_3_12.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_14.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpj30iucmx/peek_2_3_14.ltlf.dfa.rev.neg /tmp/tmpj30iucmx/peek_2_3_14.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_18.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpibd99kwu/peek_2_3_18.ltlf.dfa.rev.neg /tmp/tmpibd99kwu/peek_2_3_18.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_19.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9z785gju/peek_2_3_19.ltlf.dfa.rev.neg /tmp/tmp9z785gju/peek_2_3_19.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_2.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3scoid1t/peek_2_3_2.ltlf.dfa.rev.neg /tmp/tmp3scoid1t/peek_2_3_2.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_2.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_21.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpyips0ic0/peek_2_3_21.ltlf.dfa.rev.neg /tmp/tmpyips0ic0/peek_2_3_21.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_26.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppr_9pbwx/peek_2_3_26.ltlf.dfa.rev.neg /tmp/tmppr_9pbwx/peek_2_3_26.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_28.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3t_7z7j5/peek_2_3_28.ltlf.dfa.rev.neg /tmp/tmp3t_7z7j5/peek_2_3_28.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_33.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpa_pgiyk4/peek_2_3_33.ltlf.dfa.rev.neg /tmp/tmpa_pgiyk4/peek_2_3_33.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_33.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_34.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbwk1o0gu/peek_2_3_34.ltlf.dfa.rev.neg /tmp/tmpbwk1o0gu/peek_2_3_34.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_35.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqov61teg/peek_2_3_35.ltlf.dfa.rev.neg /tmp/tmpqov61teg/peek_2_3_35.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_35.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_36.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5l3masa4/peek_2_3_36.ltlf.dfa.rev.neg /tmp/tmp5l3masa4/peek_2_3_36.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_36.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_37.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp67qt55f2/peek_2_3_37.ltlf.dfa.rev.neg /tmp/tmp67qt55f2/peek_2_3_37.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_38.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcabr6jtg/peek_2_3_38.ltlf.dfa.rev.neg /tmp/tmpcabr6jtg/peek_2_3_38.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_41.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpv9yizkt4/peek_2_3_41.ltlf.dfa.rev.neg /tmp/tmpv9yizkt4/peek_2_3_41.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_44.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbbrkbumo/peek_2_3_44.ltlf.dfa.rev.neg /tmp/tmpbbrkbumo/peek_2_3_44.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_45.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz7r2_28n/peek_2_3_45.ltlf.dfa.rev.neg /tmp/tmpz7r2_28n/peek_2_3_45.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_47.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpzn7vof5y/peek_2_3_47.ltlf.dfa.rev.neg /tmp/tmpzn7vof5y/peek_2_3_47.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_48.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp50042ceo/peek_2_3_48.ltlf.dfa.rev.neg /tmp/tmp50042ceo/peek_2_3_48.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_49.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpav1dyk1s/peek_2_3_49.ltlf.dfa.rev.neg /tmp/tmpav1dyk1s/peek_2_3_49.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_5.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7aox63qc/peek_2_3_5.ltlf.dfa.rev.neg /tmp/tmp7aox63qc/peek_2_3_5.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmperbkhq9k/peek_2_3_50.ltlf.dfa.rev.neg /tmp/tmperbkhq9k/peek_2_3_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_51.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpc6541plw/peek_2_3_51.ltlf.dfa.rev.neg /tmp/tmpc6541plw/peek_2_3_51.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_54.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpw10js5at/peek_2_3_54.ltlf.dfa.rev.neg /tmp/tmpw10js5at/peek_2_3_54.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_55.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp10cg91jy/peek_2_3_55.ltlf.dfa.rev.neg /tmp/tmp10cg91jy/peek_2_3_55.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_57.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvrbokc5t/peek_2_3_57.ltlf.dfa.rev.neg /tmp/tmpvrbokc5t/peek_2_3_57.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_58.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz02oc5xq/peek_2_3_58.ltlf.dfa.rev.neg /tmp/tmpz02oc5xq/peek_2_3_58.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_6.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnb6elkqv/peek_2_3_6.ltlf.dfa.rev.neg /tmp/tmpnb6elkqv/peek_2_3_6.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_62.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpba74vdah/peek_2_3_62.ltlf.dfa.rev.neg /tmp/tmpba74vdah/peek_2_3_62.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_63.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsjn_l5m4/peek_2_3_63.ltlf.dfa.rev.neg /tmp/tmpsjn_l5m4/peek_2_3_63.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_64.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpm1w7qr9r/peek_2_3_64.ltlf.dfa.rev.neg /tmp/tmpm1w7qr9r/peek_2_3_64.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_64.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_65.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxqbl1r2z/peek_2_3_65.ltlf.dfa.rev.neg /tmp/tmpxqbl1r2z/peek_2_3_65.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpir3xbety/peek_2_3_66.ltlf.dfa.rev.neg /tmp/tmpir3xbety/peek_2_3_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_68.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkkihixg_/peek_2_3_68.ltlf.dfa.rev.neg /tmp/tmpkkihixg_/peek_2_3_68.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_69.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppj4k4yx3/peek_2_3_69.ltlf.dfa.rev.neg /tmp/tmppj4k4yx3/peek_2_3_69.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_69.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_7.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkz8mct32/peek_2_3_7.ltlf.dfa.rev.neg /tmp/tmpkz8mct32/peek_2_3_7.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_71.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkhvb_3to/peek_2_3_71.ltlf.dfa.rev.neg /tmp/tmpkhvb_3to/peek_2_3_71.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_71.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_74.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmptjjoxix4/peek_2_3_74.ltlf.dfa.rev.neg /tmp/tmptjjoxix4/peek_2_3_74.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpot_t50mr/peek_2_3_77.ltlf.dfa.rev.neg /tmp/tmpot_t50mr/peek_2_3_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_78.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmmqlv1fz/peek_2_3_78.ltlf.dfa.rev.neg /tmp/tmpmmqlv1fz/peek_2_3_78.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_8.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpddenyhk5/peek_2_3_8.ltlf.dfa.rev.neg /tmp/tmpddenyhk5/peek_2_3_8.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_80.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwiutf3eg/peek_2_3_80.ltlf.dfa.rev.neg /tmp/tmpwiutf3eg/peek_2_3_80.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_81.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpy8hod8ub/peek_2_3_81.ltlf.dfa.rev.neg /tmp/tmpy8hod8ub/peek_2_3_81.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_82.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp158u_1xo/peek_2_3_82.ltlf.dfa.rev.neg /tmp/tmp158u_1xo/peek_2_3_82.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_83.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8xzuwn4h/peek_2_3_83.ltlf.dfa.rev.neg /tmp/tmp8xzuwn4h/peek_2_3_83.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_84.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmphx_w15ge/peek_2_3_84.ltlf.dfa.rev.neg /tmp/tmphx_w15ge/peek_2_3_84.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_85.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppb62gx8o/peek_2_3_85.ltlf.dfa.rev.neg /tmp/tmppb62gx8o/peek_2_3_85.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_86.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4oo6bs5w/peek_2_3_86.ltlf.dfa.rev.neg /tmp/tmp4oo6bs5w/peek_2_3_86.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_87.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpm_t1yk02/peek_2_3_87.ltlf.dfa.rev.neg /tmp/tmpm_t1yk02/peek_2_3_87.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_88.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpftasye3_/peek_2_3_88.ltlf.dfa.rev.neg /tmp/tmpftasye3_/peek_2_3_88.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_88.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp08biir_t/peek_2_3_9.ltlf.dfa.rev.neg /tmp/tmp08biir_t/peek_2_3_9.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_91.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpn2p5_1w8/peek_2_3_91.ltlf.dfa.rev.neg /tmp/tmpn2p5_1w8/peek_2_3_91.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_92.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpl2p51_7i/peek_2_3_92.ltlf.dfa.rev.neg /tmp/tmpl2p51_7i/peek_2_3_92.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_92.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplbbto3qz/peek_2_3_93.ltlf.dfa.rev.neg /tmp/tmplbbto3qz/peek_2_3_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_94.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkva9r4tb/peek_2_3_94.ltlf.dfa.rev.neg /tmp/tmpkva9r4tb/peek_2_3_94.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_96.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5tr8jv2u/peek_2_3_96.ltlf.dfa.rev.neg /tmp/tmp5tr8jv2u/peek_2_3_96.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_96.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_98.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp89_vmuhq/peek_2_3_98.ltlf.dfa.rev.neg /tmp/tmp89_vmuhq/peek_2_3_98.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_98.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_99.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpehrl2hme/peek_2_3_99.ltlf.dfa.rev.neg /tmp/tmpehrl2hme/peek_2_3_99.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_3_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_1.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjazmgg3b/peek_2_4_1.ltlf.dfa.rev.neg /tmp/tmpjazmgg3b/peek_2_4_1.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpu8kakwkh/peek_2_4_10.ltlf.dfa.rev.neg /tmp/tmpu8kakwkh/peek_2_4_10.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_100.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3watvuou/peek_2_4_100.ltlf.dfa.rev.neg /tmp/tmp3watvuou/peek_2_4_100.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_11.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplsznyxgj/peek_2_4_11.ltlf.dfa.rev.neg /tmp/tmplsznyxgj/peek_2_4_11.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_12.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwlwmbw56/peek_2_4_12.ltlf.dfa.rev.neg /tmp/tmpwlwmbw56/peek_2_4_12.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_13.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpasvwg3j4/peek_2_4_13.ltlf.dfa.rev.neg /tmp/tmpasvwg3j4/peek_2_4_13.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_13.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_14.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpw3sb2837/peek_2_4_14.ltlf.dfa.rev.neg /tmp/tmpw3sb2837/peek_2_4_14.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_15.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdr51k4s8/peek_2_4_15.ltlf.dfa.rev.neg /tmp/tmpdr51k4s8/peek_2_4_15.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_17.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqerzw4rl/peek_2_4_17.ltlf.dfa.rev.neg /tmp/tmpqerzw4rl/peek_2_4_17.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_18.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmph4xszgwo/peek_2_4_18.ltlf.dfa.rev.neg /tmp/tmph4xszgwo/peek_2_4_18.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_19.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp26fyp2gc/peek_2_4_19.ltlf.dfa.rev.neg /tmp/tmp26fyp2gc/peek_2_4_19.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_21.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvr2scrwl/peek_2_4_21.ltlf.dfa.rev.neg /tmp/tmpvr2scrwl/peek_2_4_21.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_25.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6_ij9ln9/peek_2_4_25.ltlf.dfa.rev.neg /tmp/tmp6_ij9ln9/peek_2_4_25.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_26.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwcqkituz/peek_2_4_26.ltlf.dfa.rev.neg /tmp/tmpwcqkituz/peek_2_4_26.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_29.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkn755bj9/peek_2_4_29.ltlf.dfa.rev.neg /tmp/tmpkn755bj9/peek_2_4_29.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_29.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_30.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7e6mcjnn/peek_2_4_30.ltlf.dfa.rev.neg /tmp/tmp7e6mcjnn/peek_2_4_30.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_31.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp92pfwm3s/peek_2_4_31.ltlf.dfa.rev.neg /tmp/tmp92pfwm3s/peek_2_4_31.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_31.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_32.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwl0ukl0u/peek_2_4_32.ltlf.dfa.rev.neg /tmp/tmpwl0ukl0u/peek_2_4_32.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_33.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp94v21paz/peek_2_4_33.ltlf.dfa.rev.neg /tmp/tmp94v21paz/peek_2_4_33.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_33.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_34.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfdum62et/peek_2_4_34.ltlf.dfa.rev.neg /tmp/tmpfdum62et/peek_2_4_34.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_36.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpe_ile5g_/peek_2_4_36.ltlf.dfa.rev.neg /tmp/tmpe_ile5g_/peek_2_4_36.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_36.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_38.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp62mg83x5/peek_2_4_38.ltlf.dfa.rev.neg /tmp/tmp62mg83x5/peek_2_4_38.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_39.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8bby54_z/peek_2_4_39.ltlf.dfa.rev.neg /tmp/tmp8bby54_z/peek_2_4_39.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_39.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_4.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsy0j4ex4/peek_2_4_4.ltlf.dfa.rev.neg /tmp/tmpsy0j4ex4/peek_2_4_4.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_40.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmperfgu8n0/peek_2_4_40.ltlf.dfa.rev.neg /tmp/tmperfgu8n0/peek_2_4_40.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_40.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_41.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6m713kyv/peek_2_4_41.ltlf.dfa.rev.neg /tmp/tmp6m713kyv/peek_2_4_41.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_42.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpt16xge5q/peek_2_4_42.ltlf.dfa.rev.neg /tmp/tmpt16xge5q/peek_2_4_42.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_42.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_43.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpo83dqx6k/peek_2_4_43.ltlf.dfa.rev.neg /tmp/tmpo83dqx6k/peek_2_4_43.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_44.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjz2milwo/peek_2_4_44.ltlf.dfa.rev.neg /tmp/tmpjz2milwo/peek_2_4_44.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_45.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxc1w805p/peek_2_4_45.ltlf.dfa.rev.neg /tmp/tmpxc1w805p/peek_2_4_45.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_46.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmps7qzin1y/peek_2_4_46.ltlf.dfa.rev.neg /tmp/tmps7qzin1y/peek_2_4_46.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_47.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8b__5vlo/peek_2_4_47.ltlf.dfa.rev.neg /tmp/tmp8b__5vlo/peek_2_4_47.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_48.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmptnu9pu6o/peek_2_4_48.ltlf.dfa.rev.neg /tmp/tmptnu9pu6o/peek_2_4_48.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_49.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8lx6wpjb/peek_2_4_49.ltlf.dfa.rev.neg /tmp/tmp8lx6wpjb/peek_2_4_49.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_5.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplh3psqyj/peek_2_4_5.ltlf.dfa.rev.neg /tmp/tmplh3psqyj/peek_2_4_5.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9bh4mx01/peek_2_4_50.ltlf.dfa.rev.neg /tmp/tmp9bh4mx01/peek_2_4_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_51.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7fijhiat/peek_2_4_51.ltlf.dfa.rev.neg /tmp/tmp7fijhiat/peek_2_4_51.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_52.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpj_suiivf/peek_2_4_52.ltlf.dfa.rev.neg /tmp/tmpj_suiivf/peek_2_4_52.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_53.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcydm81e4/peek_2_4_53.ltlf.dfa.rev.neg /tmp/tmpcydm81e4/peek_2_4_53.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_55.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsrj0vv0h/peek_2_4_55.ltlf.dfa.rev.neg /tmp/tmpsrj0vv0h/peek_2_4_55.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_56.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpomd3yy7t/peek_2_4_56.ltlf.dfa.rev.neg /tmp/tmpomd3yy7t/peek_2_4_56.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_58.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpyx6quvg5/peek_2_4_58.ltlf.dfa.rev.neg /tmp/tmpyx6quvg5/peek_2_4_58.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_59.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvanzc2ph/peek_2_4_59.ltlf.dfa.rev.neg /tmp/tmpvanzc2ph/peek_2_4_59.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_6.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjazrlctq/peek_2_4_6.ltlf.dfa.rev.neg /tmp/tmpjazrlctq/peek_2_4_6.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_61.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpw1r8k3ed/peek_2_4_61.ltlf.dfa.rev.neg /tmp/tmpw1r8k3ed/peek_2_4_61.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_61.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_62.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4x0zzldv/peek_2_4_62.ltlf.dfa.rev.neg /tmp/tmp4x0zzldv/peek_2_4_62.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_65.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpd6ty3aen/peek_2_4_65.ltlf.dfa.rev.neg /tmp/tmpd6ty3aen/peek_2_4_65.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpm79biqkx/peek_2_4_66.ltlf.dfa.rev.neg /tmp/tmpm79biqkx/peek_2_4_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_67.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9ukrcc6l/peek_2_4_67.ltlf.dfa.rev.neg /tmp/tmp9ukrcc6l/peek_2_4_67.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_67.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_68.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpyno074wz/peek_2_4_68.ltlf.dfa.rev.neg /tmp/tmpyno074wz/peek_2_4_68.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_69.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpt9x0b7oa/peek_2_4_69.ltlf.dfa.rev.neg /tmp/tmpt9x0b7oa/peek_2_4_69.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_69.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_7.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplk36l4yl/peek_2_4_7.ltlf.dfa.rev.neg /tmp/tmplk36l4yl/peek_2_4_7.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_70.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxyvywabp/peek_2_4_70.ltlf.dfa.rev.neg /tmp/tmpxyvywabp/peek_2_4_70.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_73.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmps922pejt/peek_2_4_73.ltlf.dfa.rev.neg /tmp/tmps922pejt/peek_2_4_73.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_73.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_74.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpulf53db6/peek_2_4_74.ltlf.dfa.rev.neg /tmp/tmpulf53db6/peek_2_4_74.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_75.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpon_71e09/peek_2_4_75.ltlf.dfa.rev.neg /tmp/tmpon_71e09/peek_2_4_75.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_76.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpahkcpka3/peek_2_4_76.ltlf.dfa.rev.neg /tmp/tmpahkcpka3/peek_2_4_76.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2pe114ws/peek_2_4_77.ltlf.dfa.rev.neg /tmp/tmp2pe114ws/peek_2_4_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_78.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9mo_404i/peek_2_4_78.ltlf.dfa.rev.neg /tmp/tmp9mo_404i/peek_2_4_78.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_80.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjrs_untt/peek_2_4_80.ltlf.dfa.rev.neg /tmp/tmpjrs_untt/peek_2_4_80.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_81.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpowwob7je/peek_2_4_81.ltlf.dfa.rev.neg /tmp/tmpowwob7je/peek_2_4_81.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_82.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp47mqakbc/peek_2_4_82.ltlf.dfa.rev.neg /tmp/tmp47mqakbc/peek_2_4_82.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_83.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmptcc10b8x/peek_2_4_83.ltlf.dfa.rev.neg /tmp/tmptcc10b8x/peek_2_4_83.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_84.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmphm6y19u0/peek_2_4_84.ltlf.dfa.rev.neg /tmp/tmphm6y19u0/peek_2_4_84.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_85.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz0bn37qs/peek_2_4_85.ltlf.dfa.rev.neg /tmp/tmpz0bn37qs/peek_2_4_85.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_86.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5etlltby/peek_2_4_86.ltlf.dfa.rev.neg /tmp/tmp5etlltby/peek_2_4_86.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_87.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpj7vai_vb/peek_2_4_87.ltlf.dfa.rev.neg /tmp/tmpj7vai_vb/peek_2_4_87.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_89.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1g2bma1v/peek_2_4_89.ltlf.dfa.rev.neg /tmp/tmp1g2bma1v/peek_2_4_89.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_89.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7e1mi6ow/peek_2_4_9.ltlf.dfa.rev.neg /tmp/tmp7e1mi6ow/peek_2_4_9.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_91.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_mmk61rf/peek_2_4_91.ltlf.dfa.rev.neg /tmp/tmp_mmk61rf/peek_2_4_91.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvb248ndy/peek_2_4_93.ltlf.dfa.rev.neg /tmp/tmpvb248ndy/peek_2_4_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_94.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnjikg2id/peek_2_4_94.ltlf.dfa.rev.neg /tmp/tmpnjikg2id/peek_2_4_94.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_95.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqx6iwhqz/peek_2_4_95.ltlf.dfa.rev.neg /tmp/tmpqx6iwhqz/peek_2_4_95.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_97.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_uzptn7r/peek_2_4_97.ltlf.dfa.rev.neg /tmp/tmp_uzptn7r/peek_2_4_97.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_97.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_98.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8o81k7vo/peek_2_4_98.ltlf.dfa.rev.neg /tmp/tmp8o81k7vo/peek_2_4_98.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_98.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_99.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmph0z8cvtc/peek_2_4_99.ltlf.dfa.rev.neg /tmp/tmph0z8cvtc/peek_2_4_99.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_2_4_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_13.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5qr884j7/peek_3_2_13.ltlf.dfa.rev.neg /tmp/tmp5qr884j7/peek_3_2_13.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_13.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_25.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_9vtqy_a/peek_3_2_25.ltlf.dfa.rev.neg /tmp/tmp_9vtqy_a/peek_3_2_25.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_43.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwg3aykz5/peek_3_2_43.ltlf.dfa.rev.neg /tmp/tmpwg3aykz5/peek_3_2_43.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_49.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1e3i5dpl/peek_3_2_49.ltlf.dfa.rev.neg /tmp/tmp1e3i5dpl/peek_3_2_49.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_70.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1j5r190l/peek_3_2_70.ltlf.dfa.rev.neg /tmp/tmp1j5r190l/peek_3_2_70.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_85.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpk4c9ai85/peek_3_2_85.ltlf.dfa.rev.neg /tmp/tmpk4c9ai85/peek_3_2_85.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_97.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmpfsece7/peek_3_2_97.ltlf.dfa.rev.neg /tmp/tmpmpfsece7/peek_3_2_97.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_2_97.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_26.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4kp2n9ig/peek_3_3_26.ltlf.dfa /tmp/tmp4kp2n9ig/peek_3_3_26.part 0 partial dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 140\nThe number of state variables: 140\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_belief-states | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_3.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqx7qgqxa/peek_3_3_3.ltlf.dfa.rev.neg /tmp/tmpqx7qgqxa/peek_3_3_3.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_3.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_31.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5uir_42v/peek_3_3_31.ltlf.dfa.rev.neg /tmp/tmp5uir_42v/peek_3_3_31.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_31.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_32.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgmd_xuht/peek_3_3_32.ltlf.dfa.rev.neg /tmp/tmpgmd_xuht/peek_3_3_32.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_37.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppxer85yr/peek_3_3_37.ltlf.dfa.rev.neg /tmp/tmppxer85yr/peek_3_3_37.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_41.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpavnygkww/peek_3_3_41.ltlf.dfa.rev.neg /tmp/tmpavnygkww/peek_3_3_41.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_1dw9_j5/peek_3_3_50.ltlf.dfa.rev.neg /tmp/tmp_1dw9_j5/peek_3_3_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_52.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpeywcq01u/peek_3_3_52.ltlf.dfa.rev.neg /tmp/tmpeywcq01u/peek_3_3_52.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_59.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpl6svrksf/peek_3_3_59.ltlf.dfa.rev.neg /tmp/tmpl6svrksf/peek_3_3_59.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_62.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp42646whp/peek_3_3_62.ltlf.dfa.rev.neg /tmp/tmp42646whp/peek_3_3_62.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmrn_cuhe/peek_3_3_66.ltlf.dfa.rev.neg /tmp/tmpmrn_cuhe/peek_3_3_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7x9vo161/peek_3_3_77.ltlf.dfa.rev.neg /tmp/tmp7x9vo161/peek_3_3_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_78.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkbr0jam1/peek_3_3_78.ltlf.dfa.rev.neg /tmp/tmpkbr0jam1/peek_3_3_78.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_84.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpympi_ix8/peek_3_3_84.ltlf.dfa.rev.neg /tmp/tmpympi_ix8/peek_3_3_84.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_91.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8cdynkl8/peek_3_3_91.ltlf.dfa.rev.neg /tmp/tmp8cdynkl8/peek_3_3_91.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_94.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxwmswzkq/peek_3_3_94.ltlf.dfa.rev.neg /tmp/tmpxwmswzkq/peek_3_3_94.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_3_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_100.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbqf_kzym/peek_3_4_100.ltlf.dfa.rev.neg /tmp/tmpbqf_kzym/peek_3_4_100.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_11.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpi2or73qa/peek_3_4_11.ltlf.dfa.rev.neg /tmp/tmpi2or73qa/peek_3_4_11.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_15.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0qplobdk/peek_3_4_15.ltlf.dfa.rev.neg /tmp/tmp0qplobdk/peek_3_4_15.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_18.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpaq08zpsj/peek_3_4_18.ltlf.dfa.rev.neg /tmp/tmpaq08zpsj/peek_3_4_18.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_20.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpx7emw1fm/peek_3_4_20.ltlf.dfa.rev.neg /tmp/tmpx7emw1fm/peek_3_4_20.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_22.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6_jk6yaj/peek_3_4_22.ltlf.dfa.rev.neg /tmp/tmp6_jk6yaj/peek_3_4_22.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_22.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_23.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdh9fba_i/peek_3_4_23.ltlf.dfa.rev.neg /tmp/tmpdh9fba_i/peek_3_4_23.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_23.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_27.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_ypmkeip/peek_3_4_27.ltlf.dfa.rev.neg /tmp/tmp_ypmkeip/peek_3_4_27.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_27.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_32.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgkqxlkj2/peek_3_4_32.ltlf.dfa.rev.neg /tmp/tmpgkqxlkj2/peek_3_4_32.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_44.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvoz5a9q6/peek_3_4_44.ltlf.dfa.rev.neg /tmp/tmpvoz5a9q6/peek_3_4_44.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_45.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8tbroksz/peek_3_4_45.ltlf.dfa.rev.neg /tmp/tmp8tbroksz/peek_3_4_45.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_46.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5rngh9zh/peek_3_4_46.ltlf.dfa.rev.neg /tmp/tmp5rngh9zh/peek_3_4_46.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_48.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvmj9yon4/peek_3_4_48.ltlf.dfa.rev.neg /tmp/tmpvmj9yon4/peek_3_4_48.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_49.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwqkvu4jt/peek_3_4_49.ltlf.dfa.rev.neg /tmp/tmpwqkvu4jt/peek_3_4_49.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8i8exkgu/peek_3_4_50.ltlf.dfa.rev.neg /tmp/tmp8i8exkgu/peek_3_4_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_51.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmprmd9scjz/peek_3_4_51.ltlf.dfa.rev.neg /tmp/tmprmd9scjz/peek_3_4_51.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_52.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmoe41r9h/peek_3_4_52.ltlf.dfa.rev.neg /tmp/tmpmoe41r9h/peek_3_4_52.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_53.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1_rzciqj/peek_3_4_53.ltlf.dfa.rev.neg /tmp/tmp1_rzciqj/peek_3_4_53.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_55.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3qnttdh6/peek_3_4_55.ltlf.dfa.rev.neg /tmp/tmp3qnttdh6/peek_3_4_55.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_56.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfs6v93vn/peek_3_4_56.ltlf.dfa.rev.neg /tmp/tmpfs6v93vn/peek_3_4_56.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_61.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2pxow3gn/peek_3_4_61.ltlf.dfa.rev.neg /tmp/tmp2pxow3gn/peek_3_4_61.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_61.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnirjsgjg/peek_3_4_66.ltlf.dfa.rev.neg /tmp/tmpnirjsgjg/peek_3_4_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_7.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_4j254yw/peek_3_4_7.ltlf.dfa.rev.neg /tmp/tmp_4j254yw/peek_3_4_7.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbvgmrgb5/peek_3_4_77.ltlf.dfa.rev.neg /tmp/tmpbvgmrgb5/peek_3_4_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_81.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppebh7aby/peek_3_4_81.ltlf.dfa.rev.neg /tmp/tmppebh7aby/peek_3_4_81.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_82.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmphxniqylu/peek_3_4_82.ltlf.dfa.rev.neg /tmp/tmphxniqylu/peek_3_4_82.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_83.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpao_4hrdv/peek_3_4_83.ltlf.dfa.rev.neg /tmp/tmpao_4hrdv/peek_3_4_83.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_84.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpb2jmmem9/peek_3_4_84.ltlf.dfa.rev.neg /tmp/tmpb2jmmem9/peek_3_4_84.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpey8hj1_e/peek_3_4_9.ltlf.dfa.rev.neg /tmp/tmpey8hj1_e/peek_3_4_9.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4k76dzfh/peek_3_4_93.ltlf.dfa.rev.neg /tmp/tmp4k76dzfh/peek_3_4_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_3_4_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_1.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp79ocuvzj/peek_4_1_1.ltlf.dfa.rev.neg /tmp/tmp79ocuvzj/peek_4_1_1.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5qph5kf4/peek_4_1_10.ltlf.dfa.rev.neg /tmp/tmp5qph5kf4/peek_4_1_10.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_100.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpubexozdn/peek_4_1_100.ltlf.dfa.rev.neg /tmp/tmpubexozdn/peek_4_1_100.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_11.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpube6f1cz/peek_4_1_11.ltlf.dfa.rev.neg /tmp/tmpube6f1cz/peek_4_1_11.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_12.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmx2bowcz/peek_4_1_12.ltlf.dfa.rev.neg /tmp/tmpmx2bowcz/peek_4_1_12.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_14.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpd0ofwuyb/peek_4_1_14.ltlf.dfa.rev.neg /tmp/tmpd0ofwuyb/peek_4_1_14.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_15.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjglbmyez/peek_4_1_15.ltlf.dfa.rev.neg /tmp/tmpjglbmyez/peek_4_1_15.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_17.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpat8_0wdz/peek_4_1_17.ltlf.dfa.rev.neg /tmp/tmpat8_0wdz/peek_4_1_17.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_18.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpe21sb0ls/peek_4_1_18.ltlf.dfa /tmp/tmpe21sb0ls/peek_4_1_18.part 0 partial dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 1019\nThe number of state variables: 1019\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_belief-states | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_18.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpv9n16nfp/peek_4_1_18.ltlf.dfa.rev.neg /tmp/tmpv9n16nfp/peek_4_1_18.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_19.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpar2ep9hy/peek_4_1_19.ltlf.dfa.rev.neg /tmp/tmpar2ep9hy/peek_4_1_19.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_20.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqd06znf9/peek_4_1_20.ltlf.dfa.rev.neg /tmp/tmpqd06znf9/peek_4_1_20.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_21.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpm5jmwzuf/peek_4_1_21.ltlf.dfa.rev.neg /tmp/tmpm5jmwzuf/peek_4_1_21.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_22.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpq8__2jb_/peek_4_1_22.ltlf.dfa.rev.neg /tmp/tmpq8__2jb_/peek_4_1_22.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_22.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_23.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpumt_16lg/peek_4_1_23.ltlf.dfa.rev.neg /tmp/tmpumt_16lg/peek_4_1_23.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_23.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_25.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplvx51wpr/peek_4_1_25.ltlf.dfa.rev.neg /tmp/tmplvx51wpr/peek_4_1_25.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_26.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkrtzg0qh/peek_4_1_26.ltlf.dfa.rev.neg /tmp/tmpkrtzg0qh/peek_4_1_26.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_27.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpg_jhpcs8/peek_4_1_27.ltlf.dfa.rev.neg /tmp/tmpg_jhpcs8/peek_4_1_27.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_27.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_28.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpljeg0m95/peek_4_1_28.ltlf.dfa /tmp/tmpljeg0m95/peek_4_1_28.part 0 partial dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 1007\nThe number of state variables: 1007\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_belief-states | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_28.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpr82czi1p/peek_4_1_28.ltlf.dfa.rev.neg /tmp/tmpr82czi1p/peek_4_1_28.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_29.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0_4_38kd/peek_4_1_29.ltlf.dfa.rev.neg /tmp/tmp0_4_38kd/peek_4_1_29.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_29.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_3.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplbdad83g/peek_4_1_3.ltlf.dfa.rev.neg /tmp/tmplbdad83g/peek_4_1_3.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_3.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_30.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpj79etb3q/peek_4_1_30.ltlf.dfa.rev.neg /tmp/tmpj79etb3q/peek_4_1_30.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_32.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkgfwtzo1/peek_4_1_32.ltlf.dfa.rev.neg /tmp/tmpkgfwtzo1/peek_4_1_32.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_34.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7jc6rbbu/peek_4_1_34.ltlf.dfa.rev.neg /tmp/tmp7jc6rbbu/peek_4_1_34.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_35.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpv4pccgxt/peek_4_1_35.ltlf.dfa.rev.neg /tmp/tmpv4pccgxt/peek_4_1_35.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_35.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_36.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmproxmemp3/peek_4_1_36.ltlf.dfa.rev.neg /tmp/tmproxmemp3/peek_4_1_36.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_36.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_37.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpc776cr8d/peek_4_1_37.ltlf.dfa.rev.neg /tmp/tmpc776cr8d/peek_4_1_37.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_38.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjvw9c73d/peek_4_1_38.ltlf.dfa.rev.neg /tmp/tmpjvw9c73d/peek_4_1_38.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_39.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdvrczp_2/peek_4_1_39.ltlf.dfa.rev.neg /tmp/tmpdvrczp_2/peek_4_1_39.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_39.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_4.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvdonj25f/peek_4_1_4.ltlf.dfa.rev.neg /tmp/tmpvdonj25f/peek_4_1_4.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_40.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5mfdckfb/peek_4_1_40.ltlf.dfa.rev.neg /tmp/tmp5mfdckfb/peek_4_1_40.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_40.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_41.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3hsslity/peek_4_1_41.ltlf.dfa.rev.neg /tmp/tmp3hsslity/peek_4_1_41.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_42.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3ik8e6ls/peek_4_1_42.ltlf.dfa.rev.neg /tmp/tmp3ik8e6ls/peek_4_1_42.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_42.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_44.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8_aw3x2w/peek_4_1_44.ltlf.dfa.rev.neg /tmp/tmp8_aw3x2w/peek_4_1_44.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_45.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpaqalmptt/peek_4_1_45.ltlf.dfa.rev.neg /tmp/tmpaqalmptt/peek_4_1_45.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_46.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5fl78cki/peek_4_1_46.ltlf.dfa.rev.neg /tmp/tmp5fl78cki/peek_4_1_46.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_47.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8f3_wqz4/peek_4_1_47.ltlf.dfa.rev.neg /tmp/tmp8f3_wqz4/peek_4_1_47.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_5.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbeucivyx/peek_4_1_5.ltlf.dfa.rev.neg /tmp/tmpbeucivyx/peek_4_1_5.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgk9hgmln/peek_4_1_50.ltlf.dfa.rev.neg /tmp/tmpgk9hgmln/peek_4_1_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_51.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvbmxcuj4/peek_4_1_51.ltlf.dfa.rev.neg /tmp/tmpvbmxcuj4/peek_4_1_51.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_52.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmheprwiq/peek_4_1_52.ltlf.dfa.rev.neg /tmp/tmpmheprwiq/peek_4_1_52.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_53.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnvj2u1lq/peek_4_1_53.ltlf.dfa.rev.neg /tmp/tmpnvj2u1lq/peek_4_1_53.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_54.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpw7ue4hqp/peek_4_1_54.ltlf.dfa.rev.neg /tmp/tmpw7ue4hqp/peek_4_1_54.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_57.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwmb3w40g/peek_4_1_57.ltlf.dfa /tmp/tmpwmb3w40g/peek_4_1_57.part 0 partial dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 1037\nThe number of state variables: 1037\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_belief-states | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_57.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpy9o30xhg/peek_4_1_57.ltlf.dfa.rev.neg /tmp/tmpy9o30xhg/peek_4_1_57.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_58.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpt5jnpwza/peek_4_1_58.ltlf.dfa.rev.neg /tmp/tmpt5jnpwza/peek_4_1_58.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_59.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp09ytnheg/peek_4_1_59.ltlf.dfa.rev.neg /tmp/tmp09ytnheg/peek_4_1_59.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_6.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9wc9ag7a/peek_4_1_6.ltlf.dfa.rev.neg /tmp/tmp9wc9ag7a/peek_4_1_6.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_60.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplp_h_0wb/peek_4_1_60.ltlf.dfa.rev.neg /tmp/tmplp_h_0wb/peek_4_1_60.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_60.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_61.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpaf3665h0/peek_4_1_61.ltlf.dfa.rev.neg /tmp/tmpaf3665h0/peek_4_1_61.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_61.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_62.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmptv0d59hp/peek_4_1_62.ltlf.dfa.rev.neg /tmp/tmptv0d59hp/peek_4_1_62.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_63.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9v0k32gb/peek_4_1_63.ltlf.dfa.rev.neg /tmp/tmp9v0k32gb/peek_4_1_63.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_65.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppndbw10s/peek_4_1_65.ltlf.dfa.rev.neg /tmp/tmppndbw10s/peek_4_1_65.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4_zx091u/peek_4_1_66.ltlf.dfa.rev.neg /tmp/tmp4_zx091u/peek_4_1_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_68.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp97d19mr4/peek_4_1_68.ltlf.dfa.rev.neg /tmp/tmp97d19mr4/peek_4_1_68.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_69.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvhut32w_/peek_4_1_69.ltlf.dfa.rev.neg /tmp/tmpvhut32w_/peek_4_1_69.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_69.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_7.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplkxvtl21/peek_4_1_7.ltlf.dfa.rev.neg /tmp/tmplkxvtl21/peek_4_1_7.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_70.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcsib_qrg/peek_4_1_70.ltlf.dfa.rev.neg /tmp/tmpcsib_qrg/peek_4_1_70.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_71.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_tfpkshc/peek_4_1_71.ltlf.dfa.rev.neg /tmp/tmp_tfpkshc/peek_4_1_71.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_71.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_72.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfdjxk42_/peek_4_1_72.ltlf.dfa.rev.neg /tmp/tmpfdjxk42_/peek_4_1_72.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_73.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8rl6bicq/peek_4_1_73.ltlf.dfa.rev.neg /tmp/tmp8rl6bicq/peek_4_1_73.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_73.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_74.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpw00c83r3/peek_4_1_74.ltlf.dfa.rev.neg /tmp/tmpw00c83r3/peek_4_1_74.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_75.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfky7z0hl/peek_4_1_75.ltlf.dfa.rev.neg /tmp/tmpfky7z0hl/peek_4_1_75.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_76.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmph6rykua8/peek_4_1_76.ltlf.dfa.rev.neg /tmp/tmph6rykua8/peek_4_1_76.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5ebpeziv/peek_4_1_77.ltlf.dfa.rev.neg /tmp/tmp5ebpeziv/peek_4_1_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_78.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp47v0ptsu/peek_4_1_78.ltlf.dfa.rev.neg /tmp/tmp47v0ptsu/peek_4_1_78.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_79.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2ts0sfrb/peek_4_1_79.ltlf.dfa.rev.neg /tmp/tmp2ts0sfrb/peek_4_1_79.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_79.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_8.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0nh_f9rs/peek_4_1_8.ltlf.dfa.rev.neg /tmp/tmp0nh_f9rs/peek_4_1_8.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_8.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmptcwo0xv5/peek_4_1_8.ltlf.dfa /tmp/tmptcwo0xv5/peek_4_1_8.part 0 partial dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 1033\nThe number of state variables: 1033\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_belief-states | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_80.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkagghe7o/peek_4_1_80.ltlf.dfa.rev.neg /tmp/tmpkagghe7o/peek_4_1_80.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_81.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnrnxagnk/peek_4_1_81.ltlf.dfa.rev.neg /tmp/tmpnrnxagnk/peek_4_1_81.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_82.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_s_34v4p/peek_4_1_82.ltlf.dfa.rev.neg /tmp/tmp_s_34v4p/peek_4_1_82.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_83.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmphqxg5_b0/peek_4_1_83.ltlf.dfa.rev.neg /tmp/tmphqxg5_b0/peek_4_1_83.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_84.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpzsh9pngl/peek_4_1_84.ltlf.dfa.rev.neg /tmp/tmpzsh9pngl/peek_4_1_84.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_85.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpaim6zqtl/peek_4_1_85.ltlf.dfa.rev.neg /tmp/tmpaim6zqtl/peek_4_1_85.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_86.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfrluw1tu/peek_4_1_86.ltlf.dfa.rev.neg /tmp/tmpfrluw1tu/peek_4_1_86.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_87.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz7c3wjul/peek_4_1_87.ltlf.dfa.rev.neg /tmp/tmpz7c3wjul/peek_4_1_87.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_88.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp40y3a0kb/peek_4_1_88.ltlf.dfa.rev.neg /tmp/tmp40y3a0kb/peek_4_1_88.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_88.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_89.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpr4616266/peek_4_1_89.ltlf.dfa.rev.neg /tmp/tmpr4616266/peek_4_1_89.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_89.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkxj3xjh9/peek_4_1_9.ltlf.dfa.rev.neg /tmp/tmpkxj3xjh9/peek_4_1_9.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_90.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpt325lonk/peek_4_1_90.ltlf.dfa.rev.neg /tmp/tmpt325lonk/peek_4_1_90.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_90.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_91.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmph1oa54_r/peek_4_1_91.ltlf.dfa.rev.neg /tmp/tmph1oa54_r/peek_4_1_91.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_92.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgi7ffe8c/peek_4_1_92.ltlf.dfa.rev.neg /tmp/tmpgi7ffe8c/peek_4_1_92.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_92.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpzjl8nqdh/peek_4_1_93.ltlf.dfa.rev.neg /tmp/tmpzjl8nqdh/peek_4_1_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_94.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmphz1jjr3_/peek_4_1_94.ltlf.dfa.rev.neg /tmp/tmphz1jjr3_/peek_4_1_94.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_95.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqksfjyxu/peek_4_1_95.ltlf.dfa.rev.neg /tmp/tmpqksfjyxu/peek_4_1_95.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_96.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpv3ehr0mg/peek_4_1_96.ltlf.dfa.rev.neg /tmp/tmpv3ehr0mg/peek_4_1_96.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_96.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_97.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqbo6tsfx/peek_4_1_97.ltlf.dfa.rev.neg /tmp/tmpqbo6tsfx/peek_4_1_97.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_97.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_99.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbj0dfa9g/peek_4_1_99.ltlf.dfa.rev.neg /tmp/tmpbj0dfa9g/peek_4_1_99.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_1_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_1.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdxwvct26/peek_4_2_1.ltlf.dfa.rev.neg /tmp/tmpdxwvct26/peek_4_2_1.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_1.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpk8jasjoi/peek_4_2_1.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpk8jasjoi/peek_4_2_1.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638830 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpk8jasjoi/peek_4_2_1.ltlf\n     638831                       | paste -sd'&'\n     638832 Killed                  | ltlsynt --part-file=/tmp/tmpk8jasjoi/peek_4_2_1.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_fl1ldxw/peek_4_2_10.ltlf.dfa.rev.neg /tmp/tmp_fl1ldxw/peek_4_2_10.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_10.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvb0y0fwz/peek_4_2_10.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvb0y0fwz/peek_4_2_10.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639496 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvb0y0fwz/peek_4_2_10.ltlf\n     639497                       | paste -sd'&'\n     639498 Killed                  | ltlsynt --part-file=/tmp/tmpvb0y0fwz/peek_4_2_10.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_100.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpef0nclfm/peek_4_2_100.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpef0nclfm/peek_4_2_100.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639029 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpef0nclfm/peek_4_2_100.ltlf\n     639030                       | paste -sd'&'\n     639031 Killed                  | ltlsynt --part-file=/tmp/tmpef0nclfm/peek_4_2_100.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_11.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcb8i6ozf/peek_4_2_11.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpcb8i6ozf/peek_4_2_11.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638018 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcb8i6ozf/peek_4_2_11.ltlf\n     638019                       | paste -sd'&'\n     638020 Killed                  | ltlsynt --part-file=/tmp/tmpcb8i6ozf/peek_4_2_11.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_12.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppjlunhtz/peek_4_2_12.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmppjlunhtz/peek_4_2_12.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671126 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppjlunhtz/peek_4_2_12.ltlf\n     671127                       | paste -sd'&'\n     671128 Killed                  | ltlsynt --part-file=/tmp/tmppjlunhtz/peek_4_2_12.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_13.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3yl9l8fs/peek_4_2_13.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp3yl9l8fs/peek_4_2_13.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670539 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3yl9l8fs/peek_4_2_13.ltlf\n     670540                       | paste -sd'&'\n     670541 Killed                  | ltlsynt --part-file=/tmp/tmp3yl9l8fs/peek_4_2_13.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_13.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_14.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxy1rjxbw/peek_4_2_14.ltlf.dfa.rev.neg /tmp/tmpxy1rjxbw/peek_4_2_14.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_14.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpchgc3ct1/peek_4_2_14.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpchgc3ct1/peek_4_2_14.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670390 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpchgc3ct1/peek_4_2_14.ltlf\n     670391                       | paste -sd'&'\n     670392 Killed                  | ltlsynt --part-file=/tmp/tmpchgc3ct1/peek_4_2_14.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_15.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpw79zu2yf/peek_4_2_15.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpw79zu2yf/peek_4_2_15.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670824 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpw79zu2yf/peek_4_2_15.ltlf\n     670825                       | paste -sd'&'\n     670826 Killed                  | ltlsynt --part-file=/tmp/tmpw79zu2yf/peek_4_2_15.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_16.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoo688_l3/peek_4_2_16.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpoo688_l3/peek_4_2_16.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671341 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoo688_l3/peek_4_2_16.ltlf\n     671342                       | paste -sd'&'\n     671343 Killed                  | ltlsynt --part-file=/tmp/tmpoo688_l3/peek_4_2_16.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_16.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_17.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9pgzottv/peek_4_2_17.ltlf.dfa.rev.neg /tmp/tmp9pgzottv/peek_4_2_17.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_17.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpz7z3gbq6/peek_4_2_17.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpz7z3gbq6/peek_4_2_17.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670945 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpz7z3gbq6/peek_4_2_17.ltlf\n     670946                       | paste -sd'&'\n     670947 Killed                  | ltlsynt --part-file=/tmp/tmpz7z3gbq6/peek_4_2_17.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_18.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpjhdyltzx/peek_4_2_18.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpjhdyltzx/peek_4_2_18.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671358 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpjhdyltzx/peek_4_2_18.ltlf\n     671359                       | paste -sd'&'\n     671360 Killed                  | ltlsynt --part-file=/tmp/tmpjhdyltzx/peek_4_2_18.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_19.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6wuexgv2/peek_4_2_19.ltlf.dfa.rev.neg /tmp/tmp6wuexgv2/peek_4_2_19.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_19.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvoiu018f/peek_4_2_19.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvoiu018f/peek_4_2_19.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670711 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvoiu018f/peek_4_2_19.ltlf\n     670712                       | paste -sd'&'\n     670713 Killed                  | ltlsynt --part-file=/tmp/tmpvoiu018f/peek_4_2_19.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_2.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmphrk9u55q/peek_4_2_2.ltlf.dfa.rev.neg /tmp/tmphrk9u55q/peek_4_2_2.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_2.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_2.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfb6twmm0/peek_4_2_2.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpfb6twmm0/peek_4_2_2.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671250 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfb6twmm0/peek_4_2_2.ltlf\n     671251                       | paste -sd'&'\n     671252 Killed                  | ltlsynt --part-file=/tmp/tmpfb6twmm0/peek_4_2_2.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_2.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_20.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwch2mcfs/peek_4_2_20.ltlf.dfa.rev.neg /tmp/tmpwch2mcfs/peek_4_2_20.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_20.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxhmxkulb/peek_4_2_20.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpxhmxkulb/peek_4_2_20.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638333 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxhmxkulb/peek_4_2_20.ltlf\n     638334                       | paste -sd'&'\n     638335 Killed                  | ltlsynt --part-file=/tmp/tmpxhmxkulb/peek_4_2_20.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_21.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7vujnxtd/peek_4_2_21.ltlf.dfa.rev.neg /tmp/tmp7vujnxtd/peek_4_2_21.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_21.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp2q3bp0gp/peek_4_2_21.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp2q3bp0gp/peek_4_2_21.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638328 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp2q3bp0gp/peek_4_2_21.ltlf\n     638329                       | paste -sd'&'\n     638330 Killed                  | ltlsynt --part-file=/tmp/tmp2q3bp0gp/peek_4_2_21.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_22.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5f54tz60/peek_4_2_22.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5f54tz60/peek_4_2_22.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638612 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5f54tz60/peek_4_2_22.ltlf\n     638613                       | paste -sd'&'\n     638614 Killed                  | ltlsynt --part-file=/tmp/tmp5f54tz60/peek_4_2_22.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_22.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_23.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmph5pjabhq/peek_4_2_23.ltlf.dfa.rev.neg /tmp/tmph5pjabhq/peek_4_2_23.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_23.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_23.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0_91msl9/peek_4_2_23.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp0_91msl9/peek_4_2_23.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638838 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0_91msl9/peek_4_2_23.ltlf\n     638839                       | paste -sd'&'\n     638840 Killed                  | ltlsynt --part-file=/tmp/tmp0_91msl9/peek_4_2_23.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_23.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_24.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdquz9j8o/peek_4_2_24.ltlf.dfa.rev.neg /tmp/tmpdquz9j8o/peek_4_2_24.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_24.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_24.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkqz04a5b/peek_4_2_24.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpkqz04a5b/peek_4_2_24.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639500 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkqz04a5b/peek_4_2_24.ltlf\n     639501                       | paste -sd'&'\n     639502 Killed                  | ltlsynt --part-file=/tmp/tmpkqz04a5b/peek_4_2_24.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_24.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_25.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_o1ua80m/peek_4_2_25.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_o1ua80m/peek_4_2_25.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639033 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_o1ua80m/peek_4_2_25.ltlf\n     639034                       | paste -sd'&'\n     639035 Killed                  | ltlsynt --part-file=/tmp/tmp_o1ua80m/peek_4_2_25.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_26.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkbibfbza/peek_4_2_26.ltlf.dfa.rev.neg /tmp/tmpkbibfbza/peek_4_2_26.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_26.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcq3vx67h/peek_4_2_26.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpcq3vx67h/peek_4_2_26.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638027 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcq3vx67h/peek_4_2_26.ltlf\n     638028                       | paste -sd'&'\n     638029 Killed                  | ltlsynt --part-file=/tmp/tmpcq3vx67h/peek_4_2_26.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_27.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgik1lzn8/peek_4_2_27.ltlf.dfa.rev.neg /tmp/tmpgik1lzn8/peek_4_2_27.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_27.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_27.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7v_i4ai5/peek_4_2_27.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7v_i4ai5/peek_4_2_27.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671134 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7v_i4ai5/peek_4_2_27.ltlf\n     671135                       | paste -sd'&'\n     671136 Killed                  | ltlsynt --part-file=/tmp/tmp7v_i4ai5/peek_4_2_27.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_27.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_28.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1kpmo5gc/peek_4_2_28.ltlf.dfa.rev.neg /tmp/tmp1kpmo5gc/peek_4_2_28.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_28.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmhh01rqq/peek_4_2_28.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpmhh01rqq/peek_4_2_28.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670547 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmhh01rqq/peek_4_2_28.ltlf\n     670548                       | paste -sd'&'\n     670549 Killed                  | ltlsynt --part-file=/tmp/tmpmhh01rqq/peek_4_2_28.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_29.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp1qls5atm/peek_4_2_29.ltlf.dfa.rev.neg /tmp/tmp1qls5atm/peek_4_2_29.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_29.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_29.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpda3kvib5/peek_4_2_29.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpda3kvib5/peek_4_2_29.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670394 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpda3kvib5/peek_4_2_29.ltlf\n     670395                       | paste -sd'&'\n     670396 Killed                  | ltlsynt --part-file=/tmp/tmpda3kvib5/peek_4_2_29.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_29.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_3.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnpacxddt/peek_4_2_3.ltlf.dfa.rev.neg /tmp/tmpnpacxddt/peek_4_2_3.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_3.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_3.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6662bbwu/peek_4_2_3.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp6662bbwu/peek_4_2_3.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670830 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6662bbwu/peek_4_2_3.ltlf\n     670831                       | paste -sd'&'\n     670832 Killed                  | ltlsynt --part-file=/tmp/tmp6662bbwu/peek_4_2_3.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_3.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_30.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsrwlqhx0/peek_4_2_30.ltlf.dfa.rev.neg /tmp/tmpsrwlqhx0/peek_4_2_30.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_30.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp67fu42fs/peek_4_2_30.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp67fu42fs/peek_4_2_30.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671346 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp67fu42fs/peek_4_2_30.ltlf\n     671347                       | paste -sd'&'\n     671348 Killed                  | ltlsynt --part-file=/tmp/tmp67fu42fs/peek_4_2_30.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_31.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9jb99on9/peek_4_2_31.ltlf.dfa.rev.neg /tmp/tmp9jb99on9/peek_4_2_31.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_31.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_31.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpaok4560s/peek_4_2_31.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpaok4560s/peek_4_2_31.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670953 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpaok4560s/peek_4_2_31.ltlf\n     670954                       | paste -sd'&'\n     670955 Killed                  | ltlsynt --part-file=/tmp/tmpaok4560s/peek_4_2_31.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_31.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_32.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpu9lkvve5/peek_4_2_32.ltlf.dfa.rev.neg /tmp/tmpu9lkvve5/peek_4_2_32.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_32.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp96a1mtlc/peek_4_2_32.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp96a1mtlc/peek_4_2_32.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671366 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp96a1mtlc/peek_4_2_32.ltlf\n     671367                       | paste -sd'&'\n     671368 Killed                  | ltlsynt --part-file=/tmp/tmp96a1mtlc/peek_4_2_32.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_33.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5em_lpm3/peek_4_2_33.ltlf.dfa.rev.neg /tmp/tmp5em_lpm3/peek_4_2_33.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_33.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_33.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpeeachhha/peek_4_2_33.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpeeachhha/peek_4_2_33.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670715 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpeeachhha/peek_4_2_33.ltlf\n     670716                       | paste -sd'&'\n     670717 Killed                  | ltlsynt --part-file=/tmp/tmpeeachhha/peek_4_2_33.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_33.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_34.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpieh1rrbw/peek_4_2_34.ltlf.dfa.rev.neg /tmp/tmpieh1rrbw/peek_4_2_34.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_34.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0b82kezg/peek_4_2_34.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp0b82kezg/peek_4_2_34.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671254 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0b82kezg/peek_4_2_34.ltlf\n     671255                       | paste -sd'&'\n     671256 Killed                  | ltlsynt --part-file=/tmp/tmp0b82kezg/peek_4_2_34.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_35.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpp4hkb787/peek_4_2_35.ltlf.dfa.rev.neg /tmp/tmpp4hkb787/peek_4_2_35.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_35.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_35.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp08vorm9r/peek_4_2_35.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp08vorm9r/peek_4_2_35.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638350 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp08vorm9r/peek_4_2_35.ltlf\n     638351                       | paste -sd'&'\n     638352 Killed                  | ltlsynt --part-file=/tmp/tmp08vorm9r/peek_4_2_35.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_35.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_36.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6gk_0bqn/peek_4_2_36.ltlf.dfa.rev.neg /tmp/tmp6gk_0bqn/peek_4_2_36.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_36.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_36.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp980waoho/peek_4_2_36.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp980waoho/peek_4_2_36.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638337 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp980waoho/peek_4_2_36.ltlf\n     638338                       | paste -sd'&'\n     638339 Killed                  | ltlsynt --part-file=/tmp/tmp980waoho/peek_4_2_36.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_36.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_37.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpi_5sozml/peek_4_2_37.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpi_5sozml/peek_4_2_37.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638616 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpi_5sozml/peek_4_2_37.ltlf\n     638617                       | paste -sd'&'\n     638618 Killed                  | ltlsynt --part-file=/tmp/tmpi_5sozml/peek_4_2_37.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_38.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplqwqg_k4/peek_4_2_38.ltlf.dfa.rev.neg /tmp/tmplqwqg_k4/peek_4_2_38.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_38.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5xg6ld06/peek_4_2_38.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5xg6ld06/peek_4_2_38.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638842 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5xg6ld06/peek_4_2_38.ltlf\n     638843                       | paste -sd'&'\n     638844 Killed                  | ltlsynt --part-file=/tmp/tmp5xg6ld06/peek_4_2_38.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_39.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpn0w48cug/peek_4_2_39.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpn0w48cug/peek_4_2_39.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639504 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpn0w48cug/peek_4_2_39.ltlf\n     639505                       | paste -sd'&'\n     639506 Killed                  | ltlsynt --part-file=/tmp/tmpn0w48cug/peek_4_2_39.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_39.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_4.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpk11jclt1/peek_4_2_4.ltlf.dfa.rev.neg /tmp/tmpk11jclt1/peek_4_2_4.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_4.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5i1oh3jl/peek_4_2_4.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5i1oh3jl/peek_4_2_4.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639037 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5i1oh3jl/peek_4_2_4.ltlf\n     639038                       | paste -sd'&'\n     639039 Killed                  | ltlsynt --part-file=/tmp/tmp5i1oh3jl/peek_4_2_4.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_40.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4iw1m8bb/peek_4_2_40.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4iw1m8bb/peek_4_2_40.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638034 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4iw1m8bb/peek_4_2_40.ltlf\n     638035                       | paste -sd'&'\n     638036 Killed                  | ltlsynt --part-file=/tmp/tmp4iw1m8bb/peek_4_2_40.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_40.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_41.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpk_u25ulg/peek_4_2_41.ltlf.dfa.rev.neg /tmp/tmpk_u25ulg/peek_4_2_41.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_41.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpu2c_02gt/peek_4_2_41.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpu2c_02gt/peek_4_2_41.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671138 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpu2c_02gt/peek_4_2_41.ltlf\n     671139                       | paste -sd'&'\n     671140 Killed                  | ltlsynt --part-file=/tmp/tmpu2c_02gt/peek_4_2_41.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_42.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpx8l9z08_/peek_4_2_42.ltlf.dfa.rev.neg /tmp/tmpx8l9z08_/peek_4_2_42.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_42.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_42.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6g2_3g6v/peek_4_2_42.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp6g2_3g6v/peek_4_2_42.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670555 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6g2_3g6v/peek_4_2_42.ltlf\n     670556                       | paste -sd'&'\n     670557 Killed                  | ltlsynt --part-file=/tmp/tmp6g2_3g6v/peek_4_2_42.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_42.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_43.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpo361iikh/peek_4_2_43.ltlf.dfa.rev.neg /tmp/tmpo361iikh/peek_4_2_43.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_43.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_u_jaqd4/peek_4_2_43.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_u_jaqd4/peek_4_2_43.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670398 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_u_jaqd4/peek_4_2_43.ltlf\n     670399                       | paste -sd'&'\n     670400 Killed                  | ltlsynt --part-file=/tmp/tmp_u_jaqd4/peek_4_2_43.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_44.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpk98fs9xd/peek_4_2_44.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpk98fs9xd/peek_4_2_44.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670834 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpk98fs9xd/peek_4_2_44.ltlf\n     670835                       | paste -sd'&'\n     670836 Killed                  | ltlsynt --part-file=/tmp/tmpk98fs9xd/peek_4_2_44.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_45.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp14qd9x5n/peek_4_2_45.ltlf.dfa.rev.neg /tmp/tmp14qd9x5n/peek_4_2_45.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_45.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpjx84cn5l/peek_4_2_45.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpjx84cn5l/peek_4_2_45.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671350 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpjx84cn5l/peek_4_2_45.ltlf\n     671351                       | paste -sd'&'\n     671352 Killed                  | ltlsynt --part-file=/tmp/tmpjx84cn5l/peek_4_2_45.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_46.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpyxy4vb6b/peek_4_2_46.ltlf.dfa.rev.neg /tmp/tmpyxy4vb6b/peek_4_2_46.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_46.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgsckd09o/peek_4_2_46.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpgsckd09o/peek_4_2_46.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670961 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgsckd09o/peek_4_2_46.ltlf\n     670962                       | paste -sd'&'\n     670963 Killed                  | ltlsynt --part-file=/tmp/tmpgsckd09o/peek_4_2_46.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_47.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp__wro_gg/peek_4_2_47.ltlf.dfa.rev.neg /tmp/tmp__wro_gg/peek_4_2_47.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_47.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmphfqy1hql/peek_4_2_47.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmphfqy1hql/peek_4_2_47.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671377 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmphfqy1hql/peek_4_2_47.ltlf\n     671378                       | paste -sd'&'\n     671379 Killed                  | ltlsynt --part-file=/tmp/tmphfqy1hql/peek_4_2_47.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_48.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_28e72by/peek_4_2_48.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_28e72by/peek_4_2_48.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670726 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_28e72by/peek_4_2_48.ltlf\n     670727                       | paste -sd'&'\n     670728 Killed                  | ltlsynt --part-file=/tmp/tmp_28e72by/peek_4_2_48.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_49.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjmg2aa4x/peek_4_2_49.ltlf.dfa.rev.neg /tmp/tmpjmg2aa4x/peek_4_2_49.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_49.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp493hab84/peek_4_2_49.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp493hab84/peek_4_2_49.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671258 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp493hab84/peek_4_2_49.ltlf\n     671259                       | paste -sd'&'\n     671260 Killed                  | ltlsynt --part-file=/tmp/tmp493hab84/peek_4_2_49.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_5.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8orjy46n/peek_4_2_5.ltlf.dfa.rev.neg /tmp/tmp8orjy46n/peek_4_2_5.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_5.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp783r2_ap/peek_4_2_5.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp783r2_ap/peek_4_2_5.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638366 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp783r2_ap/peek_4_2_5.ltlf\n     638367                       | paste -sd'&'\n     638368 Killed                  | ltlsynt --part-file=/tmp/tmp783r2_ap/peek_4_2_5.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8dtmer0d/peek_4_2_50.ltlf.dfa.rev.neg /tmp/tmp8dtmer0d/peek_4_2_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_50.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4qw7v6n9/peek_4_2_50.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4qw7v6n9/peek_4_2_50.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638346 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4qw7v6n9/peek_4_2_50.ltlf\n     638347                       | paste -sd'&'\n     638348 Killed                  | ltlsynt --part-file=/tmp/tmp4qw7v6n9/peek_4_2_50.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_51.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprrrodzvo/peek_4_2_51.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmprrrodzvo/peek_4_2_51.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638620 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprrrodzvo/peek_4_2_51.ltlf\n     638621                       | paste -sd'&'\n     638622 Killed                  | ltlsynt --part-file=/tmp/tmprrrodzvo/peek_4_2_51.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_52.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0_kuyr_m/peek_4_2_52.ltlf.dfa.rev.neg /tmp/tmp0_kuyr_m/peek_4_2_52.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_52.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoivdtu3a/peek_4_2_52.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpoivdtu3a/peek_4_2_52.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638846 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoivdtu3a/peek_4_2_52.ltlf\n     638847                       | paste -sd'&'\n     638848 Killed                  | ltlsynt --part-file=/tmp/tmpoivdtu3a/peek_4_2_52.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_53.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmprqgjxa36/peek_4_2_53.ltlf.dfa.rev.neg /tmp/tmprqgjxa36/peek_4_2_53.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_53.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp2bgj82cl/peek_4_2_53.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp2bgj82cl/peek_4_2_53.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639508 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp2bgj82cl/peek_4_2_53.ltlf\n     639509                       | paste -sd'&'\n     639510 Killed                  | ltlsynt --part-file=/tmp/tmp2bgj82cl/peek_4_2_53.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_54.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpa9yxzh_0/peek_4_2_54.ltlf.dfa.rev.neg /tmp/tmpa9yxzh_0/peek_4_2_54.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_54.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx9672k2n/peek_4_2_54.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpx9672k2n/peek_4_2_54.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639049 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx9672k2n/peek_4_2_54.ltlf\n     639050                       | paste -sd'&'\n     639051 Killed                  | ltlsynt --part-file=/tmp/tmpx9672k2n/peek_4_2_54.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_55.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpuw99l5so/peek_4_2_55.ltlf.dfa.rev.neg /tmp/tmpuw99l5so/peek_4_2_55.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_55.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqqfe96de/peek_4_2_55.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpqqfe96de/peek_4_2_55.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638042 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqqfe96de/peek_4_2_55.ltlf\n     638043                       | paste -sd'&'\n     638044 Killed                  | ltlsynt --part-file=/tmp/tmpqqfe96de/peek_4_2_55.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_56.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpq53sizdd/peek_4_2_56.ltlf.dfa.rev.neg /tmp/tmpq53sizdd/peek_4_2_56.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_56.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo_ggga_z/peek_4_2_56.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpo_ggga_z/peek_4_2_56.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671142 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo_ggga_z/peek_4_2_56.ltlf\n     671143                       | paste -sd'&'\n     671144 Killed                  | ltlsynt --part-file=/tmp/tmpo_ggga_z/peek_4_2_56.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_57.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpr771feo9/peek_4_2_57.ltlf.dfa.rev.neg /tmp/tmpr771feo9/peek_4_2_57.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_57.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp97av97uc/peek_4_2_57.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp97av97uc/peek_4_2_57.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670559 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp97av97uc/peek_4_2_57.ltlf\n     670560                       | paste -sd'&'\n     670561 Killed                  | ltlsynt --part-file=/tmp/tmp97av97uc/peek_4_2_57.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_58.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6px6g0ea/peek_4_2_58.ltlf.dfa.rev.neg /tmp/tmp6px6g0ea/peek_4_2_58.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_58.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpldqlyd88/peek_4_2_58.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpldqlyd88/peek_4_2_58.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670405 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpldqlyd88/peek_4_2_58.ltlf\n     670406                       | paste -sd'&'\n     670407 Killed                  | ltlsynt --part-file=/tmp/tmpldqlyd88/peek_4_2_58.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_59.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwy80y3w4/peek_4_2_59.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpwy80y3w4/peek_4_2_59.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670842 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwy80y3w4/peek_4_2_59.ltlf\n     670843                       | paste -sd'&'\n     670844 Killed                  | ltlsynt --part-file=/tmp/tmpwy80y3w4/peek_4_2_59.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_6.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0lsn34me/peek_4_2_6.ltlf.dfa.rev.neg /tmp/tmp0lsn34me/peek_4_2_6.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_6.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppl7_u9ql/peek_4_2_6.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmppl7_u9ql/peek_4_2_6.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671354 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppl7_u9ql/peek_4_2_6.ltlf\n     671355                       | paste -sd'&'\n     671356 Killed                  | ltlsynt --part-file=/tmp/tmppl7_u9ql/peek_4_2_6.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_60.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf6s81pmd/peek_4_2_60.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpf6s81pmd/peek_4_2_60.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670969 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf6s81pmd/peek_4_2_60.ltlf\n     670970                       | paste -sd'&'\n     670971 Killed                  | ltlsynt --part-file=/tmp/tmpf6s81pmd/peek_4_2_60.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_60.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_61.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpupohc2i4/peek_4_2_61.ltlf.dfa.rev.neg /tmp/tmpupohc2i4/peek_4_2_61.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_61.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_61.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpl_lgg8hq/peek_4_2_61.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpl_lgg8hq/peek_4_2_61.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671388 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpl_lgg8hq/peek_4_2_61.ltlf\n     671389                       | paste -sd'&'\n     671390 Killed                  | ltlsynt --part-file=/tmp/tmpl_lgg8hq/peek_4_2_61.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_61.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_62.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpevznmkui/peek_4_2_62.ltlf.dfa.rev.neg /tmp/tmpevznmkui/peek_4_2_62.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_62.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpv40h_yp1/peek_4_2_62.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpv40h_yp1/peek_4_2_62.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670730 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpv40h_yp1/peek_4_2_62.ltlf\n     670731                       | paste -sd'&'\n     670732 Killed                  | ltlsynt --part-file=/tmp/tmpv40h_yp1/peek_4_2_62.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_63.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbpphivio/peek_4_2_63.ltlf.dfa.rev.neg /tmp/tmpbpphivio/peek_4_2_63.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_63.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6rqvw75_/peek_4_2_63.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp6rqvw75_/peek_4_2_63.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671262 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6rqvw75_/peek_4_2_63.ltlf\n     671263                       | paste -sd'&'\n     671264 Killed                  | ltlsynt --part-file=/tmp/tmp6rqvw75_/peek_4_2_63.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_64.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpen0g_kaq/peek_4_2_64.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpen0g_kaq/peek_4_2_64.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638397 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpen0g_kaq/peek_4_2_64.ltlf\n     638398                       | paste -sd'&'\n     638399 Killed                  | ltlsynt --part-file=/tmp/tmpen0g_kaq/peek_4_2_64.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_64.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_65.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpvxuznt5k/peek_4_2_65.ltlf.dfa.rev.neg /tmp/tmpvxuznt5k/peek_4_2_65.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_65.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpp59e5o0g/peek_4_2_65.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpp59e5o0g/peek_4_2_65.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638357 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpp59e5o0g/peek_4_2_65.ltlf\n     638358                       | paste -sd'&'\n     638359 Killed                  | ltlsynt --part-file=/tmp/tmpp59e5o0g/peek_4_2_65.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp62dccyjw/peek_4_2_66.ltlf.dfa.rev.neg /tmp/tmp62dccyjw/peek_4_2_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_66.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpna80gnct/peek_4_2_66.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpna80gnct/peek_4_2_66.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638624 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpna80gnct/peek_4_2_66.ltlf\n     638625                       | paste -sd'&'\n     638626 Killed                  | ltlsynt --part-file=/tmp/tmpna80gnct/peek_4_2_66.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_67.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0b6lzm63/peek_4_2_67.ltlf.dfa.rev.neg /tmp/tmp0b6lzm63/peek_4_2_67.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_67.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_67.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_q0teybj/peek_4_2_67.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_q0teybj/peek_4_2_67.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638853 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_q0teybj/peek_4_2_67.ltlf\n     638854                       | paste -sd'&'\n     638855 Killed                  | ltlsynt --part-file=/tmp/tmp_q0teybj/peek_4_2_67.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_67.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_68.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4vnpdzi4/peek_4_2_68.ltlf.dfa.rev.neg /tmp/tmp4vnpdzi4/peek_4_2_68.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_68.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgvmtdu_r/peek_4_2_68.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpgvmtdu_r/peek_4_2_68.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639512 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgvmtdu_r/peek_4_2_68.ltlf\n     639513                       | paste -sd'&'\n     639514 Killed                  | ltlsynt --part-file=/tmp/tmpgvmtdu_r/peek_4_2_68.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_69.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpz0snet98/peek_4_2_69.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpz0snet98/peek_4_2_69.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639053 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpz0snet98/peek_4_2_69.ltlf\n     639054                       | paste -sd'&'\n     639055 Killed                  | ltlsynt --part-file=/tmp/tmpz0snet98/peek_4_2_69.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_69.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_7.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdueq26iw/peek_4_2_7.ltlf.dfa.rev.neg /tmp/tmpdueq26iw/peek_4_2_7.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_7.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp86bcpux4/peek_4_2_7.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp86bcpux4/peek_4_2_7.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638046 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp86bcpux4/peek_4_2_7.ltlf\n     638047                       | paste -sd'&'\n     638048 Killed                  | ltlsynt --part-file=/tmp/tmp86bcpux4/peek_4_2_7.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_70.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjxt6r8wh/peek_4_2_70.ltlf.dfa.rev.neg /tmp/tmpjxt6r8wh/peek_4_2_70.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_70.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpc35n1f7r/peek_4_2_70.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpc35n1f7r/peek_4_2_70.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671146 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpc35n1f7r/peek_4_2_70.ltlf\n     671147                       | paste -sd'&'\n     671148 Killed                  | ltlsynt --part-file=/tmp/tmpc35n1f7r/peek_4_2_70.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_71.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqvw8p1dh/peek_4_2_71.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpqvw8p1dh/peek_4_2_71.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670564 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqvw8p1dh/peek_4_2_71.ltlf\n     670565                       | paste -sd'&'\n     670566 Killed                  | ltlsynt --part-file=/tmp/tmpqvw8p1dh/peek_4_2_71.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_71.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_72.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnwbfinpr/peek_4_2_72.ltlf.dfa.rev.neg /tmp/tmpnwbfinpr/peek_4_2_72.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_72.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpdswmj5_s/peek_4_2_72.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpdswmj5_s/peek_4_2_72.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670412 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpdswmj5_s/peek_4_2_72.ltlf\n     670413                       | paste -sd'&'\n     670414 Killed                  | ltlsynt --part-file=/tmp/tmpdswmj5_s/peek_4_2_72.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_74.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxtwe0am1/peek_4_2_74.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpxtwe0am1/peek_4_2_74.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671362 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxtwe0am1/peek_4_2_74.ltlf\n     671363                       | paste -sd'&'\n     671364 Killed                  | ltlsynt --part-file=/tmp/tmpxtwe0am1/peek_4_2_74.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_75.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpd8nsxwxz/peek_4_2_75.ltlf.dfa.rev.neg /tmp/tmpd8nsxwxz/peek_4_2_75.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_75.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpujk7mpgz/peek_4_2_75.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpujk7mpgz/peek_4_2_75.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670977 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpujk7mpgz/peek_4_2_75.ltlf\n     670978                       | paste -sd'&'\n     670979 Killed                  | ltlsynt --part-file=/tmp/tmpujk7mpgz/peek_4_2_75.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_76.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwpjwow46/peek_4_2_76.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpwpjwow46/peek_4_2_76.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671396 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwpjwow46/peek_4_2_76.ltlf\n     671397                       | paste -sd'&'\n     671398 Killed                  | ltlsynt --part-file=/tmp/tmpwpjwow46/peek_4_2_76.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_77.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9699h939/peek_4_2_77.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp9699h939/peek_4_2_77.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670738 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9699h939/peek_4_2_77.ltlf\n     670739                       | paste -sd'&'\n     670740 Killed                  | ltlsynt --part-file=/tmp/tmp9699h939/peek_4_2_77.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_78.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3oqixkdb/peek_4_2_78.ltlf.dfa.rev.neg /tmp/tmp3oqixkdb/peek_4_2_78.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_78.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgjk7_eg5/peek_4_2_78.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpgjk7_eg5/peek_4_2_78.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671269 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgjk7_eg5/peek_4_2_78.ltlf\n     671270                       | paste -sd'&'\n     671271 Killed                  | ltlsynt --part-file=/tmp/tmpgjk7_eg5/peek_4_2_78.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_79.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp72aywegy/peek_4_2_79.ltlf.dfa.rev.neg /tmp/tmp72aywegy/peek_4_2_79.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_79.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_79.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgh28ja_m/peek_4_2_79.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpgh28ja_m/peek_4_2_79.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638411 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgh28ja_m/peek_4_2_79.ltlf\n     638412                       | paste -sd'&'\n     638413 Killed                  | ltlsynt --part-file=/tmp/tmpgh28ja_m/peek_4_2_79.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_79.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_8.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbikehjwa/peek_4_2_8.ltlf.dfa.rev.neg /tmp/tmpbikehjwa/peek_4_2_8.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_8.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx1xb7ihg/peek_4_2_8.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpx1xb7ihg/peek_4_2_8.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638393 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx1xb7ihg/peek_4_2_8.ltlf\n     638394                       | paste -sd'&'\n     638395 Killed                  | ltlsynt --part-file=/tmp/tmpx1xb7ihg/peek_4_2_8.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_80.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzess0lvc/peek_4_2_80.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpzess0lvc/peek_4_2_80.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638636 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzess0lvc/peek_4_2_80.ltlf\n     638637                       | paste -sd'&'\n     638638 Killed                  | ltlsynt --part-file=/tmp/tmpzess0lvc/peek_4_2_80.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_81.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppomepd2h/peek_4_2_81.ltlf.dfa.rev.neg /tmp/tmppomepd2h/peek_4_2_81.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_81.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpojg1f4q9/peek_4_2_81.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpojg1f4q9/peek_4_2_81.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638862 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpojg1f4q9/peek_4_2_81.ltlf\n     638863                       | paste -sd'&'\n     638864 Killed                  | ltlsynt --part-file=/tmp/tmpojg1f4q9/peek_4_2_81.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_82.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6gnvmy6d/peek_4_2_82.ltlf.dfa.rev.neg /tmp/tmp6gnvmy6d/peek_4_2_82.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_82.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5kyst5_0/peek_4_2_82.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5kyst5_0/peek_4_2_82.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639528 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5kyst5_0/peek_4_2_82.ltlf\n     639529                       | paste -sd'&'\n     639530 Killed                  | ltlsynt --part-file=/tmp/tmp5kyst5_0/peek_4_2_82.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_83.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz7o28rn4/peek_4_2_83.ltlf.dfa.rev.neg /tmp/tmpz7o28rn4/peek_4_2_83.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_83.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpevv1a44q/peek_4_2_83.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpevv1a44q/peek_4_2_83.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639057 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpevv1a44q/peek_4_2_83.ltlf\n     639058                       | paste -sd'&'\n     639059 Killed                  | ltlsynt --part-file=/tmp/tmpevv1a44q/peek_4_2_83.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_84.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5srd9bpc/peek_4_2_84.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5srd9bpc/peek_4_2_84.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638050 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5srd9bpc/peek_4_2_84.ltlf\n     638051                       | paste -sd'&'\n     638052 Killed                  | ltlsynt --part-file=/tmp/tmp5srd9bpc/peek_4_2_84.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_85.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnda9mjkt/peek_4_2_85.ltlf.dfa.rev.neg /tmp/tmpnda9mjkt/peek_4_2_85.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_85.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp64r3mw79/peek_4_2_85.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp64r3mw79/peek_4_2_85.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671150 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp64r3mw79/peek_4_2_85.ltlf\n     671151                       | paste -sd'&'\n     671152 Killed                  | ltlsynt --part-file=/tmp/tmp64r3mw79/peek_4_2_85.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_86.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpc3mqtwno/peek_4_2_86.ltlf.dfa.rev.neg /tmp/tmpc3mqtwno/peek_4_2_86.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_86.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp52qz150r/peek_4_2_86.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp52qz150r/peek_4_2_86.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670572 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp52qz150r/peek_4_2_86.ltlf\n     670573                       | paste -sd'&'\n     670574 Killed                  | ltlsynt --part-file=/tmp/tmp52qz150r/peek_4_2_86.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_87.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpupsfl_1r/peek_4_2_87.ltlf.dfa.rev.neg /tmp/tmpupsfl_1r/peek_4_2_87.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_87.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpnagocdt8/peek_4_2_87.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpnagocdt8/peek_4_2_87.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670416 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpnagocdt8/peek_4_2_87.ltlf\n     670417                       | paste -sd'&'\n     670418 Killed                  | ltlsynt --part-file=/tmp/tmpnagocdt8/peek_4_2_87.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_88.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5smavcw2/peek_4_2_88.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5smavcw2/peek_4_2_88.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670895 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5smavcw2/peek_4_2_88.ltlf\n     670896                       | paste -sd'&'\n     670897 Killed                  | ltlsynt --part-file=/tmp/tmp5smavcw2/peek_4_2_88.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_88.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_89.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmprj1bffp6/peek_4_2_89.ltlf.dfa.rev.neg /tmp/tmprj1bffp6/peek_4_2_89.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_89.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_89.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp10tm7ra7/peek_4_2_89.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp10tm7ra7/peek_4_2_89.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671370 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp10tm7ra7/peek_4_2_89.ltlf\n     671371                       | paste -sd'&'\n     671372 Killed                  | ltlsynt --part-file=/tmp/tmp10tm7ra7/peek_4_2_89.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_89.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_9.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpivaiezef/peek_4_2_9.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpivaiezef/peek_4_2_9.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670994 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpivaiezef/peek_4_2_9.ltlf\n     670995                       | paste -sd'&'\n     670996 Killed                  | ltlsynt --part-file=/tmp/tmpivaiezef/peek_4_2_9.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_90.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6rtcaucr/peek_4_2_90.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp6rtcaucr/peek_4_2_90.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671404 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6rtcaucr/peek_4_2_90.ltlf\n     671405                       | paste -sd'&'\n     671406 Killed                  | ltlsynt --part-file=/tmp/tmp6rtcaucr/peek_4_2_90.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_90.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_91.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpb6hmdk50/peek_4_2_91.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpb6hmdk50/peek_4_2_91.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670742 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpb6hmdk50/peek_4_2_91.ltlf\n     670743                       | paste -sd'&'\n     670744 Killed                  | ltlsynt --part-file=/tmp/tmpb6hmdk50/peek_4_2_91.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_92.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplmbevvkd/peek_4_2_92.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmplmbevvkd/peek_4_2_92.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671276 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplmbevvkd/peek_4_2_92.ltlf\n     671277                       | paste -sd'&'\n     671278 Killed                  | ltlsynt --part-file=/tmp/tmplmbevvkd/peek_4_2_92.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_92.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpv2ul8d9y/peek_4_2_93.ltlf.dfa.rev.neg /tmp/tmpv2ul8d9y/peek_4_2_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_93.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpeu0325wx/peek_4_2_93.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpeu0325wx/peek_4_2_93.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638429 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpeu0325wx/peek_4_2_93.ltlf\n     638430                       | paste -sd'&'\n     638431 Killed                  | ltlsynt --part-file=/tmp/tmpeu0325wx/peek_4_2_93.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_94.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp50pahylr/peek_4_2_94.ltlf.dfa.rev.neg /tmp/tmp50pahylr/peek_4_2_94.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_94.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqc7v8xp5/peek_4_2_94.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpqc7v8xp5/peek_4_2_94.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638415 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqc7v8xp5/peek_4_2_94.ltlf\n     638416                       | paste -sd'&'\n     638417 Killed                  | ltlsynt --part-file=/tmp/tmpqc7v8xp5/peek_4_2_94.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_95.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpy4lgckx5/peek_4_2_95.ltlf.dfa.rev.neg /tmp/tmpy4lgckx5/peek_4_2_95.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_95.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxo8fzopz/peek_4_2_95.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpxo8fzopz/peek_4_2_95.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638640 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxo8fzopz/peek_4_2_95.ltlf\n     638641                       | paste -sd'&'\n     638642 Killed                  | ltlsynt --part-file=/tmp/tmpxo8fzopz/peek_4_2_95.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_96.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpv56v4at6/peek_4_2_96.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpv56v4at6/peek_4_2_96.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638874 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpv56v4at6/peek_4_2_96.ltlf\n     638875                       | paste -sd'&'\n     638876 Killed                  | ltlsynt --part-file=/tmp/tmpv56v4at6/peek_4_2_96.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_96.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_97.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpseyatsjm/peek_4_2_97.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpseyatsjm/peek_4_2_97.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639537 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpseyatsjm/peek_4_2_97.ltlf\n     639538                       | paste -sd'&'\n     639539 Killed                  | ltlsynt --part-file=/tmp/tmpseyatsjm/peek_4_2_97.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_97.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_98.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgxjdvsj3/peek_4_2_98.ltlf.dfa.rev.neg /tmp/tmpgxjdvsj3/peek_4_2_98.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_98.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_98.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxytn30wp/peek_4_2_98.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpxytn30wp/peek_4_2_98.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639061 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxytn30wp/peek_4_2_98.ltlf\n     639062                       | paste -sd'&'\n     639063 Killed                  | ltlsynt --part-file=/tmp/tmpxytn30wp/peek_4_2_98.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_98.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_99.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpso2ztyrm/peek_4_2_99.ltlf.dfa.rev.neg /tmp/tmpso2ztyrm/peek_4_2_99.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_99.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplfdzl2ny/peek_4_2_99.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmplfdzl2ny/peek_4_2_99.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638058 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplfdzl2ny/peek_4_2_99.ltlf\n     638059                       | paste -sd'&'\n     638060 Killed                  | ltlsynt --part-file=/tmp/tmplfdzl2ny/peek_4_2_99.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_2_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_1.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmph_sjj9ha/peek_4_3_1.ltlf.dfa.rev.neg /tmp/tmph_sjj9ha/peek_4_3_1.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_1.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6eittg76/peek_4_3_1.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp6eittg76/peek_4_3_1.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671154 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6eittg76/peek_4_3_1.ltlf\n     671155                       | paste -sd'&'\n     671156 Killed                  | ltlsynt --part-file=/tmp/tmp6eittg76/peek_4_3_1.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpw7ffzaht/peek_4_3_10.ltlf.dfa.rev.neg /tmp/tmpw7ffzaht/peek_4_3_10.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_10.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpztpowzy3/peek_4_3_10.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpztpowzy3/peek_4_3_10.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670576 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpztpowzy3/peek_4_3_10.ltlf\n     670577                       | paste -sd'&'\n     670578 Killed                  | ltlsynt --part-file=/tmp/tmpztpowzy3/peek_4_3_10.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_100.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbzgjg5me/peek_4_3_100.ltlf.dfa.rev.neg /tmp/tmpbzgjg5me/peek_4_3_100.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_100.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr4hu26vr/peek_4_3_100.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpr4hu26vr/peek_4_3_100.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670424 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr4hu26vr/peek_4_3_100.ltlf\n     670425                       | paste -sd'&'\n     670426 Killed                  | ltlsynt --part-file=/tmp/tmpr4hu26vr/peek_4_3_100.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_11.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsffbt6zc/peek_4_3_11.ltlf.dfa.rev.neg /tmp/tmpsffbt6zc/peek_4_3_11.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_11.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgt4oqk6v/peek_4_3_11.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpgt4oqk6v/peek_4_3_11.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670899 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgt4oqk6v/peek_4_3_11.ltlf\n     670900                       | paste -sd'&'\n     670901 Killed                  | ltlsynt --part-file=/tmp/tmpgt4oqk6v/peek_4_3_11.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_12.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5nswlihj/peek_4_3_12.ltlf.dfa.rev.neg /tmp/tmp5nswlihj/peek_4_3_12.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_12.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpsux_zkau/peek_4_3_12.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpsux_zkau/peek_4_3_12.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671384 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpsux_zkau/peek_4_3_12.ltlf\n     671385                       | paste -sd'&'\n     671386 Killed                  | ltlsynt --part-file=/tmp/tmpsux_zkau/peek_4_3_12.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_13.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvphqnpu2/peek_4_3_13.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvphqnpu2/peek_4_3_13.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671002 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvphqnpu2/peek_4_3_13.ltlf\n     671003                       | paste -sd'&'\n     671004 Killed                  | ltlsynt --part-file=/tmp/tmpvphqnpu2/peek_4_3_13.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_13.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_14.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpijq_7nvf/peek_4_3_14.ltlf.dfa.rev.neg /tmp/tmpijq_7nvf/peek_4_3_14.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_14.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmph_h968th/peek_4_3_14.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmph_h968th/peek_4_3_14.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671412 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmph_h968th/peek_4_3_14.ltlf\n     671413                       | paste -sd'&'\n     671414 Killed                  | ltlsynt --part-file=/tmp/tmph_h968th/peek_4_3_14.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_15.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpaf4ui7j9/peek_4_3_15.ltlf.dfa.rev.neg /tmp/tmpaf4ui7j9/peek_4_3_15.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_15.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfe1ugh04/peek_4_3_15.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpfe1ugh04/peek_4_3_15.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670746 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfe1ugh04/peek_4_3_15.ltlf\n     670747                       | paste -sd'&'\n     670748 Killed                  | ltlsynt --part-file=/tmp/tmpfe1ugh04/peek_4_3_15.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_16.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpt0qr14ex/peek_4_3_16.ltlf.dfa.rev.neg /tmp/tmpt0qr14ex/peek_4_3_16.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_16.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_16.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcwb701sy/peek_4_3_16.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpcwb701sy/peek_4_3_16.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671280 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcwb701sy/peek_4_3_16.ltlf\n     671281                       | paste -sd'&'\n     671282 Killed                  | ltlsynt --part-file=/tmp/tmpcwb701sy/peek_4_3_16.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_16.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_17.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqd5uehce/peek_4_3_17.ltlf.dfa.rev.neg /tmp/tmpqd5uehce/peek_4_3_17.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_17.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp8evu8y0l/peek_4_3_17.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp8evu8y0l/peek_4_3_17.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638446 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp8evu8y0l/peek_4_3_17.ltlf\n     638447                       | paste -sd'&'\n     638448 Killed                  | ltlsynt --part-file=/tmp/tmp8evu8y0l/peek_4_3_17.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_18.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqe5wzuy3/peek_4_3_18.ltlf.dfa.rev.neg /tmp/tmpqe5wzuy3/peek_4_3_18.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_18.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkyw7uw2g/peek_4_3_18.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpkyw7uw2g/peek_4_3_18.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638433 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkyw7uw2g/peek_4_3_18.ltlf\n     638434                       | paste -sd'&'\n     638435 Killed                  | ltlsynt --part-file=/tmp/tmpkyw7uw2g/peek_4_3_18.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_19.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpk6mfgy53/peek_4_3_19.ltlf.dfa.rev.neg /tmp/tmpk6mfgy53/peek_4_3_19.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_19.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4_46ldkk/peek_4_3_19.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4_46ldkk/peek_4_3_19.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638644 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4_46ldkk/peek_4_3_19.ltlf\n     638645                       | paste -sd'&'\n     638646 Killed                  | ltlsynt --part-file=/tmp/tmp4_46ldkk/peek_4_3_19.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_2.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2uqphilb/peek_4_3_2.ltlf.dfa.rev.neg /tmp/tmp2uqphilb/peek_4_3_2.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_2.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_2.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmposnlux4i/peek_4_3_2.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmposnlux4i/peek_4_3_2.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638883 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmposnlux4i/peek_4_3_2.ltlf\n     638884                       | paste -sd'&'\n     638885 Killed                  | ltlsynt --part-file=/tmp/tmposnlux4i/peek_4_3_2.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_2.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_20.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwzgbj7t5/peek_4_3_20.ltlf.dfa.rev.neg /tmp/tmpwzgbj7t5/peek_4_3_20.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_20.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp1_lf6fm9/peek_4_3_20.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp1_lf6fm9/peek_4_3_20.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639552 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp1_lf6fm9/peek_4_3_20.ltlf\n     639553                       | paste -sd'&'\n     639554 Killed                  | ltlsynt --part-file=/tmp/tmp1_lf6fm9/peek_4_3_20.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_21.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptuyj0fyf/peek_4_3_21.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmptuyj0fyf/peek_4_3_21.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639065 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptuyj0fyf/peek_4_3_21.ltlf\n     639066                       | paste -sd'&'\n     639067 Killed                  | ltlsynt --part-file=/tmp/tmptuyj0fyf/peek_4_3_21.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_22.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpg3_4ac5r/peek_4_3_22.ltlf.dfa.rev.neg /tmp/tmpg3_4ac5r/peek_4_3_22.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_22.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_22.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpnbziou37/peek_4_3_22.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpnbziou37/peek_4_3_22.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638062 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpnbziou37/peek_4_3_22.ltlf\n     638063                       | paste -sd'&'\n     638064 Killed                  | ltlsynt --part-file=/tmp/tmpnbziou37/peek_4_3_22.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_22.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_23.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoqsiqf4o/peek_4_3_23.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpoqsiqf4o/peek_4_3_23.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671158 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoqsiqf4o/peek_4_3_23.ltlf\n     671159                       | paste -sd'&'\n     671160 Killed                  | ltlsynt --part-file=/tmp/tmpoqsiqf4o/peek_4_3_23.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_23.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_24.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpa7ec3mfg/peek_4_3_24.ltlf.dfa.rev.neg /tmp/tmpa7ec3mfg/peek_4_3_24.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_24.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_24.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6x4l1lma/peek_4_3_24.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp6x4l1lma/peek_4_3_24.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670580 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6x4l1lma/peek_4_3_24.ltlf\n     670581                       | paste -sd'&'\n     670582 Killed                  | ltlsynt --part-file=/tmp/tmp6x4l1lma/peek_4_3_24.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_24.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_25.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5tcl_ekq/peek_4_3_25.ltlf.dfa.rev.neg /tmp/tmp5tcl_ekq/peek_4_3_25.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_25.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpabxs7ctr/peek_4_3_25.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpabxs7ctr/peek_4_3_25.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670428 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpabxs7ctr/peek_4_3_25.ltlf\n     670429                       | paste -sd'&'\n     670430 Killed                  | ltlsynt --part-file=/tmp/tmpabxs7ctr/peek_4_3_25.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_26.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp070kc_s7/peek_4_3_26.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp070kc_s7/peek_4_3_26.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670903 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp070kc_s7/peek_4_3_26.ltlf\n     670904                       | paste -sd'&'\n     670905 Killed                  | ltlsynt --part-file=/tmp/tmp070kc_s7/peek_4_3_26.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_27.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpimmfhsla/peek_4_3_27.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpimmfhsla/peek_4_3_27.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671392 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpimmfhsla/peek_4_3_27.ltlf\n     671393                       | paste -sd'&'\n     671394 Killed                  | ltlsynt --part-file=/tmp/tmpimmfhsla/peek_4_3_27.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_27.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_28.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpiibolcrl/peek_4_3_28.ltlf.dfa.rev.neg /tmp/tmpiibolcrl/peek_4_3_28.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_28.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgd754cpz/peek_4_3_28.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpgd754cpz/peek_4_3_28.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671007 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgd754cpz/peek_4_3_28.ltlf\n     671008                       | paste -sd'&'\n     671009 Killed                  | ltlsynt --part-file=/tmp/tmpgd754cpz/peek_4_3_28.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_29.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_fhdf507/peek_4_3_29.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_fhdf507/peek_4_3_29.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671420 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_fhdf507/peek_4_3_29.ltlf\n     671421                       | paste -sd'&'\n     671422 Killed                  | ltlsynt --part-file=/tmp/tmp_fhdf507/peek_4_3_29.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_29.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_3.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg61zqr_q/peek_4_3_3.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpg61zqr_q/peek_4_3_3.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670753 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg61zqr_q/peek_4_3_3.ltlf\n     670754                       | paste -sd'&'\n     670755 Killed                  | ltlsynt --part-file=/tmp/tmpg61zqr_q/peek_4_3_3.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_3.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_30.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzcjbpyhd/peek_4_3_30.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpzcjbpyhd/peek_4_3_30.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671284 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzcjbpyhd/peek_4_3_30.ltlf\n     671285                       | paste -sd'&'\n     671286 Killed                  | ltlsynt --part-file=/tmp/tmpzcjbpyhd/peek_4_3_30.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_31.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3pmd3qko/peek_4_3_31.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp3pmd3qko/peek_4_3_31.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638469 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3pmd3qko/peek_4_3_31.ltlf\n     638470                       | paste -sd'&'\n     638471 Killed                  | ltlsynt --part-file=/tmp/tmp3pmd3qko/peek_4_3_31.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_31.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_32.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpga8vgs_u/peek_4_3_32.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpga8vgs_u/peek_4_3_32.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638455 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpga8vgs_u/peek_4_3_32.ltlf\n     638456                       | paste -sd'&'\n     638457 Killed                  | ltlsynt --part-file=/tmp/tmpga8vgs_u/peek_4_3_32.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_33.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz83w0vzw/peek_4_3_33.ltlf.dfa.rev.neg /tmp/tmpz83w0vzw/peek_4_3_33.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_33.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_33.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxpmwoiae/peek_4_3_33.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpxpmwoiae/peek_4_3_33.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638652 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxpmwoiae/peek_4_3_33.ltlf\n     638653                       | paste -sd'&'\n     638654 Killed                  | ltlsynt --part-file=/tmp/tmpxpmwoiae/peek_4_3_33.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_33.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_34.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpyess7ll9/peek_4_3_34.ltlf.dfa.rev.neg /tmp/tmpyess7ll9/peek_4_3_34.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_34.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprabgyu6_/peek_4_3_34.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmprabgyu6_/peek_4_3_34.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638902 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprabgyu6_/peek_4_3_34.ltlf\n     638903                       | paste -sd'&'\n     638904 Killed                  | ltlsynt --part-file=/tmp/tmprabgyu6_/peek_4_3_34.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_35.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpy1qa77q3/peek_4_3_35.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpy1qa77q3/peek_4_3_35.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639578 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpy1qa77q3/peek_4_3_35.ltlf\n     639579                       | paste -sd'&'\n     639580 Killed                  | ltlsynt --part-file=/tmp/tmpy1qa77q3/peek_4_3_35.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_35.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_36.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpw42mwqwx/peek_4_3_36.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpw42mwqwx/peek_4_3_36.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639074 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpw42mwqwx/peek_4_3_36.ltlf\n     639075                       | paste -sd'&'\n     639076 Killed                  | ltlsynt --part-file=/tmp/tmpw42mwqwx/peek_4_3_36.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_36.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_37.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8foy134p/peek_4_3_37.ltlf.dfa.rev.neg /tmp/tmp8foy134p/peek_4_3_37.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_37.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpapwg85hg/peek_4_3_37.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpapwg85hg/peek_4_3_37.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638115 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpapwg85hg/peek_4_3_37.ltlf\n     638116                       | paste -sd'&'\n     638117 Killed                  | ltlsynt --part-file=/tmp/tmpapwg85hg/peek_4_3_37.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_38.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwhhwn48l/peek_4_3_38.ltlf.dfa.rev.neg /tmp/tmpwhhwn48l/peek_4_3_38.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_38.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5y85jgf6/peek_4_3_38.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5y85jgf6/peek_4_3_38.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671169 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5y85jgf6/peek_4_3_38.ltlf\n     671170                       | paste -sd'&'\n     671171 Killed                  | ltlsynt --part-file=/tmp/tmp5y85jgf6/peek_4_3_38.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_39.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkpo4v6jl/peek_4_3_39.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpkpo4v6jl/peek_4_3_39.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670585 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkpo4v6jl/peek_4_3_39.ltlf\n     670586                       | paste -sd'&'\n     670587 Killed                  | ltlsynt --part-file=/tmp/tmpkpo4v6jl/peek_4_3_39.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_39.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_4.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcpqby4y_/peek_4_3_4.ltlf.dfa.rev.neg /tmp/tmpcpqby4y_/peek_4_3_4.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_4.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6xwhx8j9/peek_4_3_4.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp6xwhx8j9/peek_4_3_4.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670432 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp6xwhx8j9/peek_4_3_4.ltlf\n     670433                       | paste -sd'&'\n     670434 Killed                  | ltlsynt --part-file=/tmp/tmp6xwhx8j9/peek_4_3_4.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_40.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg13ksumk/peek_4_3_40.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpg13ksumk/peek_4_3_40.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670911 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg13ksumk/peek_4_3_40.ltlf\n     670912                       | paste -sd'&'\n     670913 Killed                  | ltlsynt --part-file=/tmp/tmpg13ksumk/peek_4_3_40.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_40.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_41.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpl6lg0jd5/peek_4_3_41.ltlf.dfa.rev.neg /tmp/tmpl6lg0jd5/peek_4_3_41.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_41.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_3vka5x1/peek_4_3_41.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_3vka5x1/peek_4_3_41.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671400 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_3vka5x1/peek_4_3_41.ltlf\n     671401                       | paste -sd'&'\n     671402 Killed                  | ltlsynt --part-file=/tmp/tmp_3vka5x1/peek_4_3_41.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_42.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxu_rqkqi/peek_4_3_42.ltlf.dfa.rev.neg /tmp/tmpxu_rqkqi/peek_4_3_42.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_42.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_42.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpp2byn0e1/peek_4_3_42.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpp2byn0e1/peek_4_3_42.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671011 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpp2byn0e1/peek_4_3_42.ltlf\n     671012                       | paste -sd'&'\n     671013 Killed                  | ltlsynt --part-file=/tmp/tmpp2byn0e1/peek_4_3_42.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_42.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_43.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0wyfqnru/peek_4_3_43.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp0wyfqnru/peek_4_3_43.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671424 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0wyfqnru/peek_4_3_43.ltlf\n     671425                       | paste -sd'&'\n     671426 Killed                  | ltlsynt --part-file=/tmp/tmp0wyfqnru/peek_4_3_43.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_44.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqp4wro6j/peek_4_3_44.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpqp4wro6j/peek_4_3_44.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670764 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqp4wro6j/peek_4_3_44.ltlf\n     670765                       | paste -sd'&'\n     670766 Killed                  | ltlsynt --part-file=/tmp/tmpqp4wro6j/peek_4_3_44.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_45.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpg49jixx8/peek_4_3_45.ltlf.dfa.rev.neg /tmp/tmpg49jixx8/peek_4_3_45.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_45.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7sorprye/peek_4_3_45.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7sorprye/peek_4_3_45.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671288 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7sorprye/peek_4_3_45.ltlf\n     671289                       | paste -sd'&'\n     671290 Killed                  | ltlsynt --part-file=/tmp/tmp7sorprye/peek_4_3_45.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_46.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_ldv96jy/peek_4_3_46.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_ldv96jy/peek_4_3_46.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638477 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_ldv96jy/peek_4_3_46.ltlf\n     638478                       | paste -sd'&'\n     638479 Killed                  | ltlsynt --part-file=/tmp/tmp_ldv96jy/peek_4_3_46.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_47.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvg8aab8z/peek_4_3_47.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvg8aab8z/peek_4_3_47.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638473 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvg8aab8z/peek_4_3_47.ltlf\n     638474                       | paste -sd'&'\n     638475 Killed                  | ltlsynt --part-file=/tmp/tmpvg8aab8z/peek_4_3_47.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_48.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpwc8w72zf/peek_4_3_48.ltlf.dfa.rev.neg /tmp/tmpwc8w72zf/peek_4_3_48.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_48.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpftp_n_bd/peek_4_3_48.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpftp_n_bd/peek_4_3_48.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638656 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpftp_n_bd/peek_4_3_48.ltlf\n     638657                       | paste -sd'&'\n     638658 Killed                  | ltlsynt --part-file=/tmp/tmpftp_n_bd/peek_4_3_48.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_49.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3x519sk6/peek_4_3_49.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp3x519sk6/peek_4_3_49.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638918 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3x519sk6/peek_4_3_49.ltlf\n     638919                       | paste -sd'&'\n     638920 Killed                  | ltlsynt --part-file=/tmp/tmp3x519sk6/peek_4_3_49.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_5.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg6uykho3/peek_4_3_5.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpg6uykho3/peek_4_3_5.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"the following signals can be temporarily removed:\n  peek_env_0 := 1\nnew formula: (plate_env_0 & plate_env_1 & plate_env_2 & plate_env_3 & G(X[!]turn_env -> ((!plate_env_0 <-> X[!]plate_env_0) -> !(!plate_env_1 <-> X[!]plate_env_1))) & G(X[!]turn_env -> ((!plate_env_0 <-> X[!]plate_env_0) -> !(!plate_env_2 <-> X[!]plate_env_2))) & G(X[!]turn_env -> ((!plate_env_0 <-> X[!]plate_env_0) -> !(!plate_env_3 <-> X[!]plate_env_3))) & G(X[!]turn_env -> ((!plate_env_1 <-> X[!]plate_env_1) -> !(!plate_env_2 <-> X[!]plate_env_2))) & G(X[!]turn_env -> ((!plate_env_1 <-> X[!]plate_env_1) -> !(!plate_env_3 <-> X[!]plate_env_3))) & G(X[!]turn_env -> ((!plate_env_2 <-> X[!]plate_env_2) -> !(!plate_env_3 <-> X[!]plate_env_3))) & G(X[!]!turn_env -> !(!plate_env_0 <-> X[!]plate_env_0)) & G(X[!]!turn_env -> !(!plate_env_1 <-> X[!]plate_env_1)) & G(X[!]!turn_env -> !(!plate_env_2 <-> X[!]plate_env_2)) & G(X[!]!turn_env -> !(!plate_env_3 <-> X[!]plate_env_3)) & G(peek_env_1 <-> (plate_env_3 & !plate_sys_1 & plate_sys_2 & !plate_sys_3)) & G(peek_env_2 <-> (plate_env_0 & !plate_env_1 & plate_env_2 & plate_env_3 & plate_sys_1 & plate_sys_2)) & G(peek_sys_0 <-> (!plate_env_1 & plate_env_3 & plate_sys_1 & !plate_sys_3)) & G(peek_sys_1 <-> (!plate_env_1 & plate_env_2 & plate_env_3)) & G(peek_sys_2 <-> (!plate_env_1 & !plate_env_3 & !plate_sys_2))) -> (plate_sys_0 & plate_sys_1 & plate_sys_2 & plate_sys_3 & !turn_env & !turn_sys & X[!]turn_sys & X[!]G(!turn_env <-> turn_sys) & X[!]G(X[!]1 -> (turn_env <-> X[!]turn_sys)) & G(X[!]turn_sys -> ((!plate_sys_0 <-> X[!]plate_sys_0) -> !(!plate_sys_1 <-> X[!]plate_sys_1))) & G(X[!]turn_sys -> ((!plate_sys_0 <-> X[!]plate_sys_0) -> !(!plate_sys_2 <-> X[!]plate_sys_2))) & G(X[!]turn_sys -> ((!plate_sys_0 <-> X[!]plate_sys_0) -> !(!plate_sys_3 <-> X[!]plate_sys_3))) & G(X[!]turn_sys -> ((!plate_sys_1 <-> X[!]plate_sys_1) -> !(!plate_sys_2 <-> X[!]plate_sys_2))) & G(X[!]turn_sys -> ((!plate_sys_1 <-> X[!]plate_sys_1) -> !(!plate_sys_3 <-> X[!]plate_sys_3))) & G(X[!]turn_sys -> ((!plate_sys_2 <-> X[!]plate_sys_2) -> !(!plate_sys_3 <-> X[!]plate_sys_3))) & G(X[!]!turn_sys -> !(!plate_sys_0 <-> X[!]plate_sys_0)) & G(X[!]!turn_sys -> !(!plate_sys_1 <-> X[!]plate_sys_1)) & G(X[!]!turn_sys -> !(!plate_sys_2 <-> X[!]plate_sys_2)) & G(X[!]!turn_sys -> !(!plate_sys_3 <-> X[!]plate_sys_3)) & ((!turn_env & (turn_env -> !peek_env_1) & (turn_env -> !peek_env_2)) U (turn_sys & (peek_sys_0 | peek_sys_1 | peek_sys_2))))\nthere are 1 subformulas\n/bin/sh: line 1: 639586 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg6uykho3/peek_4_3_5.ltlf\n     639587                       | paste -sd'&'\n     639588 Killed                  | ltlsynt --part-file=/tmp/tmpg6uykho3/peek_4_3_5.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_50.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnyeg7_3r/peek_4_3_50.ltlf.dfa.rev.neg /tmp/tmpnyeg7_3r/peek_4_3_50.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_50.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmovw5nec/peek_4_3_50.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpmovw5nec/peek_4_3_50.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639078 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmovw5nec/peek_4_3_50.ltlf\n     639079                       | paste -sd'&'\n     639080 Killed                  | ltlsynt --part-file=/tmp/tmpmovw5nec/peek_4_3_50.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_51.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpl8jh0l0x/peek_4_3_51.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpl8jh0l0x/peek_4_3_51.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638127 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpl8jh0l0x/peek_4_3_51.ltlf\n     638128                       | paste -sd'&'\n     638129 Killed                  | ltlsynt --part-file=/tmp/tmpl8jh0l0x/peek_4_3_51.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_52.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpibenb5gs/peek_4_3_52.ltlf.dfa.rev.neg /tmp/tmpibenb5gs/peek_4_3_52.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_52.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpju36tabx/peek_4_3_52.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpju36tabx/peek_4_3_52.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671173 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpju36tabx/peek_4_3_52.ltlf\n     671174                       | paste -sd'&'\n     671175 Killed                  | ltlsynt --part-file=/tmp/tmpju36tabx/peek_4_3_52.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_53.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqwb60tlj/peek_4_3_53.ltlf.dfa.rev.neg /tmp/tmpqwb60tlj/peek_4_3_53.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_53.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpylr92bxt/peek_4_3_53.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpylr92bxt/peek_4_3_53.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670592 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpylr92bxt/peek_4_3_53.ltlf\n     670593                       | paste -sd'&'\n     670594 Killed                  | ltlsynt --part-file=/tmp/tmpylr92bxt/peek_4_3_53.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_54.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpao1b_nhc/peek_4_3_54.ltlf.dfa.rev.neg /tmp/tmpao1b_nhc/peek_4_3_54.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_54.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvjm7_wgr/peek_4_3_54.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvjm7_wgr/peek_4_3_54.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670436 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvjm7_wgr/peek_4_3_54.ltlf\n     670437                       | paste -sd'&'\n     670438 Killed                  | ltlsynt --part-file=/tmp/tmpvjm7_wgr/peek_4_3_54.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_55.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplndcwdz8/peek_4_3_55.ltlf.dfa.rev.neg /tmp/tmplndcwdz8/peek_4_3_55.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_55.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7f9qd2rp/peek_4_3_55.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7f9qd2rp/peek_4_3_55.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670918 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7f9qd2rp/peek_4_3_55.ltlf\n     670919                       | paste -sd'&'\n     670920 Killed                  | ltlsynt --part-file=/tmp/tmp7f9qd2rp/peek_4_3_55.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_56.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxxs3gteq/peek_4_3_56.ltlf.dfa.rev.neg /tmp/tmpxxs3gteq/peek_4_3_56.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_56.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoobuyhal/peek_4_3_56.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpoobuyhal/peek_4_3_56.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671408 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoobuyhal/peek_4_3_56.ltlf\n     671409                       | paste -sd'&'\n     671410 Killed                  | ltlsynt --part-file=/tmp/tmpoobuyhal/peek_4_3_56.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_57.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgw8nycg_/peek_4_3_57.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpgw8nycg_/peek_4_3_57.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671018 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpgw8nycg_/peek_4_3_57.ltlf\n     671019                       | paste -sd'&'\n     671020 Killed                  | ltlsynt --part-file=/tmp/tmpgw8nycg_/peek_4_3_57.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_58.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4dalqays/peek_4_3_58.ltlf.dfa.rev.neg /tmp/tmp4dalqays/peek_4_3_58.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_58.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5_nb33bq/peek_4_3_58.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5_nb33bq/peek_4_3_58.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671432 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5_nb33bq/peek_4_3_58.ltlf\n     671433                       | paste -sd'&'\n     671434 Killed                  | ltlsynt --part-file=/tmp/tmp5_nb33bq/peek_4_3_58.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_59.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp7g2kxay5/peek_4_3_59.ltlf.dfa.rev.neg /tmp/tmp7g2kxay5/peek_4_3_59.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_59.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4g4yjrsm/peek_4_3_59.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4g4yjrsm/peek_4_3_59.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670768 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4g4yjrsm/peek_4_3_59.ltlf\n     670769                       | paste -sd'&'\n     670770 Killed                  | ltlsynt --part-file=/tmp/tmp4g4yjrsm/peek_4_3_59.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_6.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf_nngqam/peek_4_3_6.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpf_nngqam/peek_4_3_6.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671292 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf_nngqam/peek_4_3_6.ltlf\n     671293                       | paste -sd'&'\n     671294 Killed                  | ltlsynt --part-file=/tmp/tmpf_nngqam/peek_4_3_6.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_60.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbm80r4qv/peek_4_3_60.ltlf.dfa.rev.neg /tmp/tmpbm80r4qv/peek_4_3_60.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_60.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_60.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpaw_73o9p/peek_4_3_60.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpaw_73o9p/peek_4_3_60.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638482 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpaw_73o9p/peek_4_3_60.ltlf\n     638483                       | paste -sd'&'\n     638484 Killed                  | ltlsynt --part-file=/tmp/tmpaw_73o9p/peek_4_3_60.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_60.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_61.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr9apa5jf/peek_4_3_61.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpr9apa5jf/peek_4_3_61.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638490 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr9apa5jf/peek_4_3_61.ltlf\n     638491                       | paste -sd'&'\n     638492 Killed                  | ltlsynt --part-file=/tmp/tmpr9apa5jf/peek_4_3_61.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_61.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_62.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptvtf01r4/peek_4_3_62.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmptvtf01r4/peek_4_3_62.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638663 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptvtf01r4/peek_4_3_62.ltlf\n     638664                       | paste -sd'&'\n     638665 Killed                  | ltlsynt --part-file=/tmp/tmptvtf01r4/peek_4_3_62.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_63.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4rn7w1r0/peek_4_3_63.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4rn7w1r0/peek_4_3_63.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638930 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4rn7w1r0/peek_4_3_63.ltlf\n     638931                       | paste -sd'&'\n     638932 Killed                  | ltlsynt --part-file=/tmp/tmp4rn7w1r0/peek_4_3_63.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_64.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpb0ur8gpk/peek_4_3_64.ltlf.dfa.rev.neg /tmp/tmpb0ur8gpk/peek_4_3_64.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_64.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_64.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp34jmb6e_/peek_4_3_64.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp34jmb6e_/peek_4_3_64.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639603 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp34jmb6e_/peek_4_3_64.ltlf\n     639604                       | paste -sd'&'\n     639605 Killed                  | ltlsynt --part-file=/tmp/tmp34jmb6e_/peek_4_3_64.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_64.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_65.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxbrn1ec3/peek_4_3_65.ltlf.dfa.rev.neg /tmp/tmpxbrn1ec3/peek_4_3_65.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_65.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9hgv9n0p/peek_4_3_65.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp9hgv9n0p/peek_4_3_65.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639086 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9hgv9n0p/peek_4_3_65.ltlf\n     639087                       | paste -sd'&'\n     639088 Killed                  | ltlsynt --part-file=/tmp/tmp9hgv9n0p/peek_4_3_65.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2dgm6nlv/peek_4_3_66.ltlf.dfa.rev.neg /tmp/tmp2dgm6nlv/peek_4_3_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_66.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmsf4imjl/peek_4_3_66.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpmsf4imjl/peek_4_3_66.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638131 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmsf4imjl/peek_4_3_66.ltlf\n     638132                       | paste -sd'&'\n     638133 Killed                  | ltlsynt --part-file=/tmp/tmpmsf4imjl/peek_4_3_66.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_67.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpoufg3dfw/peek_4_3_67.ltlf.dfa.rev.neg /tmp/tmpoufg3dfw/peek_4_3_67.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_67.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_67.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyueak334/peek_4_3_67.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpyueak334/peek_4_3_67.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671178 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyueak334/peek_4_3_67.ltlf\n     671179                       | paste -sd'&'\n     671180 Killed                  | ltlsynt --part-file=/tmp/tmpyueak334/peek_4_3_67.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_67.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_68.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpjf5201dq/peek_4_3_68.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpjf5201dq/peek_4_3_68.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670603 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpjf5201dq/peek_4_3_68.ltlf\n     670604                       | paste -sd'&'\n     670605 Killed                  | ltlsynt --part-file=/tmp/tmpjf5201dq/peek_4_3_68.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_69.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx09vo5se/peek_4_3_69.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpx09vo5se/peek_4_3_69.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670440 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx09vo5se/peek_4_3_69.ltlf\n     670441                       | paste -sd'&'\n     670442 Killed                  | ltlsynt --part-file=/tmp/tmpx09vo5se/peek_4_3_69.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_69.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_7.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwhnf51t3/peek_4_3_7.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpwhnf51t3/peek_4_3_7.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670925 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwhnf51t3/peek_4_3_7.ltlf\n     670926                       | paste -sd'&'\n     670927 Killed                  | ltlsynt --part-file=/tmp/tmpwhnf51t3/peek_4_3_7.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_70.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3xea8ovj/peek_4_3_70.ltlf.dfa.rev.neg /tmp/tmp3xea8ovj/peek_4_3_70.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_70.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpskojyy5r/peek_4_3_70.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpskojyy5r/peek_4_3_70.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671416 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpskojyy5r/peek_4_3_70.ltlf\n     671417                       | paste -sd'&'\n     671418 Killed                  | ltlsynt --part-file=/tmp/tmpskojyy5r/peek_4_3_70.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_71.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpp677fkb1/peek_4_3_71.ltlf.dfa.rev.neg /tmp/tmpp677fkb1/peek_4_3_71.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_71.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_71.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4_l0nxg3/peek_4_3_71.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4_l0nxg3/peek_4_3_71.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671029 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4_l0nxg3/peek_4_3_71.ltlf\n     671030                       | paste -sd'&'\n     671031 Killed                  | ltlsynt --part-file=/tmp/tmp4_l0nxg3/peek_4_3_71.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_71.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_72.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpknqmq0_s/peek_4_3_72.ltlf.dfa.rev.neg /tmp/tmpknqmq0_s/peek_4_3_72.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_72.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptnppp6si/peek_4_3_72.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmptnppp6si/peek_4_3_72.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671448 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptnppp6si/peek_4_3_72.ltlf\n     671449                       | paste -sd'&'\n     671450 Killed                  | ltlsynt --part-file=/tmp/tmptnppp6si/peek_4_3_72.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_73.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp24k7_f9x/peek_4_3_73.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp24k7_f9x/peek_4_3_73.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670772 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp24k7_f9x/peek_4_3_73.ltlf\n     670773                       | paste -sd'&'\n     670774 Killed                  | ltlsynt --part-file=/tmp/tmp24k7_f9x/peek_4_3_73.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_73.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_74.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp3obxgdaw/peek_4_3_74.ltlf.dfa.rev.neg /tmp/tmp3obxgdaw/peek_4_3_74.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_74.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3f9cuy_g/peek_4_3_74.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp3f9cuy_g/peek_4_3_74.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671296 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3f9cuy_g/peek_4_3_74.ltlf\n     671297                       | paste -sd'&'\n     671298 Killed                  | ltlsynt --part-file=/tmp/tmp3f9cuy_g/peek_4_3_74.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_75.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpbrkswqif/peek_4_3_75.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpbrkswqif/peek_4_3_75.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638503 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpbrkswqif/peek_4_3_75.ltlf\n     638504                       | paste -sd'&'\n     638505 Killed                  | ltlsynt --part-file=/tmp/tmpbrkswqif/peek_4_3_75.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_76.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpt0zxs6as/peek_4_3_76.ltlf.dfa.rev.neg /tmp/tmpt0zxs6as/peek_4_3_76.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_76.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx9gm_6z9/peek_4_3_76.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpx9gm_6z9/peek_4_3_76.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638507 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx9gm_6z9/peek_4_3_76.ltlf\n     638508                       | paste -sd'&'\n     638509 Killed                  | ltlsynt --part-file=/tmp/tmpx9gm_6z9/peek_4_3_76.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpk2aq2dc1/peek_4_3_77.ltlf.dfa.rev.neg /tmp/tmpk2aq2dc1/peek_4_3_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_77.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp882pj_jj/peek_4_3_77.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp882pj_jj/peek_4_3_77.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638669 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp882pj_jj/peek_4_3_77.ltlf\n     638670                       | paste -sd'&'\n     638671 Killed                  | ltlsynt --part-file=/tmp/tmp882pj_jj/peek_4_3_77.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_78.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpv1d53ge2/peek_4_3_78.ltlf.dfa.rev.neg /tmp/tmpv1d53ge2/peek_4_3_78.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_78.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpa30t8efx/peek_4_3_78.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpa30t8efx/peek_4_3_78.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638949 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpa30t8efx/peek_4_3_78.ltlf\n     638950                       | paste -sd'&'\n     638951 Killed                  | ltlsynt --part-file=/tmp/tmpa30t8efx/peek_4_3_78.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_79.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpboo02iby/peek_4_3_79.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpboo02iby/peek_4_3_79.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639617 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpboo02iby/peek_4_3_79.ltlf\n     639618                       | paste -sd'&'\n     639619 Killed                  | ltlsynt --part-file=/tmp/tmpboo02iby/peek_4_3_79.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_79.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_8.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcmor0om8/peek_4_3_8.ltlf.dfa.rev.neg /tmp/tmpcmor0om8/peek_4_3_8.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_8.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkh2z4xot/peek_4_3_8.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpkh2z4xot/peek_4_3_8.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639101 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkh2z4xot/peek_4_3_8.ltlf\n     639102                       | paste -sd'&'\n     639103 Killed                  | ltlsynt --part-file=/tmp/tmpkh2z4xot/peek_4_3_8.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_80.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpm9r5bsdg/peek_4_3_80.ltlf.dfa.rev.neg /tmp/tmpm9r5bsdg/peek_4_3_80.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_80.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpu4qvchne/peek_4_3_80.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpu4qvchne/peek_4_3_80.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638135 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpu4qvchne/peek_4_3_80.ltlf\n     638136                       | paste -sd'&'\n     638137 Killed                  | ltlsynt --part-file=/tmp/tmpu4qvchne/peek_4_3_80.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_81.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_ox79ao9/peek_4_3_81.ltlf.dfa.rev.neg /tmp/tmp_ox79ao9/peek_4_3_81.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_81.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpiehp1o06/peek_4_3_81.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpiehp1o06/peek_4_3_81.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671182 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpiehp1o06/peek_4_3_81.ltlf\n     671183                       | paste -sd'&'\n     671184 Killed                  | ltlsynt --part-file=/tmp/tmpiehp1o06/peek_4_3_81.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_82.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4i8w79lk/peek_4_3_82.ltlf.dfa.rev.neg /tmp/tmp4i8w79lk/peek_4_3_82.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_82.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7464q8bs/peek_4_3_82.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7464q8bs/peek_4_3_82.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670607 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7464q8bs/peek_4_3_82.ltlf\n     670608                       | paste -sd'&'\n     670609 Killed                  | ltlsynt --part-file=/tmp/tmp7464q8bs/peek_4_3_82.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_83.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4vwzyuzp/peek_4_3_83.ltlf.dfa.rev.neg /tmp/tmp4vwzyuzp/peek_4_3_83.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_83.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5b6_x69m/peek_4_3_83.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5b6_x69m/peek_4_3_83.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670444 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5b6_x69m/peek_4_3_83.ltlf\n     670445                       | paste -sd'&'\n     670446 Killed                  | ltlsynt --part-file=/tmp/tmp5b6_x69m/peek_4_3_83.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_84.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpogf2uv4h/peek_4_3_84.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpogf2uv4h/peek_4_3_84.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670929 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpogf2uv4h/peek_4_3_84.ltlf\n     670930                       | paste -sd'&'\n     670931 Killed                  | ltlsynt --part-file=/tmp/tmpogf2uv4h/peek_4_3_84.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_85.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_z_fi7ef/peek_4_3_85.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_z_fi7ef/peek_4_3_85.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671428 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_z_fi7ef/peek_4_3_85.ltlf\n     671429                       | paste -sd'&'\n     671430 Killed                  | ltlsynt --part-file=/tmp/tmp_z_fi7ef/peek_4_3_85.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_86.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp73qgykfs/peek_4_3_86.ltlf.dfa.rev.neg /tmp/tmp73qgykfs/peek_4_3_86.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_86.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkf5vbla9/peek_4_3_86.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpkf5vbla9/peek_4_3_86.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671034 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpkf5vbla9/peek_4_3_86.ltlf\n     671035                       | paste -sd'&'\n     671036 Killed                  | ltlsynt --part-file=/tmp/tmpkf5vbla9/peek_4_3_86.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_87.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpyj673kuw/peek_4_3_87.ltlf.dfa.rev.neg /tmp/tmpyj673kuw/peek_4_3_87.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_87.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7295lfcj/peek_4_3_87.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7295lfcj/peek_4_3_87.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671457 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7295lfcj/peek_4_3_87.ltlf\n     671458                       | paste -sd'&'\n     671459 Killed                  | ltlsynt --part-file=/tmp/tmp7295lfcj/peek_4_3_87.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_88.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp0ye9qo8m/peek_4_3_88.ltlf.dfa.rev.neg /tmp/tmp0ye9qo8m/peek_4_3_88.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_88.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_88.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpeubej2k0/peek_4_3_88.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpeubej2k0/peek_4_3_88.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670777 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpeubej2k0/peek_4_3_88.ltlf\n     670778                       | paste -sd'&'\n     670779 Killed                  | ltlsynt --part-file=/tmp/tmpeubej2k0/peek_4_3_88.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_88.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_89.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp2pwj1fwi/peek_4_3_89.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp2pwj1fwi/peek_4_3_89.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671300 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp2pwj1fwi/peek_4_3_89.ltlf\n     671301                       | paste -sd'&'\n     671302 Killed                  | ltlsynt --part-file=/tmp/tmp2pwj1fwi/peek_4_3_89.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_89.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_9.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmph9lg7o28/peek_4_3_9.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmph9lg7o28/peek_4_3_9.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638511 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmph9lg7o28/peek_4_3_9.ltlf\n     638512                       | paste -sd'&'\n     638513 Killed                  | ltlsynt --part-file=/tmp/tmph9lg7o28/peek_4_3_9.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_90.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp5mr47lu9/peek_4_3_90.ltlf.dfa.rev.neg /tmp/tmp5mr47lu9/peek_4_3_90.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_90.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_90.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpw24vnc56/peek_4_3_90.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpw24vnc56/peek_4_3_90.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638520 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpw24vnc56/peek_4_3_90.ltlf\n     638521                       | paste -sd'&'\n     638522 Killed                  | ltlsynt --part-file=/tmp/tmpw24vnc56/peek_4_3_90.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_90.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_91.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9nfwwpkd/peek_4_3_91.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp9nfwwpkd/peek_4_3_91.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638673 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9nfwwpkd/peek_4_3_91.ltlf\n     638674                       | paste -sd'&'\n     638675 Killed                  | ltlsynt --part-file=/tmp/tmp9nfwwpkd/peek_4_3_91.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_92.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpku0j53ct/peek_4_3_92.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpku0j53ct/peek_4_3_92.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638953 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpku0j53ct/peek_4_3_92.ltlf\n     638954                       | paste -sd'&'\n     638955 Killed                  | ltlsynt --part-file=/tmp/tmpku0j53ct/peek_4_3_92.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_92.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpgwy8cd6w/peek_4_3_93.ltlf.dfa.rev.neg /tmp/tmpgwy8cd6w/peek_4_3_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_93.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7b3v81gm/peek_4_3_93.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7b3v81gm/peek_4_3_93.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639621 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7b3v81gm/peek_4_3_93.ltlf\n     639622                       | paste -sd'&'\n     639623 Killed                  | ltlsynt --part-file=/tmp/tmp7b3v81gm/peek_4_3_93.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_94.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoa9ncpo4/peek_4_3_94.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpoa9ncpo4/peek_4_3_94.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639112 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpoa9ncpo4/peek_4_3_94.ltlf\n     639113                       | paste -sd'&'\n     639114 Killed                  | ltlsynt --part-file=/tmp/tmpoa9ncpo4/peek_4_3_94.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_95.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxk5def4b/peek_4_3_95.ltlf.dfa.rev.neg /tmp/tmpxk5def4b/peek_4_3_95.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_95.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_cvhj0j6/peek_4_3_95.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_cvhj0j6/peek_4_3_95.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638143 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_cvhj0j6/peek_4_3_95.ltlf\n     638144                       | paste -sd'&'\n     638145 Killed                  | ltlsynt --part-file=/tmp/tmp_cvhj0j6/peek_4_3_95.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_96.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpcxzzaw52/peek_4_3_96.ltlf.dfa.rev.neg /tmp/tmpcxzzaw52/peek_4_3_96.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_96.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_96.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcvqryf83/peek_4_3_96.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpcvqryf83/peek_4_3_96.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671186 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcvqryf83/peek_4_3_96.ltlf\n     671187                       | paste -sd'&'\n     671188 Killed                  | ltlsynt --part-file=/tmp/tmpcvqryf83/peek_4_3_96.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_96.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_97.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3721ld03/peek_4_3_97.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp3721ld03/peek_4_3_97.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670615 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3721ld03/peek_4_3_97.ltlf\n     670616                       | paste -sd'&'\n     670617 Killed                  | ltlsynt --part-file=/tmp/tmp3721ld03/peek_4_3_97.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_97.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_98.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpswu2i26y/peek_4_3_98.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpswu2i26y/peek_4_3_98.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670448 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpswu2i26y/peek_4_3_98.ltlf\n     670449                       | paste -sd'&'\n     670450 Killed                  | ltlsynt --part-file=/tmp/tmpswu2i26y/peek_4_3_98.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_98.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_99.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp44unab4y/peek_4_3_99.ltlf.dfa.rev.neg /tmp/tmp44unab4y/peek_4_3_99.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_99.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_ofkgnbt/peek_4_3_99.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_ofkgnbt/peek_4_3_99.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670933 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_ofkgnbt/peek_4_3_99.ltlf\n     670934                       | paste -sd'&'\n     670935 Killed                  | ltlsynt --part-file=/tmp/tmp_ofkgnbt/peek_4_3_99.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_3_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_1.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkf2u2e28/peek_4_4_1.ltlf.dfa.rev.neg /tmp/tmpkf2u2e28/peek_4_4_1.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_1.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp1bpdq_dx/peek_4_4_1.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp1bpdq_dx/peek_4_4_1.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671436 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp1bpdq_dx/peek_4_4_1.ltlf\n     671437                       | paste -sd'&'\n     671438 Killed                  | ltlsynt --part-file=/tmp/tmp1bpdq_dx/peek_4_4_1.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_1.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_10.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyv693323/peek_4_4_10.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpyv693323/peek_4_4_10.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671038 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyv693323/peek_4_4_10.ltlf\n     671039                       | paste -sd'&'\n     671040 Killed                  | ltlsynt --part-file=/tmp/tmpyv693323/peek_4_4_10.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_100.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmplp06aopg/peek_4_4_100.ltlf.dfa.rev.neg /tmp/tmplp06aopg/peek_4_4_100.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_100.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx9bzl5w_/peek_4_4_100.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpx9bzl5w_/peek_4_4_100.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671466 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpx9bzl5w_/peek_4_4_100.ltlf\n     671467                       | paste -sd'&'\n     671468 Killed                  | ltlsynt --part-file=/tmp/tmpx9bzl5w_/peek_4_4_100.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_100.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_11.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp4vanuel3/peek_4_4_11.ltlf.dfa.rev.neg /tmp/tmp4vanuel3/peek_4_4_11.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_11.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpn95ieje4/peek_4_4_11.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpn95ieje4/peek_4_4_11.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670781 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpn95ieje4/peek_4_4_11.ltlf\n     670782                       | paste -sd'&'\n     670783 Killed                  | ltlsynt --part-file=/tmp/tmpn95ieje4/peek_4_4_11.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_11.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_12.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpsnissd3q/peek_4_4_12.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpsnissd3q/peek_4_4_12.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671304 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpsnissd3q/peek_4_4_12.ltlf\n     671305                       | paste -sd'&'\n     671306 Killed                  | ltlsynt --part-file=/tmp/tmpsnissd3q/peek_4_4_12.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_12.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_13.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4cldcjvd/peek_4_4_13.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4cldcjvd/peek_4_4_13.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638524 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4cldcjvd/peek_4_4_13.ltlf\n     638525                       | paste -sd'&'\n     638526 Killed                  | ltlsynt --part-file=/tmp/tmp4cldcjvd/peek_4_4_13.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_13.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_14.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpezxflxx8/peek_4_4_14.ltlf.dfa.rev.neg /tmp/tmpezxflxx8/peek_4_4_14.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_14.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp537crhfp/peek_4_4_14.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp537crhfp/peek_4_4_14.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638528 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp537crhfp/peek_4_4_14.ltlf\n     638529                       | paste -sd'&'\n     638530 Killed                  | ltlsynt --part-file=/tmp/tmp537crhfp/peek_4_4_14.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_14.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_15.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp069pxjmc/peek_4_4_15.ltlf.dfa.rev.neg /tmp/tmp069pxjmc/peek_4_4_15.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_15.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpdhgsmobb/peek_4_4_15.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpdhgsmobb/peek_4_4_15.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638677 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpdhgsmobb/peek_4_4_15.ltlf\n     638678                       | paste -sd'&'\n     638679 Killed                  | ltlsynt --part-file=/tmp/tmpdhgsmobb/peek_4_4_15.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_15.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_16.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_37sp2ed/peek_4_4_16.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_37sp2ed/peek_4_4_16.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638967 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_37sp2ed/peek_4_4_16.ltlf\n     638968                       | paste -sd'&'\n     638969 Killed                  | ltlsynt --part-file=/tmp/tmp_37sp2ed/peek_4_4_16.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_16.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_17.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppjswd3xa/peek_4_4_17.ltlf.dfa.rev.neg /tmp/tmppjswd3xa/peek_4_4_17.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_17.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpy0lch0gg/peek_4_4_17.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpy0lch0gg/peek_4_4_17.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639635 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpy0lch0gg/peek_4_4_17.ltlf\n     639636                       | paste -sd'&'\n     639637 Killed                  | ltlsynt --part-file=/tmp/tmpy0lch0gg/peek_4_4_17.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_17.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_18.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmt1bgcjb/peek_4_4_18.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpmt1bgcjb/peek_4_4_18.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639121 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmt1bgcjb/peek_4_4_18.ltlf\n     639122                       | paste -sd'&'\n     639123 Killed                  | ltlsynt --part-file=/tmp/tmpmt1bgcjb/peek_4_4_18.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_18.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_19.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp2qvqx_pe/peek_4_4_19.ltlf.dfa.rev.neg /tmp/tmp2qvqx_pe/peek_4_4_19.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_19.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpuyww89e9/peek_4_4_19.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpuyww89e9/peek_4_4_19.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638151 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpuyww89e9/peek_4_4_19.ltlf\n     638152                       | paste -sd'&'\n     638153 Killed                  | ltlsynt --part-file=/tmp/tmpuyww89e9/peek_4_4_19.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_19.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_2.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz61zii07/peek_4_4_2.ltlf.dfa.rev.neg /tmp/tmpz61zii07/peek_4_4_2.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_2.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_2.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppyf5s2ep/peek_4_4_2.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmppyf5s2ep/peek_4_4_2.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671193 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppyf5s2ep/peek_4_4_2.ltlf\n     671194                       | paste -sd'&'\n     671195 Killed                  | ltlsynt --part-file=/tmp/tmppyf5s2ep/peek_4_4_2.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_2.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_20.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzl58qelh/peek_4_4_20.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpzl58qelh/peek_4_4_20.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670619 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzl58qelh/peek_4_4_20.ltlf\n     670620                       | paste -sd'&'\n     670621 Killed                  | ltlsynt --part-file=/tmp/tmpzl58qelh/peek_4_4_20.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_20.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_21.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpq9vaoihf/peek_4_4_21.ltlf.dfa.rev.neg /tmp/tmpq9vaoihf/peek_4_4_21.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_21.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzn5kg1qc/peek_4_4_21.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpzn5kg1qc/peek_4_4_21.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670453 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzn5kg1qc/peek_4_4_21.ltlf\n     670454                       | paste -sd'&'\n     670455 Killed                  | ltlsynt --part-file=/tmp/tmpzn5kg1qc/peek_4_4_21.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_21.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_22.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpojifrfwi/peek_4_4_22.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpojifrfwi/peek_4_4_22.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670937 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpojifrfwi/peek_4_4_22.ltlf\n     670938                       | paste -sd'&'\n     670939 Killed                  | ltlsynt --part-file=/tmp/tmpojifrfwi/peek_4_4_22.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_22.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_23.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxzh98vo7/peek_4_4_23.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpxzh98vo7/peek_4_4_23.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671452 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxzh98vo7/peek_4_4_23.ltlf\n     671453                       | paste -sd'&'\n     671454 Killed                  | ltlsynt --part-file=/tmp/tmpxzh98vo7/peek_4_4_23.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_23.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_24.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpafg83tnr/peek_4_4_24.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpafg83tnr/peek_4_4_24.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671042 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpafg83tnr/peek_4_4_24.ltlf\n     671043                       | paste -sd'&'\n     671044 Killed                  | ltlsynt --part-file=/tmp/tmpafg83tnr/peek_4_4_24.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_24.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_25.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpek9qyz2i/peek_4_4_25.ltlf.dfa.rev.neg /tmp/tmpek9qyz2i/peek_4_4_25.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_25.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpuj_4c03c/peek_4_4_25.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpuj_4c03c/peek_4_4_25.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671474 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpuj_4c03c/peek_4_4_25.ltlf\n     671475                       | paste -sd'&'\n     671476 Killed                  | ltlsynt --part-file=/tmp/tmpuj_4c03c/peek_4_4_25.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_25.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_26.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppxz7y2mm/peek_4_4_26.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmppxz7y2mm/peek_4_4_26.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670785 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmppxz7y2mm/peek_4_4_26.ltlf\n     670786                       | paste -sd'&'\n     670787 Killed                  | ltlsynt --part-file=/tmp/tmppxz7y2mm/peek_4_4_26.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_26.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_27.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7txcru_q/peek_4_4_27.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7txcru_q/peek_4_4_27.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671308 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7txcru_q/peek_4_4_27.ltlf\n     671309                       | paste -sd'&'\n     671310 Killed                  | ltlsynt --part-file=/tmp/tmp7txcru_q/peek_4_4_27.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_27.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_28.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfagcrjfh/peek_4_4_28.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpfagcrjfh/peek_4_4_28.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638536 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfagcrjfh/peek_4_4_28.ltlf\n     638537                       | paste -sd'&'\n     638538 Killed                  | ltlsynt --part-file=/tmp/tmpfagcrjfh/peek_4_4_28.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_28.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_29.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf6tb695q/peek_4_4_29.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpf6tb695q/peek_4_4_29.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638540 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf6tb695q/peek_4_4_29.ltlf\n     638541                       | paste -sd'&'\n     638542 Killed                  | ltlsynt --part-file=/tmp/tmpf6tb695q/peek_4_4_29.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_29.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_3.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp9d89l81j/peek_4_4_3.ltlf.dfa.rev.neg /tmp/tmp9d89l81j/peek_4_4_3.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_3.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_3.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr8pgvdhy/peek_4_4_3.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpr8pgvdhy/peek_4_4_3.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638685 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr8pgvdhy/peek_4_4_3.ltlf\n     638686                       | paste -sd'&'\n     638687 Killed                  | ltlsynt --part-file=/tmp/tmpr8pgvdhy/peek_4_4_3.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_3.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_30.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpyyxjqmww/peek_4_4_30.ltlf.dfa.rev.neg /tmp/tmpyyxjqmww/peek_4_4_30.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_30.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpn_46u8yg/peek_4_4_30.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpn_46u8yg/peek_4_4_30.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638971 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpn_46u8yg/peek_4_4_30.ltlf\n     638972                       | paste -sd'&'\n     638973 Killed                  | ltlsynt --part-file=/tmp/tmpn_46u8yg/peek_4_4_30.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_30.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_31.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjs3ozkwd/peek_4_4_31.ltlf.dfa.rev.neg /tmp/tmpjs3ozkwd/peek_4_4_31.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_31.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_31.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwz5_mnug/peek_4_4_31.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpwz5_mnug/peek_4_4_31.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639644 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwz5_mnug/peek_4_4_31.ltlf\n     639645                       | paste -sd'&'\n     639646 Killed                  | ltlsynt --part-file=/tmp/tmpwz5_mnug/peek_4_4_31.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_31.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_32.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpy6uowimk/peek_4_4_32.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpy6uowimk/peek_4_4_32.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639145 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpy6uowimk/peek_4_4_32.ltlf\n     639146                       | paste -sd'&'\n     639147 Killed                  | ltlsynt --part-file=/tmp/tmpy6uowimk/peek_4_4_32.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_32.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_33.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3gbfrwb_/peek_4_4_33.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp3gbfrwb_/peek_4_4_33.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638163 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3gbfrwb_/peek_4_4_33.ltlf\n     638164                       | paste -sd'&'\n     638165 Killed                  | ltlsynt --part-file=/tmp/tmp3gbfrwb_/peek_4_4_33.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_33.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_34.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqtwzshdl/peek_4_4_34.ltlf.dfa.rev.neg /tmp/tmpqtwzshdl/peek_4_4_34.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_34.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpls5o22ip/peek_4_4_34.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpls5o22ip/peek_4_4_34.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671200 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpls5o22ip/peek_4_4_34.ltlf\n     671201                       | paste -sd'&'\n     671202 Killed                  | ltlsynt --part-file=/tmp/tmpls5o22ip/peek_4_4_34.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_34.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_35.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpznhtuxuk/peek_4_4_35.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpznhtuxuk/peek_4_4_35.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670623 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpznhtuxuk/peek_4_4_35.ltlf\n     670624                       | paste -sd'&'\n     670625 Killed                  | ltlsynt --part-file=/tmp/tmpznhtuxuk/peek_4_4_35.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_35.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_36.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo07m0qkb/peek_4_4_36.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpo07m0qkb/peek_4_4_36.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670457 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo07m0qkb/peek_4_4_36.ltlf\n     670458                       | paste -sd'&'\n     670459 Killed                  | ltlsynt --part-file=/tmp/tmpo07m0qkb/peek_4_4_36.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_36.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_37.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpith_7eu1/peek_4_4_37.ltlf.dfa.rev.neg /tmp/tmpith_7eu1/peek_4_4_37.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_37.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_pxt70pj/peek_4_4_37.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_pxt70pj/peek_4_4_37.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670941 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_pxt70pj/peek_4_4_37.ltlf\n     670942                       | paste -sd'&'\n     670943 Killed                  | ltlsynt --part-file=/tmp/tmp_pxt70pj/peek_4_4_37.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_37.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_38.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpztlzvmmp/peek_4_4_38.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpztlzvmmp/peek_4_4_38.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671462 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpztlzvmmp/peek_4_4_38.ltlf\n     671463                       | paste -sd'&'\n     671464 Killed                  | ltlsynt --part-file=/tmp/tmpztlzvmmp/peek_4_4_38.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_38.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_39.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmph5uqz_sv/peek_4_4_39.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmph5uqz_sv/peek_4_4_39.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671046 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmph5uqz_sv/peek_4_4_39.ltlf\n     671047                       | paste -sd'&'\n     671048 Killed                  | ltlsynt --part-file=/tmp/tmph5uqz_sv/peek_4_4_39.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_39.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_4.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpd3cla4j5/peek_4_4_4.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpd3cla4j5/peek_4_4_4.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671482 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpd3cla4j5/peek_4_4_4.ltlf\n     671483                       | paste -sd'&'\n     671484 Killed                  | ltlsynt --part-file=/tmp/tmpd3cla4j5/peek_4_4_4.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_4.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_40.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprf1jauco/peek_4_4_40.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmprf1jauco/peek_4_4_40.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670789 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprf1jauco/peek_4_4_40.ltlf\n     670790                       | paste -sd'&'\n     670791 Killed                  | ltlsynt --part-file=/tmp/tmprf1jauco/peek_4_4_40.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_40.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_41.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0gxiemmk/peek_4_4_41.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp0gxiemmk/peek_4_4_41.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671313 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0gxiemmk/peek_4_4_41.ltlf\n     671314                       | paste -sd'&'\n     671315 Killed                  | ltlsynt --part-file=/tmp/tmp0gxiemmk/peek_4_4_41.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_41.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_42.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxecdgqjz/peek_4_4_42.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpxecdgqjz/peek_4_4_42.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638544 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpxecdgqjz/peek_4_4_42.ltlf\n     638545                       | paste -sd'&'\n     638546 Killed                  | ltlsynt --part-file=/tmp/tmpxecdgqjz/peek_4_4_42.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_42.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_43.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpst8ffunt/peek_4_4_43.ltlf.dfa.rev.neg /tmp/tmpst8ffunt/peek_4_4_43.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_43.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvuoj9qp6/peek_4_4_43.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvuoj9qp6/peek_4_4_43.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638553 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvuoj9qp6/peek_4_4_43.ltlf\n     638554                       | paste -sd'&'\n     638555 Killed                  | ltlsynt --part-file=/tmp/tmpvuoj9qp6/peek_4_4_43.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_43.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_44.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_bk1st68/peek_4_4_44.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp_bk1st68/peek_4_4_44.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638693 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp_bk1st68/peek_4_4_44.ltlf\n     638694                       | paste -sd'&'\n     638695 Killed                  | ltlsynt --part-file=/tmp/tmp_bk1st68/peek_4_4_44.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_44.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_45.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpno74zklz/peek_4_4_45.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpno74zklz/peek_4_4_45.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638980 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpno74zklz/peek_4_4_45.ltlf\n     638981                       | paste -sd'&'\n     638982 Killed                  | ltlsynt --part-file=/tmp/tmpno74zklz/peek_4_4_45.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_45.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_46.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp8upb0a4x/peek_4_4_46.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp8upb0a4x/peek_4_4_46.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639648 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp8upb0a4x/peek_4_4_46.ltlf\n     639649                       | paste -sd'&'\n     639650 Killed                  | ltlsynt --part-file=/tmp/tmp8upb0a4x/peek_4_4_46.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_46.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_47.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpb_lifrwi/peek_4_4_47.ltlf.dfa.rev.neg /tmp/tmpb_lifrwi/peek_4_4_47.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_47.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7cwgld3w/peek_4_4_47.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7cwgld3w/peek_4_4_47.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639159 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7cwgld3w/peek_4_4_47.ltlf\n     639160                       | paste -sd'&'\n     639161 Killed                  | ltlsynt --part-file=/tmp/tmp7cwgld3w/peek_4_4_47.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_47.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_48.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpfnx1fg42/peek_4_4_48.ltlf.dfa.rev.neg /tmp/tmpfnx1fg42/peek_4_4_48.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_48.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp34ttri39/peek_4_4_48.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp34ttri39/peek_4_4_48.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638177 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp34ttri39/peek_4_4_48.ltlf\n     638178                       | paste -sd'&'\n     638179 Killed                  | ltlsynt --part-file=/tmp/tmp34ttri39/peek_4_4_48.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_48.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_49.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpe5qqlbm5/peek_4_4_49.ltlf.dfa.rev.neg /tmp/tmpe5qqlbm5/peek_4_4_49.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_49.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp010wc3r3/peek_4_4_49.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp010wc3r3/peek_4_4_49.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671204 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp010wc3r3/peek_4_4_49.ltlf\n     671205                       | paste -sd'&'\n     671206 Killed                  | ltlsynt --part-file=/tmp/tmp010wc3r3/peek_4_4_49.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_49.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_5.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpmo_cwg69/peek_4_4_5.ltlf.dfa.rev.neg /tmp/tmpmo_cwg69/peek_4_4_5.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_5.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpipp31mc0/peek_4_4_5.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpipp31mc0/peek_4_4_5.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670627 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpipp31mc0/peek_4_4_5.ltlf\n     670628                       | paste -sd'&'\n     670629 Killed                  | ltlsynt --part-file=/tmp/tmpipp31mc0/peek_4_4_5.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_5.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_50.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpnr37jzi3/peek_4_4_50.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpnr37jzi3/peek_4_4_50.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670461 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpnr37jzi3/peek_4_4_50.ltlf\n     670462                       | paste -sd'&'\n     670463 Killed                  | ltlsynt --part-file=/tmp/tmpnr37jzi3/peek_4_4_50.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_50.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_51.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp126hehfi/peek_4_4_51.ltlf.dfa.rev.neg /tmp/tmp126hehfi/peek_4_4_51.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_51.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpe0pyxmxh/peek_4_4_51.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpe0pyxmxh/peek_4_4_51.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670949 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpe0pyxmxh/peek_4_4_51.ltlf\n     670950                       | paste -sd'&'\n     670951 Killed                  | ltlsynt --part-file=/tmp/tmpe0pyxmxh/peek_4_4_51.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_51.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_52.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp13m_in7w/peek_4_4_52.ltlf.dfa.rev.neg /tmp/tmp13m_in7w/peek_4_4_52.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_52.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpj1o35f3l/peek_4_4_52.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpj1o35f3l/peek_4_4_52.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671470 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpj1o35f3l/peek_4_4_52.ltlf\n     671471                       | paste -sd'&'\n     671472 Killed                  | ltlsynt --part-file=/tmp/tmpj1o35f3l/peek_4_4_52.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_52.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_53.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpud4z4kb_/peek_4_4_53.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpud4z4kb_/peek_4_4_53.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671052 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpud4z4kb_/peek_4_4_53.ltlf\n     671053                       | paste -sd'&'\n     671054 Killed                  | ltlsynt --part-file=/tmp/tmpud4z4kb_/peek_4_4_53.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_53.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_54.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmptr9zuecj/peek_4_4_54.ltlf.dfa.rev.neg /tmp/tmptr9zuecj/peek_4_4_54.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_54.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpktj3e8as/peek_4_4_54.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpktj3e8as/peek_4_4_54.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671494 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpktj3e8as/peek_4_4_54.ltlf\n     671495                       | paste -sd'&'\n     671496 Killed                  | ltlsynt --part-file=/tmp/tmpktj3e8as/peek_4_4_54.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_54.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_55.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdkm3_s39/peek_4_4_55.ltlf.dfa.rev.neg /tmp/tmpdkm3_s39/peek_4_4_55.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_55.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplujisqvh/peek_4_4_55.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmplujisqvh/peek_4_4_55.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670793 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplujisqvh/peek_4_4_55.ltlf\n     670794                       | paste -sd'&'\n     670795 Killed                  | ltlsynt --part-file=/tmp/tmplujisqvh/peek_4_4_55.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_55.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_56.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpz0a8y4bw/peek_4_4_56.ltlf.dfa.rev.neg /tmp/tmpz0a8y4bw/peek_4_4_56.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_56.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpej1u38d6/peek_4_4_56.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpej1u38d6/peek_4_4_56.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671317 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpej1u38d6/peek_4_4_56.ltlf\n     671318                       | paste -sd'&'\n     671319 Killed                  | ltlsynt --part-file=/tmp/tmpej1u38d6/peek_4_4_56.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_56.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_57.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpglagzxx_/peek_4_4_57.ltlf.dfa.rev.neg /tmp/tmpglagzxx_/peek_4_4_57.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_57.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpps5vfw72/peek_4_4_57.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpps5vfw72/peek_4_4_57.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638556 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpps5vfw72/peek_4_4_57.ltlf\n     638557                       | paste -sd'&'\n     638558 Killed                  | ltlsynt --part-file=/tmp/tmpps5vfw72/peek_4_4_57.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_57.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_58.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpsaomxlza/peek_4_4_58.ltlf.dfa.rev.neg /tmp/tmpsaomxlza/peek_4_4_58.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_58.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9bygvzro/peek_4_4_58.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp9bygvzro/peek_4_4_58.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638564 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9bygvzro/peek_4_4_58.ltlf\n     638565                       | paste -sd'&'\n     638566 Killed                  | ltlsynt --part-file=/tmp/tmp9bygvzro/peek_4_4_58.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_58.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_59.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg5bd5rti/peek_4_4_59.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpg5bd5rti/peek_4_4_59.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638697 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpg5bd5rti/peek_4_4_59.ltlf\n     638698                       | paste -sd'&'\n     638699 Killed                  | ltlsynt --part-file=/tmp/tmpg5bd5rti/peek_4_4_59.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_59.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_6.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmroql60y/peek_4_4_6.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpmroql60y/peek_4_4_6.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638984 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmroql60y/peek_4_4_6.ltlf\n     638985                       | paste -sd'&'\n     638986 Killed                  | ltlsynt --part-file=/tmp/tmpmroql60y/peek_4_4_6.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_6.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_60.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp32pnawcn/peek_4_4_60.ltlf.dfa.rev.neg /tmp/tmp32pnawcn/peek_4_4_60.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_60.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_60.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo2mx1xdf/peek_4_4_60.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpo2mx1xdf/peek_4_4_60.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639662 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo2mx1xdf/peek_4_4_60.ltlf\n     639663                       | paste -sd'&'\n     639664 Killed                  | ltlsynt --part-file=/tmp/tmpo2mx1xdf/peek_4_4_60.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_60.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_61.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfd4_cct5/peek_4_4_61.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpfd4_cct5/peek_4_4_61.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639172 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpfd4_cct5/peek_4_4_61.ltlf\n     639173                       | paste -sd'&'\n     639174 Killed                  | ltlsynt --part-file=/tmp/tmpfd4_cct5/peek_4_4_61.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_61.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_62.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplswgw632/peek_4_4_62.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmplswgw632/peek_4_4_62.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638196 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplswgw632/peek_4_4_62.ltlf\n     638197                       | paste -sd'&'\n     638198 Killed                  | ltlsynt --part-file=/tmp/tmplswgw632/peek_4_4_62.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_62.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_63.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6ku0q3on/peek_4_4_63.ltlf.dfa.rev.neg /tmp/tmp6ku0q3on/peek_4_4_63.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_63.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzy8fpaub/peek_4_4_63.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpzy8fpaub/peek_4_4_63.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671208 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzy8fpaub/peek_4_4_63.ltlf\n     671209                       | paste -sd'&'\n     671210 Killed                  | ltlsynt --part-file=/tmp/tmpzy8fpaub/peek_4_4_63.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_63.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_64.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3pxw29qg/peek_4_4_64.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp3pxw29qg/peek_4_4_64.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670631 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp3pxw29qg/peek_4_4_64.ltlf\n     670632                       | paste -sd'&'\n     670633 Killed                  | ltlsynt --part-file=/tmp/tmp3pxw29qg/peek_4_4_64.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_64.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_65.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprt2t2hwd/peek_4_4_65.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmprt2t2hwd/peek_4_4_65.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670465 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmprt2t2hwd/peek_4_4_65.ltlf\n     670466                       | paste -sd'&'\n     670467 Killed                  | ltlsynt --part-file=/tmp/tmprt2t2hwd/peek_4_4_65.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_65.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_66.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpecrqp6nn/peek_4_4_66.ltlf.dfa.rev.neg /tmp/tmpecrqp6nn/peek_4_4_66.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_66.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9tgoob3p/peek_4_4_66.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp9tgoob3p/peek_4_4_66.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670957 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9tgoob3p/peek_4_4_66.ltlf\n     670958                       | paste -sd'&'\n     670959 Killed                  | ltlsynt --part-file=/tmp/tmp9tgoob3p/peek_4_4_66.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_66.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_67.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo_mvfj_h/peek_4_4_67.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpo_mvfj_h/peek_4_4_67.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671478 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpo_mvfj_h/peek_4_4_67.ltlf\n     671479                       | paste -sd'&'\n     671480 Killed                  | ltlsynt --part-file=/tmp/tmpo_mvfj_h/peek_4_4_67.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_67.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_68.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplqc6u9d4/peek_4_4_68.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmplqc6u9d4/peek_4_4_68.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671056 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmplqc6u9d4/peek_4_4_68.ltlf\n     671057                       | paste -sd'&'\n     671058 Killed                  | ltlsynt --part-file=/tmp/tmplqc6u9d4/peek_4_4_68.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_68.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_69.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzvs291r0/peek_4_4_69.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpzvs291r0/peek_4_4_69.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671503 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpzvs291r0/peek_4_4_69.ltlf\n     671504                       | paste -sd'&'\n     671505 Killed                  | ltlsynt --part-file=/tmp/tmpzvs291r0/peek_4_4_69.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_69.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_7.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4q90edwe/peek_4_4_7.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp4q90edwe/peek_4_4_7.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670797 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp4q90edwe/peek_4_4_7.ltlf\n     670798                       | paste -sd'&'\n     670799 Killed                  | ltlsynt --part-file=/tmp/tmp4q90edwe/peek_4_4_7.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_7.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_70.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpbkq3ha7l/peek_4_4_70.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpbkq3ha7l/peek_4_4_70.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671321 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpbkq3ha7l/peek_4_4_70.ltlf\n     671322                       | paste -sd'&'\n     671323 Killed                  | ltlsynt --part-file=/tmp/tmpbkq3ha7l/peek_4_4_70.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_70.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_71.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqf_vimst/peek_4_4_71.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpqf_vimst/peek_4_4_71.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638560 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpqf_vimst/peek_4_4_71.ltlf\n     638561                       | paste -sd'&'\n     638562 Killed                  | ltlsynt --part-file=/tmp/tmpqf_vimst/peek_4_4_71.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_71.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_72.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpa9nzg37l/peek_4_4_72.ltlf.dfa.rev.neg /tmp/tmpa9nzg37l/peek_4_4_72.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_72.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpi698rqug/peek_4_4_72.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpi698rqug/peek_4_4_72.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638573 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpi698rqug/peek_4_4_72.ltlf\n     638574                       | paste -sd'&'\n     638575 Killed                  | ltlsynt --part-file=/tmp/tmpi698rqug/peek_4_4_72.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_72.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_73.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpsij768mk/peek_4_4_73.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpsij768mk/peek_4_4_73.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638701 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpsij768mk/peek_4_4_73.ltlf\n     638702                       | paste -sd'&'\n     638703 Killed                  | ltlsynt --part-file=/tmp/tmpsij768mk/peek_4_4_73.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_73.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_74.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpnpub5b36/peek_4_4_74.ltlf.dfa.rev.neg /tmp/tmpnpub5b36/peek_4_4_74.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_74.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpd1nxs9wz/peek_4_4_74.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpd1nxs9wz/peek_4_4_74.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638988 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpd1nxs9wz/peek_4_4_74.ltlf\n     638989                       | paste -sd'&'\n     638990 Killed                  | ltlsynt --part-file=/tmp/tmpd1nxs9wz/peek_4_4_74.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_74.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_75.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpadvysxpe/peek_4_4_75.ltlf.dfa.rev.neg /tmp/tmpadvysxpe/peek_4_4_75.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_75.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmfhuuvm0/peek_4_4_75.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpmfhuuvm0/peek_4_4_75.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639673 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpmfhuuvm0/peek_4_4_75.ltlf\n     639674                       | paste -sd'&'\n     639675 Killed                  | ltlsynt --part-file=/tmp/tmpmfhuuvm0/peek_4_4_75.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_75.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_76.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp8ix82565/peek_4_4_76.ltlf.dfa.rev.neg /tmp/tmp8ix82565/peek_4_4_76.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_76.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5_z_u04m/peek_4_4_76.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5_z_u04m/peek_4_4_76.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639191 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5_z_u04m/peek_4_4_76.ltlf\n     639192                       | paste -sd'&'\n     639193 Killed                  | ltlsynt --part-file=/tmp/tmp5_z_u04m/peek_4_4_76.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_76.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_77.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6hmarvwj/peek_4_4_77.ltlf.dfa.rev.neg /tmp/tmp6hmarvwj/peek_4_4_77.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_77.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyp_susd7/peek_4_4_77.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpyp_susd7/peek_4_4_77.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638219 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyp_susd7/peek_4_4_77.ltlf\n     638220                       | paste -sd'&'\n     638221 Killed                  | ltlsynt --part-file=/tmp/tmpyp_susd7/peek_4_4_77.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_77.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_78.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbhdvcj60/peek_4_4_78.ltlf.dfa.rev.neg /tmp/tmpbhdvcj60/peek_4_4_78.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_78.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwnov98o2/peek_4_4_78.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpwnov98o2/peek_4_4_78.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671212 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpwnov98o2/peek_4_4_78.ltlf\n     671213                       | paste -sd'&'\n     671214 Killed                  | ltlsynt --part-file=/tmp/tmpwnov98o2/peek_4_4_78.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_78.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_79.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvffunn1x/peek_4_4_79.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvffunn1x/peek_4_4_79.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670635 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvffunn1x/peek_4_4_79.ltlf\n     670636                       | paste -sd'&'\n     670637 Killed                  | ltlsynt --part-file=/tmp/tmpvffunn1x/peek_4_4_79.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_79.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_8.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp6cweafa7/peek_4_4_8.ltlf.dfa.rev.neg /tmp/tmp6cweafa7/peek_4_4_8.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_8.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf53eb6ve/peek_4_4_8.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpf53eb6ve/peek_4_4_8.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670469 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf53eb6ve/peek_4_4_8.ltlf\n     670470                       | paste -sd'&'\n     670471 Killed                  | ltlsynt --part-file=/tmp/tmpf53eb6ve/peek_4_4_8.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_8.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_80.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpovzd9r56/peek_4_4_80.ltlf.dfa.rev.neg /tmp/tmpovzd9r56/peek_4_4_80.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_80.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcdccxpq9/peek_4_4_80.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpcdccxpq9/peek_4_4_80.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670965 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpcdccxpq9/peek_4_4_80.ltlf\n     670966                       | paste -sd'&'\n     670967 Killed                  | ltlsynt --part-file=/tmp/tmpcdccxpq9/peek_4_4_80.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_80.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_81.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpppyi56cp/peek_4_4_81.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpppyi56cp/peek_4_4_81.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671486 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpppyi56cp/peek_4_4_81.ltlf\n     671487                       | paste -sd'&'\n     671488 Killed                  | ltlsynt --part-file=/tmp/tmpppyi56cp/peek_4_4_81.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_81.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_82.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpizv7nz83/peek_4_4_82.ltlf.dfa.rev.neg /tmp/tmpizv7nz83/peek_4_4_82.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_82.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpb7lbq9q3/peek_4_4_82.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpb7lbq9q3/peek_4_4_82.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671060 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpb7lbq9q3/peek_4_4_82.ltlf\n     671061                       | paste -sd'&'\n     671062 Killed                  | ltlsynt --part-file=/tmp/tmpb7lbq9q3/peek_4_4_82.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_82.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_83.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5wwk33ea/peek_4_4_83.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp5wwk33ea/peek_4_4_83.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671518 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp5wwk33ea/peek_4_4_83.ltlf\n     671519                       | paste -sd'&'\n     671520 Killed                  | ltlsynt --part-file=/tmp/tmp5wwk33ea/peek_4_4_83.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_83.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_84.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptllc_yks/peek_4_4_84.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmptllc_yks/peek_4_4_84.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670803 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptllc_yks/peek_4_4_84.ltlf\n     670804                       | paste -sd'&'\n     670805 Killed                  | ltlsynt --part-file=/tmp/tmptllc_yks/peek_4_4_84.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_84.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_85.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpdszzlodb/peek_4_4_85.ltlf.dfa.rev.neg /tmp/tmpdszzlodb/peek_4_4_85.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_85.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr8qdt63k/peek_4_4_85.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpr8qdt63k/peek_4_4_85.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671325 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpr8qdt63k/peek_4_4_85.ltlf\n     671326                       | paste -sd'&'\n     671327 Killed                  | ltlsynt --part-file=/tmp/tmpr8qdt63k/peek_4_4_85.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_85.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_86.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpusrfrp_1/peek_4_4_86.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpusrfrp_1/peek_4_4_86.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638569 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpusrfrp_1/peek_4_4_86.ltlf\n     638570                       | paste -sd'&'\n     638571 Killed                  | ltlsynt --part-file=/tmp/tmpusrfrp_1/peek_4_4_86.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_86.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_87.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0rzgcwh5/peek_4_4_87.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp0rzgcwh5/peek_4_4_87.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638590 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp0rzgcwh5/peek_4_4_87.ltlf\n     638591                       | paste -sd'&'\n     638592 Killed                  | ltlsynt --part-file=/tmp/tmp0rzgcwh5/peek_4_4_87.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_87.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_88.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp8s_d20cp/peek_4_4_88.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp8s_d20cp/peek_4_4_88.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638705 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp8s_d20cp/peek_4_4_88.ltlf\n     638706                       | paste -sd'&'\n     638707 Killed                  | ltlsynt --part-file=/tmp/tmp8s_d20cp/peek_4_4_88.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_88.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_89.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvdhee4cy/peek_4_4_89.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpvdhee4cy/peek_4_4_89.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638995 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpvdhee4cy/peek_4_4_89.ltlf\n     638996                       | paste -sd'&'\n     638997 Killed                  | ltlsynt --part-file=/tmp/tmpvdhee4cy/peek_4_4_89.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_89.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmppj5exy7y/peek_4_4_9.ltlf.dfa.rev.neg /tmp/tmppj5exy7y/peek_4_4_9.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_9.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7t9zjnqb/peek_4_4_9.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp7t9zjnqb/peek_4_4_9.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639677 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp7t9zjnqb/peek_4_4_9.ltlf\n     639678                       | paste -sd'&'\n     639679 Killed                  | ltlsynt --part-file=/tmp/tmp7t9zjnqb/peek_4_4_9.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_9.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_90.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpjix630uo/peek_4_4_90.ltlf.dfa.rev.neg /tmp/tmpjix630uo/peek_4_4_90.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_90.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_90.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmphyfbdm4t/peek_4_4_90.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmphyfbdm4t/peek_4_4_90.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 639195 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmphyfbdm4t/peek_4_4_90.ltlf\n     639196                       | paste -sd'&'\n     639197 Killed                  | ltlsynt --part-file=/tmp/tmphyfbdm4t/peek_4_4_90.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_90.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_91.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpqvaetcgs/peek_4_4_91.ltlf.dfa.rev.neg /tmp/tmpqvaetcgs/peek_4_4_91.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_91.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9mm37u4_/peek_4_4_91.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp9mm37u4_/peek_4_4_91.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 638238 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp9mm37u4_/peek_4_4_91.ltlf\n     638239                       | paste -sd'&'\n     638240 Killed                  | ltlsynt --part-file=/tmp/tmp9mm37u4_/peek_4_4_91.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_91.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_92.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpq2ebvq6g/peek_4_4_92.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpq2ebvq6g/peek_4_4_92.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671216 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpq2ebvq6g/peek_4_4_92.ltlf\n     671217                       | paste -sd'&'\n     671218 Killed                  | ltlsynt --part-file=/tmp/tmpq2ebvq6g/peek_4_4_92.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_92.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_93.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbhzfd67e/peek_4_4_93.ltlf.dfa.rev.neg /tmp/tmpbhzfd67e/peek_4_4_93.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_93.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpif2k0rtj/peek_4_4_93.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpif2k0rtj/peek_4_4_93.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670644 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpif2k0rtj/peek_4_4_93.ltlf\n     670645                       | paste -sd'&'\n     670646 Killed                  | ltlsynt --part-file=/tmp/tmpif2k0rtj/peek_4_4_93.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_93.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_94.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpxh9qnmd4/peek_4_4_94.ltlf.dfa.rev.neg /tmp/tmpxh9qnmd4/peek_4_4_94.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_94.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp1u3t8wa8/peek_4_4_94.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp1u3t8wa8/peek_4_4_94.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670473 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp1u3t8wa8/peek_4_4_94.ltlf\n     670474                       | paste -sd'&'\n     670475 Killed                  | ltlsynt --part-file=/tmp/tmp1u3t8wa8/peek_4_4_94.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_94.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_95.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_6cajj8s/peek_4_4_95.ltlf.dfa.rev.neg /tmp/tmp_6cajj8s/peek_4_4_95.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_95.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyt2msnw8/peek_4_4_95.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpyt2msnw8/peek_4_4_95.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670973 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpyt2msnw8/peek_4_4_95.ltlf\n     670974                       | paste -sd'&'\n     670975 Killed                  | ltlsynt --part-file=/tmp/tmpyt2msnw8/peek_4_4_95.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_95.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_96.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpbx884_we/peek_4_4_96.ltlf.dfa.rev.neg /tmp/tmpbx884_we/peek_4_4_96.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_96.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_96.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptis7jem5/peek_4_4_96.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmptis7jem5/peek_4_4_96.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671490 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmptis7jem5/peek_4_4_96.ltlf\n     671491                       | paste -sd'&'\n     671492 Killed                  | ltlsynt --part-file=/tmp/tmptis7jem5/peek_4_4_96.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_96.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_97.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmp_ql418e7/peek_4_4_97.ltlf.dfa.rev.neg /tmp/tmp_ql418e7/peek_4_4_97.part 0 partial cordfa' died with <Signals.SIGKILL: 9>., b''
Count: 1

| Tool | Test |
| --- | --- |
| lucas_projection-based | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_97.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_97.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf0ku_2is/peek_4_4_97.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpf0ku_2is/peek_4_4_97.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671065 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpf0ku_2is/peek_4_4_97.ltlf\n     671066                       | paste -sd'&'\n     671067 Killed                  | ltlsynt --part-file=/tmp/tmpf0ku_2is/peek_4_4_97.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_97.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_98.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpi3gzajwc/peek_4_4_98.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmpi3gzajwc/peek_4_4_98.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 671522 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmpi3gzajwc/peek_4_4_98.ltlf\n     671523                       | paste -sd'&'\n     671524 Killed                  | ltlsynt --part-file=/tmp/tmpi3gzajwc/peek_4_4_98.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_98.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_99.ltlf: Command 'sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp03hzag4e/peek_4_4_99.ltlf | paste -sd'&' | ltlsynt --part-file=/tmp/tmp03hzag4e/peek_4_4_99.part.spot.part --real --verbose --algo=ds' returned non-zero exit status 137., b"there are 1 subformulas\n/bin/sh: line 1: 670807 Done                    sed 's/X/X[!]/g;s/N/X/g;s/^/(/;s/$/)/' /tmp/tmp03hzag4e/peek_4_4_99.ltlf\n     670808                       | paste -sd'&'\n     670809 Killed                  | ltlsynt --part-file=/tmp/tmp03hzag4e/peek_4_4_99.part.spot.part --real --verbose --algo=ds\n"
Count: 1

| Tool | Test |
| --- | --- |
| spot_ltl | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/peek/peek_4_4_99.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_10.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpi2y63r5t/seek_10.ltlf.dfa.quant /tmp/tmpi2y63r5t/seek_10.part.quant 0 full dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_mso | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_10.ltlf |

#### Failed to run /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_9.ltlf: Command '"/RG/rg-fried/alnadav5/lucas/Syft/build/bin/Syft" /tmp/tmpkaqmc0xn/seek_9.ltlf.dfa.quant /tmp/tmpkaqmc0xn/seek_9.part.quant 0 full dfa' died with <Signals.SIGKILL: 9>., b'The number of explicit states: 0\n'
Count: 1

| Tool | Test |
| --- | --- |
| lucas_mso | /RG/rg-fried/alnadav5/ltlf-po-benchmarks/lucas/ltlf/seek_9.ltlf |

### Expected Errors (Timeouts - Status -2)

| Tool | Timeout Count |
| --- | --- |
| lucas_belief-states | 773 |
| lucas_projection-based | 673 |
| spot_ltl | 310 |
| spot_ltlf | 2 |
| spot_ltlfilt | 809 |
