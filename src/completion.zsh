# Zsh autocomplete for LTLf Benchmarks
_ltlf_benchmarks() {
    local -a jobs tools_a tools_b
    local results_dir="/home/cowclaw/results_shards/data/results"
    
    # Get all directory names in the results folder (Job IDs)
    if [[ -d $results_dir ]]; then
        jobs=($(ls -1 $results_dir))
    fi

    # Helper to get tools from a specific job id argument on the command line
    # Usage: _get_tools_for_job <job_id_val>
    _get_tools_for_job() {
        if [[ -n $1 && -d "$results_dir/$1" ]]; then
            echo $(ls -1 "$results_dir/$1")
        fi
    }

    case $words[1] in
        *analyze.py|*report_errors.py|*visualize.py)
            _arguments \
                '--job-id[The Job ID to process]:job id:($jobs)' \
                '--results-dir[Path to results]:directory:_files -/' \
                '*::files:_files'
            ;;
        *cross_check.py)
            # Find what jobs are already on the command line to narrow tool choices
            local job_a_val=${words[$words[(i)--job-a]+1]}
            local job_b_val=${words[$words[(i)--job-b]+1]}
            
            [[ $job_a_val != "--job-a" ]] && tools_a=($(_get_tools_for_job $job_a_val))
            [[ $job_b_val != "--job-b" ]] && tools_b=($(_get_tools_for_job $job_b_val))

            _arguments \
                '--job-a[First Job ID]:job id:($jobs)' \
                '--job-b[Second Job ID]:job id:($jobs)' \
                '--tool-a[First Tool Name]:tool name:($tools_a)' \
                '--tool-b[Second Tool Name]:tool name:($tools_b)' \
                '--output[Save conflicts to CSV]:file:_files' \
                '*::files:_files'
            ;;
    esac
}

# Register the completion for the scripts
compdef _ltlf_benchmarks src/analyze.py src/report_errors.py src/visualize.py src/cross_check.py
