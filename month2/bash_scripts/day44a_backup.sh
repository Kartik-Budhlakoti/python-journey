#!/bin/bash

# Validate arguments
if [ $# -ne 2 ];then
    echo "Usage: $0 <source> <destination>"
    echo "Example: $0 /home/kartik007/Desktop/python-new/python-journey/month2/bash_scripts  /home/kartik007/Desktop/python-new/python-journey/month2"
    exit 1
fi
source_dir=$1
dest_dir=$2

# Validate source exists
if [ ! -d "$source_dir"]; then
    echo "Error: source directory doesn't exist: $source_dir"
    exit 1
fi

# Create destination if doesn't exist
if [ ! -d "$dest_dir" ];then
    mkdir -p "$dest_dir"
    echo "Created the destination $dest_dir"
fi

#  the folder is with the timestamps
timestamp=$(date +%Y%m%d_%H%M%S)
backup_name="backup_$timestamp"
backup_path="$dest_dir/$backup_name"

# now creating the backup
echo "Starting backup..."
echo "Source : $source_dir"
echo "Destination : $dest_dir"

# excluding .venv and .git
count=0
for file in "$source_dir"/*.py "$source_dir"/*.md "$source_dir"/*.txt ; do
    if [ -f "$file" ]; then
        cp "$file" "$dest_dir/"
        echo "  Backed up : $(basename $file)"
        count=$((count + 1))
    fi
done

echo "Backup complete. $count files backed up."
echo "BACKUP_PATH=$backup_path"
exit 0