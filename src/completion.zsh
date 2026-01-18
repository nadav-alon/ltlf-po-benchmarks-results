# Zsh autocomplete for LTLf Benchmarks
_ltlf_benchmarks() {
    local results_dir="/home/cowclaw/results_shards/data/results"
    local label_file="/home/cowclaw/results_shards/data/job_labels.json"
    
    # 1. Load Job IDs and Labels safely
    local -a jobs
    if [[ -d "$results_dir" ]]; then
        local raw
        raw=$(python3 -c "
import json, os
res_dir = '$results_dir'
lbl_file = '$label_file'
labels = {}
if os.path.exists(lbl_file):
    try:
        with open(lbl_file) as f: labels = json.load(f)
    except: pass
for j in sorted(os.listdir(res_dir)):
    if os.path.isdir(os.path.join(res_dir, j)):
        d = labels.get(j, '').replace(':', ' ')
        print(f'{j}:{d}' if d else j)
" 2>/dev/null)
        # Split into array by line
        while IFS= read -r line; do
            [[ -n "$line" ]] && jobs+=("$line")
        done <<< "$raw"
    fi

    # 2. Check what flag we are completing for
    local prev="$words[CURRENT-1]"
    
    case "$prev" in
        --job-id|--job-a|--job-b)
            _describe -t jobs 'job ids' jobs
            return
            ;;
        --tool-a|--tool-b)
            # Find the associated job ID on the command line
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

    # 3. Default: Complete the flags themselves
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
