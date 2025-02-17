import pandas as pd
import sys

# ============= 1. 参数初始化 =============

# 定义 cluster 字典，键为元素符号，值为对应的列数（列数等于列的索引+1）
cluster = {"Si": 2, "Al": 3, "B": 4, "O": 6}

# 将列数转换为索引
col6 = 7 - 1  # B原子数所在列
col8 = 9 - 1  # 百分比所在列
col5 = 6 - 1  # O原子配位数所在列
# 指定要对比计算的列（例如 N(Si), N(Al), N(B) 等），其所在列数减1后得到索引
colist = [c - 1 for c in [2, 3, 4]]

# 手动指定需要处理的 col5 值列表
# 假设我们想同时处理 O 原子配位数 = 3、4、5、6 的行
col5_list = [3, 4, 5, 6]

# 读取数据文件，忽略前3行
data = pd.read_csv('B_isaacs.txt', sep='\s+', skiprows=3, header=None)

# ============= 2. 基础统计：a0（全部数据） =============
print("=== 全部数据（a0） ===")
print(data)

# 计算体系中第 col6 列 (B原子数) 的总和 t1 和 第 col8 列 (百分比) 的总和 t2
t1 = data[col6].sum()
t2 = data[col8].sum()
print(f"[全部数据] B原子数之和 (t1): {t1}, 百分比之和 (t2): {t2}\n")

# ============= 3. 检查 col5_list 中的值是否都存在 =============
unique_col5_values = data[col5].unique()
for val in col5_list:
    if val not in unique_col5_values:
        print(f"错误：在列 col5 中未找到数值 {val}，程序结束。")
        sys.exit(1)

# ============= 4. 动态构造 1 系列和 2 系列数据集，并计算差值等 =============

# 用于存储各个子数据集以及各种统计值
data1_dict = {}  # 存储 a1, b1, c1... 之类的原始子集
data2_dict = {}  # 存储 a2, b2, c2... 之类的筛选后子集

sum1_dict = {}   # 对应 x1, y1, z1... (col6 的和)
sum2_dict = {}   # 对应 x2, y2, z2... (col8 的和)
sum3_dict = {}   # 对应 x3, y3, z3... (col6 的和)
sum4_dict = {}   # 对应 x4, y4, z4... (col8 的和)

# 对于每个 col5 值，比如 3、4、5、6，生成对应 data1, data2
for idx, val in enumerate(col5_list):
    # 1）构造 data1 子集：筛选 col5 == val 的行
    subset_1 = data[data[col5] == val].copy()
    data1_dict[val] = subset_1

    # 计算 col6 和 col8 的和（类似 x1、x2、y1、y2 等）
    sum_col6_1 = subset_1[col6].sum()
    sum_col8_1 = subset_1[col8].sum()
    sum1_dict[val] = sum_col6_1
    sum2_dict[val] = sum_col8_1

    print(f"=== 数据集 {idx+1}（col5 = {val}）=== ")
    print(subset_1)
    print(f"[col5={val}] sum_col6_1: {sum_col6_1}, sum_col8_1: {sum_col8_1}")

    # 2）构造 data2 子集
    #    - 先计算 z1 = 指定列 colist 的加和
    #    - 只保留 z1 <= val 的行（对应 a2、b2、c2... 的逻辑）
    z1_name = f"z1_{val}"  # 每个配位数对应一个 z1 列名，避免冲突
    subset_1[z1_name] = subset_1[colist].sum(axis=1)

    subset_2 = subset_1[subset_1[z1_name] <= val].copy()
    data2_dict[val] = subset_2

    # 计算 col6 和 col8 的和（类似 x3、x4、y3、y4 等）
    sum_col6_2 = subset_2[col6].sum()
    sum_col8_2 = subset_2[col8].sum()
    sum3_dict[val] = sum_col6_2
    sum4_dict[val] = sum_col8_2

    print(f"--- data2 (col5={val}, z1 <= {val}) ---")
    print(subset_2)
    print(f"[col5={val}] sum_col6_2: {sum_col6_2}, sum_col8_2: {sum_col8_2}")

    # 3）打印差值（和初始代码类似 x1 - x3, x2 - x4）
    print(f"差值: (sum_col6_1 - sum_col6_2) = {sum_col6_1 - sum_col6_2}, "
          f"(sum_col8_1 - sum_col8_2) = {sum_col8_1 - sum_col8_2}\n")

# ============= 5. 计算 k0, k1, k2, ... 及相关统计 =============

# （在原代码中只针对 a2, b2 计算了 k0、k1、k2。
#  如果希望扩展到 c2、d2... 就需要将它们都包含在总和里。下面的思路是“将所有 data2 的 B原子数之和”做分母或分子。）
total_sum3 = sum(sum3_dict[val] for val in col5_list)  # 相当于 (x3 + y3 + z3 + ...)
total_sum4 = sum(sum4_dict[val] for val in col5_list)  # 相当于 (x4 + y4 + z4 + ...)

# 定义 k0 = (所有 2 系列数据集的 col6 之和) / (a0 的 col6 之和)，即 total_sum3 / t1
k0 = total_sum3 / t1 if t1 != 0 else 0

print("=== 全部 2 系列数据集统计 ===")
print(f"所有 2 系列数据集之和 sum_col6: {total_sum3}, sum_col8: {total_sum4}")
print(f"k0 = total_sum3 / t1 = {k0:.4f}")

# 计算并打印每个配位数所占的比例 k(val) = sum3[val] / total_sum3
# （原来的 k1, k2 是 x3 / (x3+y3), y3 / (x3+y3)；现扩展为多组）
for val in col5_list:
    if total_sum3 != 0:
        ratio_val = sum3_dict[val] / total_sum3
    else:
        ratio_val = 0
    print(f"配位数 {val} 的比例 = {ratio_val:.4f}")
print()

# ============= 6. 进一步细分（类似 as0, as1, as2, as3 以及 bs0, bs1...） =============
# 这里原先只做了 a2, b2 的分组统计，现在扩展到对所有 data2_dict[val] 做同样处理。
# 对于 col5 = val 的 data2，需要按 z1 从 0 到 val 来分组（与原始代码思路相同）。

for val in col5_list:
    subset_2 = data2_dict[val]
    z1_name = f"z1_{val}"
    # 分别计算 z1=0,1,2,...,val 的行里 col6 的和
    group_sums = []
    print(f"=== data2(col5={val}) 的 z1={0}~{val} 分组统计 ===")
    for i in range(val + 1):
        part_df = subset_2[subset_2[z1_name] == i]
        sum_part = part_df[col6].sum()
        group_sums.append(sum_part)
        print(f"z1={i}, sum(col6)={sum_part}")

    print(f"总和 = {sum(group_sums)}\n")

# ============= 7. 生成 3 系列数据集（a3, b3, c3...），并对 col6, col8 做归一化、生成 cluster_combo 字段等 =============
# 这里原先代码是：a3 = a2.copy(); a3[col6]/=k0, a3[col8]/=k0, 然后 round(3)，然后生成 cluster_combo。
# 现在我们给每个 val 对应生成 data3[val]。

data3_dict = {}

def generate_cluster_combo(row):
    """根据 cluster 字典，对非零的列值拼接符号。"""
    combo_parts = []
    for key, col_num in cluster.items():
        # col_num 是列数，因此索引 = col_num - 1
        val_ = int(row[col_num - 1])
        if val_ != 0:
            combo_parts.append(f"{key}{val_}")
    return "".join(combo_parts)

for val in col5_list:
    subset_2 = data2_dict[val].copy()
    # 先做归一化
    if k0 != 0:
        subset_2[col6] = (subset_2[col6] / k0).round(3)
        subset_2[col8] = (subset_2[col8] / k0).round(3)
    else:
        # 防止 k0=0 的情况
        subset_2[col6] = subset_2[col6].round(3)
        subset_2[col8] = subset_2[col8].round(3)

    # 生成 cluster_combo
    subset_2["cluster_combo"] = subset_2.apply(generate_cluster_combo, axis=1)

    # 按 z1_{val} 升序、col8 降序排序
    z1_name = f"z1_{val}"
    subset_2_sorted = subset_2.sort_values(by=[z1_name, col8], ascending=[True, False])
    data3_dict[val] = subset_2_sorted

    # 打印结果
    print(f"=== data3(col5={val}) === (按 {z1_name} 升序, col8 降序)")
    print(subset_2_sorted)

    # 计算并打印 x5, x6 (即此 data3 的 col6, col8 之和)
    x5 = subset_2_sorted[col6].sum()
    x6 = subset_2_sorted[col8].sum()
    print(f"[data3(col5={val})] x5(col6之和)={x5}, x6(col8之和)={x6}\n")

# =============（后续如有需要，可以继续扩展）=============

print("=== 处理结束 ===")
