import pandas as pd
import os

def calc_Min_Max(filename):

    # 读取txt文件，假设文件名为data.txt
    df = pd.read_csv(filename, sep='\t', header=None, na_values='--')

    # 打印每列的最大值和最小值
    for column in df.columns:
        max_value = df[column].max()
        min_value = df[column].min()
        print(f"列 {column + 1}: 最大值 = {max_value}, 最小值 = {min_value}")



if __name__ == '__main__':
    # 获取当前文件夹下的所有文件名
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # 打印文件名（不包括子文件夹）
    for file in files:
        print(file)

    # 测试示例
    filename = input("请输入数据文件名: ")
    calc_Min_Max(filename)
