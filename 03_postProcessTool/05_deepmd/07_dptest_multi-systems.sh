#!/usr/bin/env bash
set -euo pipefail

# Activate DeepMD‑kit Python environment
source /public21/home/sc90511/deepmd-kit/bin/activate

# Directory containing validation data subfolders
VAL_DIR="../00.data/validation_data"

# Output file (will append results)
OUTPUT_FILE="dptest.out"

# Iterate over each first‑level subdirectory in VAL_DIR
for subdir in "$VAL_DIR"/*/; do
    if [ -d "$subdir" ]; then
        echo "=== Testing system: ${subdir##*/} ===" >> "$OUTPUT_FILE"
        dp test -m graph.pb -s "$subdir" >> "$OUTPUT_FILE" 2>&1
        echo "" >> "$OUTPUT_FILE"
    fi
done
