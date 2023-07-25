# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:17:56 2023

@author: sun78
"""
import os

def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Filter and retain valid lines
    valid_lines = []
    discarded_lines = []
    valid_firstElement = []
    
    for line in lines:
        data = line.split()
        a_b = data[0].split(':')
        a, b = int(a_b[0]), int(a_b[1])
        

        if a == b:
            discarded_lines.append(line)
        else:
            # Check if the reverse order exists
            # reverse_line = f"{b}:{a} {data[1]} {data[2]}\n"
            reverse_line = str(b)+':'+str(a)
            
            if reverse_line not in valid_firstElement:
                
                valid_lines.append(line)
                valid_firstElement.append(data[0])
                
            else:
                discarded_lines.append(line)

    # Write the valid lines to the output file
    with open(output_file, 'w') as f:
        f.writelines(valid_lines)

    # Write the total number of valid lines
    with open(output_file, 'a') as f:
        f.write(f"\n--- Total Valid Lines: {len(valid_lines)} ---\n")

        # Write a line separator
        f.write("----------------------\n")

        # Write the discarded lines and count
        f.writelines(discarded_lines)
        f.write(f"--- Total Discarded Lines: {len(discarded_lines)} ---\n")


if __name__ == "__main__":
    
    # 获取当前文件夹下的所有文件名
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # 打印文件名（不包括子文件夹）
    for file in files:
        print(file)
    
    # 提示用户输入txt文件名
    input_file = input('请输入要处理的txt文件名,如 bondOrder_Si-Si.txt: ')

    # input_file = "your_input_file.txt"  # Replace with the actual file name
    output_file = "bondOrder_retain.txt"  # The output file to save the filtered data
    process_data(input_file, output_file)
    print("输出的数据保存在 bondOrder_retain.txt 文件中")
