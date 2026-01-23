# Zsh autocomplete for LTLf Benchmarks
_ltlf_benchmarks() {
    local results_dir="/home/cowclaw/results_shards/data/results"
    local label_file="/home/cowclaw/results_shards/data/job_labels.json"
    
    # 1. Load Job IDs and Labels safely
    local -A labels
    local -a job_ids
    if [[ -d "$results_dir" ]]; then
        job_ids=($(ls -1 "$results_dir" | grep -E '^[0-9]+$'))
        if [[ -f "$label_file" ]]; then
            # Load labels into an associative array
            while IFS= read -r line; do
                labels[${line%%:*}]="${line#*:}"
            done <<< "$(python3 -c "import json; d=json.load(open('$label_file')); [print(f'{k}:{v}') for k,v in d.items()]" 2>/dev/null)"
        fi
    fi

    local cur="$words[CURRENT]"
    local active_opt=""
    local i
    # Find the most recent persistent flag
    for ((i=CURRENT-1; i>0; i--)); do
        if [[ "$words[i]" == --* ]]; then
            active_opt="$words[i]"
            break
        fi
    done

    local -a display_list val_list

    case "$active_opt" in
        --job-id|--job-a|--job-b)
            if [[ "$cur" == *-* ]]; then
                # Handle JOB_ID-tool completion
                local jid="${cur%%-*}"
                local filter="${cur#*-}"
                if [[ -d "$results_dir/$jid" ]]; then
                    for t in $(ls -1 "$results_dir/$jid"); do
                        local t_val="${t/_/:}"
                        if [[ -z "$filter" || "$t_val" == *"$filter"* ]]; then
                            val_list+=("$jid-$t_val")
                            display_list+=("$jid-$t_val")
                        fi
                    done
                    compadd -U -d display_list -a val_list
                    return
                fi
            fi

            # Regular Job ID completion
            local id desc
            for id in $job_ids; do
                desc="${labels[$id]}"
                if [[ -z "$cur" || "$id" == *"$cur"* || "${(L)desc}" == *"${(L)cur}"* ]]; then
                    val_list+=("$id")
                    if [[ -n "$desc" ]]; then
                        display_list+=("${(r:10:)id} -- $desc")
                    else
                        display_list+=("$id")
                    fi
                fi
            done
            compadd -U -d display_list -a val_list
            return
            ;;
        --tool-a|--tool-b)
            local job_val=""
            local i
            # Look for corresponding job-a or job-b
            local target_job="--job-a"
            [[ "$active_opt" == "--tool-b" ]] && target_job="--job-b"
            
            for ((i=CURRENT-1; i>0; i--)); do
                if [[ "$words[i]" == "$target_job" || "$words[i]" == "--job-id" ]]; then
                    job_val="$words[i+1]"
                    job_val="${job_val%%-*}"
                    break
                fi
            done
            
            if [[ -n "$job_val" && -d "$results_dir/$job_val" ]]; then
                local -a tools
                for t in $(ls -1 "$results_dir/$job_val"); do
                    tools+=("${t/_/:}")
                done
                _describe -t tools 'tools' tools
                return
            fi
            ;;
    esac

    local -a opts
    opts=(
        '--job-id:Job identifier(s) (supports JOB_ID-tool:mode)'
        '--label:Custom label(s) for the jobs'
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
