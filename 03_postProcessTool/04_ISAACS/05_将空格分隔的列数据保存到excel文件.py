import pandas as pd

# 读取B_isaacs.txt文件，跳过前3行，并指定空格作为分隔符
df = pd.read_csv('B_isaacs.txt', sep='\s+', skiprows=3, header=None)

# 将数据写入B_isaacs.xlsx文件
df.to_excel('B_isaacs.xlsx', index=False, header=False)

print("数据已成功写入B_isaacs.xlsx文件。")
