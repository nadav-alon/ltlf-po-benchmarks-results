# Zsh autocomplete for LTLf Benchmarks
_ltlf_benchmarks() {
    local results_dir="/home/cowclaw/results_shards/data/results"
    local label_file="/home/cowclaw/results_shards/data/job_labels.json"
    
    # 1. Load Job IDs and Labels safely
    local -A labels
    local -a job_ids
    if [[ -d "$results_dir" ]]; then
        job_ids=($(ls -1 "$results_dir"))
        if [[ -f "$label_file" ]]; then
            # Load labels into an associative array
            local k v
            while IFS= read -r line; do
                k="${line%%:*}"
                v="${line#*:}"
                labels[$k]="$v"
            done <<< "$(python3 -c "import json; d=json.load(open('$label_file')); [print(f'{k}:{v}') for k,v in d.items()]" 2>/dev/null)"
        fi
    fi

    local prev="$words[CURRENT-1]"
    local cur="$words[CURRENT]"

    case "$prev" in
        --job-id|--job-a|--job-b)
            # Filter matches by checking both ID and Description
            local -a display_list val_list
            local id desc
            for id in $job_ids; do
                desc="${labels[$id]}"
                # If current input matches either ID or Description (case-insensitive)
                # We use * prefix/suffix for fuzzy matching within the word
                if [[ -z "$cur" || "$id" == *"$cur"* || "${(L)desc}" == *"${(L)cur}"* ]]; then
                    val_list+=("$id")
                    if [[ -n "$desc" ]]; then
                        display_list+=("${(r:10:)id} -- $desc")
                    else
                        display_list+=("$id")
                    fi
                fi
            done
            
            # -U: Don't perform standard prefix matching (we handled filtering manually)
            # -d: Specify display strings (ID -- Description)
            # -a: Specify actual values to insert (the ID)
            compadd -U -d display_list -a val_list
            return
            ;;
        --tool-a|--tool-b)
            local job_val=""
            local i
            for ((i=CURRENT-1; i>0; i--)); do
                if [[ "$words[i]" == "--job-a" || "$words[i]" == "--job-b" || "$words[i]" == "--job-id" ]]; then
                    job_val="$words[i+1]"
                    break
                fi
            done
            if [[ -n "$job_val" && -d "$results_dir/$job_val" ]]; then
                local -a tools
                tools=($(ls -1 "$results_dir/$job_val"))
                _describe -t tools 'tools' tools
                return
            fi
            ;;
    esac

    local -a opts
    opts=(
        '--job-id:ID of the job to analyze'
        '--job-a:First job ID for comparison'
        '--job-b:Second job ID for comparison'
        '--tool-a:Tool name for first job'
        '--tool-b:Tool name for second job'
        '--results-dir:Path to results directory'
        '--list:List all failing test instances'
        '--csv:Export failures to a CSV file'
        '--output:Output filename'
        '--output-inconsistent:File to save discrepancies'
    )
    _describe -t options 'options' opts
}

compdef _ltlf_benchmarks src/analyze.py src/report_errors.py src/visualize.py src/cross_check.py
