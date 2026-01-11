import os
import csv
import glob
from collections import defaultdict

def extract_errors(results_dir):
    path_pattern = os.path.join(results_dir, "**", "test_*.csv")
    shard_files = glob.glob(path_pattern, recursive=True)
    
    # tool -> error_type -> [tests]
    errors = defaultdict(lambda: defaultdict(list))
    
    for filepath in sorted(shard_files):
        filename = os.path.basename(filepath)
        # Filename format: test_<impl>_<method>_shard_<num>.csv
        parts = filename.replace('.csv', '').split('_')
        if len(parts) < 3: continue
        impl = parts[1]
        method = parts[2]
        tool = f"{impl}_{method}"
        
        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    status = int(float(row['status']))
                    if status == -1:
                        errors[tool]['Error'].append(row['test'])
                    elif status == -2:
                        errors[tool]['Timeout'].append(row['test'])
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    return errors

def get_label(impl, mode):
    if impl == 'lucas':
        if mode == 'belief-states': return "l_bst"
        elif mode == 'projection-based': return "l_prj"
        elif mode == 'belief': return "l_bel" # Legacy
        elif mode == 'direct': return "l_dir" # Legacy
        elif mode == 'mso': return "l_mso"
        else: return f"l_{mode[:3]}"
    else:
        if mode == 'belief': return "c_bel"
        elif mode == 'direct': return "c_dir"
        elif mode == 'mso': return "c_mso"
        else: return f"c_{mode[:3]}"

if __name__ == "__main__":
    results_dir = "/home/cowclaw/results_shards/results"
    errors = extract_errors(results_dir)
    
    # Process into labeled errors
    labeled_errors = defaultdict(lambda: defaultdict(list))
    for tool_key, types in errors.items():
        parts = tool_key.split('_')
        impl = parts[0]
        mode = "_".join(parts[1:])
        label = get_label(impl, mode)
        for err_type, tests in types.items():
            labeled_errors[label][err_type].extend(tests)

    print("Error Test List for Debugging (Status -1 only)")
    print("==============================================")
    
    for label in sorted(labeled_errors.keys()):
        errs = labeled_errors[label].get('Error', [])
        if not errs:
            continue
            
        print(f"\n### {label} ({len(errs)} errors)")
        for test in sorted(set(errs)):
            print(f"  {test}")
