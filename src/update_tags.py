#!/usr/bin/env python3
import os
import json
import shutil
from pathlib import Path

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPTS_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
TAGS_FILE = os.path.join(DATA_DIR, "tags.json")
RESULTS_DIR = os.path.join(DATA_DIR, "results")
LOGS_DIR = os.path.join(DATA_DIR, "logs")

def update_symlinks(base_path, tags):
    tags_dir = os.path.join(base_path, "tags")
    
    # Create tags directory if it doesn't exist
    if not os.path.exists(tags_dir):
        os.makedirs(tags_dir)
        print(f"Created {tags_dir}")
    else:
        # Clean up existing tags to avoid conflicts (e.g., symlink vs directory)
        for item in os.listdir(tags_dir):
            item_path = os.path.join(tags_dir, item)
            if os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    
    for tag, job_input in tags.items():
        job_ids = job_input if isinstance(job_input, list) else [job_input]
        dst_path = os.path.join(tags_dir, tag)
        
        if len(job_ids) == 1:
            job_id = job_ids[0]
            src_dir = os.path.join(base_path, job_id)
            if os.path.exists(src_dir):
                os.symlink(os.path.abspath(src_dir), dst_path)
                print(f"Created link: {tag} -> {job_id}")
            else:
                print(f"Warning: Job directory {src_dir} (tag: {tag}) not found.")
        else:
            os.makedirs(dst_path, exist_ok=True)
            for job_id in job_ids:
                src_dir = os.path.join(base_path, job_id)
                dst_link = os.path.join(dst_path, job_id)
                if os.path.exists(src_dir):
                    os.symlink(os.path.abspath(src_dir), dst_link)
                else:
                    print(f"Warning: Job directory {src_dir} (tag: {tag}, id: {job_id}) not found.")
            print(f"Created tag directory for {tag} with {len(job_ids)} jobs.")

def main():
    if not os.path.exists(TAGS_FILE):
        print(f"Error: {TAGS_FILE} not found.")
        return

    with open(TAGS_FILE, 'r') as f:
        tags = json.load(f)

    print("Updating results tags...")
    update_symlinks(RESULTS_DIR, tags)
    
    print("\nUpdating logs tags...")
    update_symlinks(LOGS_DIR, tags)

if __name__ == "__main__":
    main()
