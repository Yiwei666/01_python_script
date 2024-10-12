import pandas as pd

# 定义变量，将列数转换为索引
# Number，B原子数所在列，该列求和为体系所有B原子数
col6 = 6 - 1                
# Percent，百分比所在列
col8 = 8 - 1
# N(O )，O原子配位数所在列
col5 = 5 - 1
# N(Si)   N(B ) 等所在列，修改列表 [2, 3]
colist = [c - 1 for c in [2, 3]]  # 列数转为索引

# 读取脚本所在目录下的B_isaacs.txt数据文件，忽略前3行
data = pd.read_csv('B_isaacs.txt', sep='\s+', skiprows=3, header=None)

# 打印a0数据集
print("a0 data:")
print(data)

# 计算a0数据集第col6列和第col8列的和 t1 和 t2
t1 = data[col6].sum()
t2 = data[col8].sum()
print(f"t1: {t1}, t2: {t2}")

# 从a0数据集中提取第col5列数值为3的行（a1数据集），并计算x1和x2
a1 = data[data[col5] == 3]
x1 = a1[col6].sum()
x2 = a1[col8].sum()
print(f"x1: {x1}, x2: {x2}")

# 从a0数据集中提取第col5列数值为4的行（b1数据集），并计算y1和y2
b1 = data[data[col5] == 4]
y1 = b1[col6].sum()
y2 = b1[col8].sum()
print(f"y1: {y1}, y2: {y2}")

# 计算a1数据集中每一行指定列（colist中的列）的加和az1，并选取az1小于等于3的行（a2数据集）
a1['az1'] = a1[colist].sum(axis=1)
a2 = a1[a1['az1'] <= 3]
print("a2 data:")
print(a2)

# 计算b1数据集中每一行指定列（colist中的列）的加和bz1，并选取bz1小于等于4的行（b2数据集）
b1['bz1'] = b1[colist].sum(axis=1)
b2 = b1[b1['bz1'] <= 4]
print("b2 data:")
print(b2)

# 计算a2第col6列和第col8列的和x3和x4，打印x1-x3和x2-x4
x3 = a2[col6].sum()
x4 = a2[col8].sum()
print(f"x3: {x3}, x4: {x4}")
print(f"x1 - x3: {x1 - x3}, x2 - x4: {x2 - x4}")

# 计算b2第col6列和第col8列的和y3和y4，打印y1-y3和y2-y4
y3 = b2[col6].sum()
y4 = b2[col8].sum()
print(f"y3: {y3}, y4: {y4}")
print(f"y1 - y3: {y1 - y3}, y2 - y4: {y2 - y4}")

# 定义k0 = (x3 + y3) / t1，打印k0，打印x3 + y3和x4 + y4
k0 = (x3 + y3) / t1
print(f"k0: {k0}")
print(f"x3 + y3: {x3 + y3}, x4 + y4: {x4 + y4}")

# 定义k1和k2，打印k1和k2
k1 = x3 / (x3 + y3)
k2 = y3 / (x3 + y3)
print(f"k1: {k1}, k2: {k2}")

# 从a2中选取az1分别为0，1，2，3的行，计算as0，as1，as2，as3，打印并计算总和
as_list = []
for i in range(4):
    ac = a2[a2['az1'] == i]
    as_ = ac[col6].sum()
    as_list.append(as_)
    print(f"as{i}: {as_}")
print(f"as0 + as1 + as2 + as3: {sum(as_list)}")

# 从b2中选取bz1分别为0，1，2，3，4的行，计算bs0，bs1，bs2，bs3，bs4，打印并计算总和
bs_list = []
for i in range(5):
    bc = b2[b2['bz1'] == i]
    bs_ = bc[col6].sum()
    bs_list.append(bs_)
    print(f"bs{i}: {bs_}")
print(f"bs0 + bs1 + bs2 + bs3 + bs4: {sum(bs_list)}")

# 分别打印ac0，ac1，ac2，ac3数据集和bc0，bc1，bc2，bc3，bc4数据集
for i in range(4):
    ac = a2[a2['az1'] == i]
    print(f"ac{i} data:")
    print(ac)

for i in range(5):
    bc = b2[b2['bz1'] == i]
    print(f"bc{i} data:")
    print(bc)

# 计算并打印百分比
for i in range(4):
    print(f"as{i}/x3*100%: {as_list[i]/x3*100:.2f}%")
print(f"sum of percentages: {sum([as_/x3*100 for as_ in as_list]):.2f}%")

for i in range(5):
    print(f"bs{i}/y3*100%: {bs_list[i]/y3*100:.2f}%")
print(f"sum of percentages: {sum([bs_/y3*100 for bs_ in bs_list]):.2f}%")

# 计算并打印加权百分比
for i in range(4):
    print(f"as{i}/(x3+y3)*100%: {as_list[i]/(x3+y3)*100:.2f}%")
print(f"sum of percentages: {sum([as_/(x3+y3)*100 for as_ in as_list]):.2f}%")

for i in range(5):
    print(f"bs{i}/(x3+y3)*100%: {bs_list[i]/(x3+y3)*100:.2f}%")
print(f"sum of percentages: {sum([bs_/(x3+y3)*100 for bs_ in bs_list]):.2f}%")

# 替换a2和b2中的第col6列和第col8列数据，定义为a3和b3，保留3位小数
a3 = a2.copy()
a3[col6] = (a3[col6] / k0).round(3)
a3[col8] = (a3[col8] / k0).round(3)
print("a3 data (sorted by az1):")
print(a3.sort_values(by='az1'))

b3 = b2.copy()
b3[col6] = (b3[col6] / k0).round(3)
b3[col8] = (b3[col8] / k0).round(3)
print("b3 data (sorted by bz1):")
print(b3.sort_values(by='bz1'))

# 分别计算a3第col6列的和x5和第col8列的和x6，打印出来
x5 = a3[col6].sum()
x6 = a3[col8].sum()
print(f"x5: {x5}, x6: {x6}")

# 分别计算b3第col6列的和y5和第col8列的和y6，打印出来
y5 = b3[col6].sum()
y6 = b3[col8].sum()
print(f"y5: {y5}, y6: {y6}")
