#!/bin/bash

# 获取当前目录
current_dir=$(pwd)

# 创建一个空的 step_scf.txt 文件
output_file="$current_dir/step_scf.txt"
> "$output_file"

# 用来保存临时数据
scf_converged=""
md_step=""

# 遍历 tem.out 文件
while IFS= read -r line; do
    # 检查 "SCF run converged in" 行
    if [[ "$line" =~ SCF[[:space:]]*run[[:space:]]*converged[[:space:]]*in[[:space:]]+([0-9]+)[[:space:]]*steps ]]; then
        # 提取 SCF run converged in 的数值
        scf_converged="${BASH_REMATCH[1]}"
    fi

    # 检查 "MD| Step number" 行
    if [[ "$line" =~ MD\|[[:space:]]*Step[[:space:]]*number[[:space:]]+([0-9]+) ]]; then
        # 提取 MD| Step number 的数值
        md_step="${BASH_REMATCH[1]}"
        # 如果同时获得了 SCF 和 MD 信息，就写入到 step_scf.txt
        if [[ -n "$scf_converged" && -n "$md_step" ]]; then
            echo "$md_step $scf_converged" >> "$output_file"
            # 重置临时数据
            scf_converged=""
            md_step=""
        fi
    fi
done < "tem.out"

echo "数据已写入到 $output_file"
