# 1. 项目功能

对ISAACS分析多帧xyz轨迹文件获得的结构数据（包含最近邻和次近邻配位原子种类和数量）进行分析


# 2. 文件结构

### 1. TBO模型相关

```
01_删除当前目录下无后缀ISAACS导出文件中的表头行.py
02_基于ISAACS配位原子数百分比提取.py
02-2_基于ISAACS配位原子数百分比提取_指定列数.py
03_B-O配位数同时为3和4的聚合度分析.py
04_含Al掺杂的B最近邻和次近邻聚合度分析.py
04-2_基于最近邻O和次近邻网络形成体的团簇聚合度分析.py
05_将空格分隔的列数据保存到excel文件.py
06_将团簇分子式及占比txt数据转为xlsx文件格式.py
07_基于桥氧和总氧数提取多个txt文本中的指定大类团簇中各小类团簇百分比.py
08_基于团簇分子式及占比同时计算最近邻和次近邻平均键级.py
09_基于电负性差值计算共价键和离子键比例.py
```


### 2. g(r)和CN相关

```
01_plot_RDF.py
01-2_plot_RDF_通过序号确定文件.py
01_plot_CN.py
01-2_plot_CN_通过序号确定文件.py
01_合并RDF或CN.py
```



- `01_plot_RDF.py`：从当前目录中查找所有包含 `"origin_g(r)"` 的文件，读取其中的两列数据（x 和 y），对 x 在 0 到 6 范围内的数据进行筛选，并将每个文件的曲线绘制到同一张图上，从而比较这些文件的曲线图。

- `01-2_plot_RDF_通过序号确定文件.py`：通过交互式的方式让用户选择特定的 `"origin_g(r)"` 文件，然后读取、筛选并绘制这些文件中的数据曲线。

<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20250220-201145.png" alt="Image Description" width="450">
</p>


- `01_plot_CN.py`：自动查找所有文件名包含 `"origin_dn(r)"` 的文件，从中读取两列数据（x 和 y），对 x 值在 0 到 5 范围内的数据进行筛选，然后将每个文件对应的数据曲线绘制在同一张图上，并显示图例和其他注释信息。

- `01-2_plot_CN_通过序号确定文件.py`：首先搜索所有文件名中包含 `"origin_dn(r)"` 的文件，然后允许用户通过输入序号来选择部分文件，并对选中的文件进行数据读取和筛选，最后将每个文件中的数据绘制成曲线图并展示。

<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20250220-202002.png" alt="Image Description" width="450">
</p>

- `01_合并RDF或CN.py`：把当前目录中（除了 Python 脚本外）的所有文件中、每行恰好有两列的有效数据读取出来，然后横向整合成一个总文件 `total_data.txt`，同时生成一个日志文件 `log.txt` 记录每个文件数据来源的信息。


# 3. TBO计算流程

1. 先使用 [01_删除当前目录下无后缀ISAACS导出文件中的表头行.py](01_删除当前目录下无后缀ISAACS导出文件中的表头行.py) 对ISAACS导出的 g(r) 和 dn(r) 文件进行初步处理

2. 使用如下脚本绘制  g(r) 和 dn(r) 曲线

```
01_plot_RDF.py
01-2_plot_RDF_通过序号确定文件.py
01_plot_CN.py
01-2_plot_CN_通过序号确定文件.py
```

3. 将需要绘制到一张图中的多个 gr或者cn 数据文件放到一个目录中，使用 [01_合并RDF或CN.py](01_合并RDF或CN.py) 脚本将这些数据文件合并成一个数据文件，然后使用 origin 绘图。



# 4. 环境配置


### `09_基于电负性差值计算共价键和离子键比例.py`

- 离子键成分占比

$$
ionic = \left(1 - e^{-\frac{1}{4} (X_A - X_B)^2}\right) \times 100\%
$$


<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20241109-154408.png" alt="Image Description" width="900">
</p>



### 1. `01_删除当前目录下无后缀ISAACS导出文件中的表头行.py`

1. 功能概述：

该代码的目的是在当前目录下查找没有文件后缀的文件，读取这些文件的内容，并删除文件中以 `@` 开头的行，然后将处理后的内容保存到一个新文件中。新文件的命名格式为原文件名加上 `origin_` 前缀。

2. 主要步骤：
    - 文件筛选：使用 `os.listdir('.')` 获取当前目录下的所有文件，筛选出没有文件后缀的文件。
    - 处理文件内容：对于每一个没有文件后缀的文件，打开文件并逐行读取。如果某一行不是以 `@` 开头，则将该行写入一个新文件。
    - 新文件保存：新文件的命名是将原文件的名称加上前缀 `origin_`，并将处理后的内容保存到该新文件中。

3. 通过该方式获取到的数据文件可以：
    - 复制粘贴到origin中绘图
    - 使用python脚本快速绘图获取截断半径（可以绘制RDF和CN曲线），用于ISAACS后续的`bond properties`分析。
    - 使用`58_[47类]轨迹分析和绘图.py`脚本的`09方法`也可以基于xyz文件获取指定原子对的RDF曲线。


### 2. `02_基于ISAACS配位原子数百分比提取.py`

1. 待处理的数据示例（通常由ISAACS分析xyz轨迹文件得出）：

`example_rawdata.txt`

```
#Environments for Pt atoms:

#N(tot)   N(O )   N(Si)   N(Ca)   N(Pt)          Number   or     Percent
  4        4       0       0       0           5.50993   or      68.874 %
  5        5       0       0       0           0.77483   or       9.685 %
  3        3       0       0       0           1.29139   or      16.142 %
  2        2       0       0       0           0.42384   or       5.298 %
```

2. 功能：
    - 列出当前目录下的所有文件。
    - 读取用户指定的文件，跳过前三行，并提取第一列和倒数第二列的数据。
    - 将数据按第一列排序后输出。通常适用于最近邻配位结构，且配位原子仅有一种，特别是硅酸盐渣中 X-O 的配位结构统计分析。


3. 输出示例

```
请输入你想处理的文件名: Pt-Si_coordination.txt
5 6.291
6 26.159
7 34.768
8 22.682
9 7.533
10 2.152
11 0.414
```


### 2. `02-2_基于ISAACS配位原子数百分比提取_指定列数.py`

- 源码：[02-2_基于ISAACS配位原子数百分比提取_指定列数.py](02-2_基于ISAACS配位原子数百分比提取_指定列数.py)

- 功能：

用户选择指定文件；然后读取文件内容，跳过前三行，提取用户指定的两列数据，将第一列转换为整数、第二列转换为浮点数，并按第一列排序后输出结果。


- 适用范围：

当ISAACS输出的结构分析数据中包含次近邻配位原子种类和数量时，第一列数值则不等于最近邻配位的氧原子数，因此 `02_基于ISAACS配位原子数百分比提取.py` 脚本不再适用，需要在`02-2_基于ISAACS配位原子数百分比提取_指定列数.py` 脚本中通过交互指定氧原子所在列数以及百分比所在列数。


- 输入文件示例

```
Environments for B  atoms:

N(tot)   N(Si)   N(Al)   N(B )   N(Ca)   N(O )          Number   or     Percent
  9        2       2       1       0       4           0.16000   or       0.178 %
  7        3       1       0       0       3           1.06000   or       1.178 %
  5        1       1       0       0       3          10.14000   or      11.267 %
  6        2       1       0       0       3           6.51000   or       7.233 %
  5        2       0       0       0       3           6.86000   or       7.622 %
  7        2       1       0       0       4           6.35000   or       7.056 %
  5        0       2       0       0       3           2.96000   or       3.289 %
```


- 编程思路：

在上述 `02_基于ISAACS配位原子数百分比提取.py` 代码基础进行扩展：
1. 上述 `02_基于ISAACS配位原子数百分比提取.py` 代码中固定提取 第一列和倒数第二列数据，现在需要改成通过用户指定需要提取的两列，因此在开头需要提示用户输入需要提取的2个列数（用英文逗号分隔），列数从1开始计数，负值代表倒数的列数，例如-1代表倒数第一列，-2代表倒数第二列等。
2. 仍然需要将用户选定的第1个列值对应数据转换为整数，将用户选定的第2个列值对应数据转换为浮点数。
3. 最后仍然需要按用户选定的第1个列值的数值大小排序后输出结果。





### 3. `03_B-O配位数同时为3和4的聚合度分析.py`

1. 总体思路

```
请按照以下要求编写python代码，给出完整代码

读取脚本所在目录下的 B_isaacs.txt 数据文件，忽略前3行，其余数据（定义为数据集a0）分为若干列， 列和列之间使用空格分隔，进行如下计算：
打印出a0数据集
计算a0数据集第6列数据的和t1和第8列数据的和t2（浮点数计算），打印出来
从a0数据集中提取第5列数值为3的行（定义为a1数据集），分别计算这些行第6列数据的和x1和第8列数据的和x2（浮点数计算），打印出来；
从a0数据集中提取第5列数值为4的行（定义为b1数据集），分别计算这些行第6列数据的和y1和第8列数据的和y2（浮点数计算），打印出来；
然后分别计算a1数据集中每一行第2列和第3列数的加和az1，再选取其中 az1 小于等于3的行（定义为数据集a2），打印出来；
然后分别计算b1数据集中每一行第2列和第3列数的加和bz1，再选取其中 bz1 小于等于4的行（定义为数据集b2），打印出来；
然后分别计算数据集a2第6列数据的和x3和第8列数据的和x4（浮点数计算），打印出来，再计算并打印x1-x3和x2-x4的值；
然后分别计算数据集b2第6列数据的和y3和第8列数据的和y4（浮点数计算），打印出来，再计算并打印y1-y3和y2-y4的值；
定义k0=(x3+y3)/t1，打印出k0，打印出x3+y3，打印出x4+y4；
定义k1=x3/(x3+y3)，k2=y3/(x3+y3)，打印出 k1和k2；
再从数据集a2中选取第2列和第3列数的加和az1分别为0，1，2，3的行，分别标记为ac0，ac1，ac2，ac3数据集，分别计算这些数据集中第6列数据的和as0，as1，as2，as3，打印出这些和。计算并打印出 as0+as1+as2+as3的和；
再从数据集b2中选取第2列和第3列数的加和bz1分别为0，1，2，3，4的行，分别标记为bc0，bc1，bc2，bc3，bc4数据集，分别计算这些数据集中第6列数据的和bs0，bs1，bs2，bs3，bs4，打印出这些和。计算并打印出 bs0+bs1+bs2+bs3+bs4 的和。
分别打印出ac0，ac1，ac2，ac3数据集和bc0，bc1，bc2，bc3，bc4数据集。
然后计算并打印as0/x3*100%，as1/x3*100%，as2/x3*100%，as3/x3*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
然后计算并打印bs0/y3*100%，bs1/y3*100%，bs2/y3*100%，bs3/y3*100%，bs4/y3*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
然后计算并打印as0/(x3+y3)*100%，as1/(x3+y3)*100%，as2/(x3+y3)*100%，as3/(x3+y3)*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
然后计算并打印bs0/(x3+y3)*100%，bs1/(x3+y3)*100%，bs2/(x3+y3)*100%，bs3/(x3+y3)*100%，bs4/(x3+y3)*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
将a2和b2数据集中每一行第6列数据替换成原数据/k0，第8列数据替换成原数据/k0，小数点后保留3位有效数字，得到的新数据集分别定义为a3和b3。分别打印出数据集a3和b3。
然后分别计算数据集a3第6列数据的和x5和第8列数据的和x6（浮点数计算），打印出来。
然后分别计算数据集b3第6列数据的和y5和第8列数据的和y6（浮点数计算），打印出来。

注意：
x6=k1*100%
y6=k2*100%
x3=as0+as1+as2+as3
y3=bs0+bs1+bs2+bs3+bs4
```

2. 待处理的数据示例（通常由ISAACS分析xyz轨迹文件得出）：

`B_isaacs.txt`

```
Environments for B  atoms:

N(tot)   N(Si)   N(B )   N(Ca)   N(O )          Number   or     Percent
  8        4       0       0       4          35.05000   or      19.691 %
  8        3       1       0       4           2.05000   or       1.152 %
  7        4       0       0       3           5.20000   or       2.921 %
  6        3       0       0       3          29.71000   or      16.691 %
  5        1       1       0       3           1.24000   or       0.697 %
  6        2       1       0       3           1.37000   or       0.770 %
  7        3       0       0       4          32.26000   or      18.124 %
  4        1       0       0       3          17.99000   or      10.107 %
  5        2       0       0       3          34.32000   or      19.281 %
  6        2       0       0       4          10.24000   or       5.753 %
  3        0       0       0       3           1.75000   or       0.983 %
  7        2       1       0       4           1.75000   or       0.983 %
  6        1       1       0       4           0.27000   or       0.152 %
  9        5       0       0       4           0.91000   or       0.511 %
  5        1       0       0       4           2.09000   or       1.174 %
  7        3       1       0       3           0.57000   or       0.320 %
  8        5       0       0       3           0.40000   or       0.225 %
  9        4       1       0       4           0.04000   or       0.022 %
  4        0       1       0       3           0.34000   or       0.191 %
  8        2       2       0       4           0.21000   or       0.118 %
  4        0       0       0       4           0.07000   or       0.039 %
  5        0       1       0       4           0.02000   or       0.011 %
  8        4       1       0       3           0.03000   or       0.017 %
  7        1       2       0       4           0.05000   or       0.028 %
  6        1       2       0       3           0.02000   or       0.011 %
  5        0       2       0       3           0.02000   or       0.011 %
  6        0       2       0       4           0.01000   or       0.006 %
 10        6       0       0       4           0.01000   or       0.006 %
  7        2       2       0       3           0.01000   or       0.006 %
```



### 4. `04_含Al掺杂的B最近邻和次近邻聚合度分析.py`

1. 总体思路

```
请按照以下要求编写python代码，给出完整代码
赋值 col6 = 6，col8 = 8，col5 = 5，colist=[2, 3]
读取脚本所在目录下的 B_isaacs.txt 数据文件，忽略前3行，其余数据（定义为数据集a0）分为若干列， 列和列之间使用空格分隔，进行如下计算：
打印出a0数据集
计算a0数据集第col6列数据的和t1和第col8列数据的和t2（浮点数计算），打印出来
从a0数据集中提取第col5列数值为3的行（定义为a1数据集），分别计算这些行第col6列数据的和x1和第col8列数据的和x2（浮点数计算），打印出来；
从a0数据集中提取第col5列数值为4的行（定义为b1数据集），分别计算这些行第col6列数据的和y1和第col8列数据的和y2（浮点数计算），打印出来；
然后分别计算a1数据集中每一行指定列(数组colist中列出的所有列)数的加和az1，再选取其中 az1 小于等于3的行（定义为数据集a2），打印出来；
然后分别计算b1数据集中每一行指定列(数组colist中列出的所有列)数的加和bz1，再选取其中 bz1 小于等于4的行（定义为数据集b2），打印出来；
然后分别计算数据集a2第col6列数据的和x3和第col8列数据的和x4（浮点数计算），打印出来，再计算并打印x1-x3和x2-x4的值；
然后分别计算数据集b2第col6列数据的和y3和第col8列数据的和y4（浮点数计算），打印出来，再计算并打印y1-y3和y2-y4的值；
定义k0=(x3+y3)/t1，打印出k0，打印出x3+y3，打印出x4+y4；
定义k1=x3/(x3+y3)，k2=y3/(x3+y3)，打印出 k1和k2；
再从数据集a2中选取指定列(数组colist中列出的所有列)数的加和az1分别为0，1，2，3的行，分别标记为ac0，ac1，ac2，ac3数据集，分别计算这些数据集中第col6列数据的和as0，as1，as2，as3，打印出这些和。计算并打印出 as0+as1+as2+as3的和；
再从数据集b2中选取指定列(数组colist中列出的所有列)数的加和bz1分别为0，1，2，3，4的行，分别标记为bc0，bc1，bc2，bc3，bc4数据集，分别计算这些数据集中第col6列数据的和bs0，bs1，bs2，bs3，bs4，打印出这些和。计算并打印出 bs0+bs1+bs2+bs3+bs4的和。
分别打印出ac0，ac1，ac2，ac3数据集和bc0，bc1，bc2，bc3，bc4数据集。
然后计算并打印as0/x3*100%，as1/x3*100%，as2/x3*100%，as3/x3*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
然后计算并打印bs0/y3*100%，bs1/y3*100%，bs2/y3*100%，bs3/y3*100%，bs4/y3*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
然后计算并打印as0/(x3+y3)*100%，as1/(x3+y3)*100%，as2/(x3+y3)*100%，as3/(x3+y3)*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
然后计算并打印bs0/(x3+y3)*100%，bs1/(x3+y3)*100%，bs2/(x3+y3)*100%，bs3/(x3+y3)*100%，bs4/(x3+y3)*100%的值，小数点后保留2位有效数字。计算并打印出这几个百分比的求和。
将a2和b2数据集中每一行第col6列数据替换成原数据/k0，第col8列数据替换成原数据/k0，小数点后保留3位有效数字，得到的新数据集分别定义为a3和b3。分别打印出数据集a3和b3，。
然后分别计算数据集a3第col6列数据的和x5和第col8列数据的和x6（浮点数计算），打印出来。
然后分别计算数据集b3第col6列数据的和y5和第col8列数据的和y6（浮点数计算），打印出来。
```


- 各参数含义：
  - `col6` 代表杂质原子数的`Number`列
  - `col8` 代表杂质原子百分比的`Percent`列
  - `col5` 代表氧原子配位数`N(O )`所在列
  - `colist` 列表中是所有杂质原子次近邻配位的（如网络形成体原子，不考虑碱土金属原子）所在列，会计算每一行中这些列的原子数加和，并与该行的O原子数对比，如果小于等于，则符合条件。
  - `cluster` 字典中应该包含所有最近邻原子（如O），和次近邻配位原子（考虑的网络形成体原子）的所在列数，用于构建团簇的分子式
  - `col5_list` 列表（后续脚本增加的）中包含合法的O原子配位数值，例如对于B为[3,4]，对于过渡金属原子，可能包含更多的O配位数值



2. 体系中不含Al体系（CaO-SiO2-B2O3）

```
Environments for B  atoms:

N(tot)   N(Si)   N(B )   N(Ca)   N(O )          Number   or     Percent
  8        4       0       0       4          35.05000   or      19.691 %
  8        3       1       0       4           2.05000   or       1.152 %
  7        4       0       0       3           5.20000   or       2.921 %
  6        3       0       0       3          29.71000   or      16.691 %
```

- 环境变量

```py
# 定义cluster字典，键为元素符号，值为对应的列数（列数等于列的索引+1）
cluster = {"Si": 2, "B": 3, "O": 5}

# 定义变量，将列数转换为索引
# Number，B原子数所在列，该列求和为体系所有B原子数
col6 = 6 - 1                
# Percent，百分比所在列
col8 = 8 - 1
# N(O )，O原子配位数所在列
col5 = 5 - 1
# N(Si)   N(B ) 等所在列，修改列表 [2, 3]
colist = [c - 1 for c in [2, 3]]  # 列数转为索引
```

需要修改的环境变量包括 `Number Percent O` 以及 `Si B` 所在的列数


3. 体系中含Al体系（CaO-SiO2-Al2O3-B2O3）

```
Environments for B  atoms:

N(tot)   N(Si)   N(Al)   N(B )   N(Ca)   N(O )          Number   or     Percent
  6        3       0       0       0       3           8.88000   or       9.867 %
  6        0       1       1       0       4           0.01000   or       0.011 %
  5        2       0       0       0       3          14.99000   or      16.656 %
  7        3       0       0       0       4          10.28000   or      11.422 %
  8        4       0       0       0       4          10.60000   or      11.778 %
```

- 环境变量

```py
# 定义cluster字典，键为元素符号，值为对应的列数（列数等于列的索引+1）
cluster = {"Si": 2, "Al": 3, "B": 4, "O": 6}

# 定义变量，将列数转换为索引
# Number，B原子数所在列，该列求和为体系所有B原子数
col6 = 7 - 1                
# Percent，百分比所在列
col8 = 9 - 1
# N(O )，O原子配位数所在列
col5 = 6 - 1
# N(Si)   N(B ) 等所在列，修改列表 [2, 3]
colist = [c - 1 for c in [2, 3, 4]]  # 列数转为索引
```

需要修改的环境变量包括 `Number, Percent, O` 以及 `Si, Al, B` 所在的列数


4. 输出文件示例

```
a3 data (sorted by az1 ascending and col8 descending with cluster_combo):
    0  1  2  3  4       5   6       7  8  az1 cluster_combo
10  3  0  0  0  3   1.823  or   1.024  %    0            O3
7   4  1  0  0  3  18.745  or  10.531  %    1         Si1O3
......
5   6  2  1  0  3   1.428  or   0.802  %    3       Si2B1O3
24  6  1  2  0  3   0.021  or   0.011  %    3       Si1B2O3
b3 data (sorted by bz1 ascending and col8 descending with cluster_combo):
    0  1  2  3  4       5   6       7  8  bz1 cluster_combo
20  4  0  0  0  4   0.073  or   0.041  %    0            O4
14  5  1  0  0  4   2.178  or   1.223  %    1         Si1O4
......
19  8  2  2  0  4   0.219  or   0.123  %    4       Si2B2O4
x5: 90.401, x6: 50.78600000000001
y5: 87.59800000000001, y6: 49.211000000000006
```



### 4. `04-2_基于最近邻O和次近邻网络形成体的团簇聚合度分析.py`

- 源码：[04-2_基于最近邻O和次近邻网络形成体的团簇聚合度分析.py](04-2_基于最近邻O和次近邻网络形成体的团簇聚合度分析.py)

1. 功能：分析具有多个氧原子配位数的中心原子聚合度（不局限于X-O配位数仅为3和4两种情况，次近邻配位的网络形成体原子种类不局限于Si、B、Al等）

- 编程思路1：

```
上述代码 `04_含Al掺杂的B最近邻和次近邻聚合度分析.py` 是正常工作的，但是我现在需要进行扩展：
1. 上述代码中在构造a1和b1系列数据集时，只是考虑了col5列数值为3的行（a1数据集）和col5列数值为4的行（b1数据集）。如果用户还需要同时计算col5列数值为其他值时，还需要构造c1，d1等系列数据集。因此可以在代码开头手动初始化一个列表，列表中是a1，b1，c1等系列数据集构造时col5列数值对应的值，如 [3, 4, 5, 6]，如果列表中的数值不存在于col5列中，可以给出提示并结束代码运行。注意也需要像a1和b1数据集一样，同步计算和打印其他数据集的 [col6].sum()、[col8].sum()值。
2. 对于 a1，b1，c1等系列数据集，需要计算 数据集中每一行指定列（colist中的列）的加和az1，bz1，cz1等，并与各数据集在构造时对应的col5列数值进行对比，进而来构造a2、b2、c2等数据集。在上述代码中，az1和bz1对比的数值分别是3和4。
3. 对于 a2、b2、c2等系列数据集，仍然需要计算和打印[col6].sum()、[col8].sum()值，并仿照上述代码计算差值和比例等。
4. 其余部分功能需要和上述代码一致，新代码的扩展主要体现在使用列表来指定多个数据集的创建，对于创建后的数据集的计算仍然要参考按上述初始代码，确保功能不变。
输出出修改后的完整代码
```

- 新增思路2：

```
上述修改后的代码是正常工作的，但是我需要其新增打印出一部分过程数据/信息，分析如下：
1. 上述代码在`"=== 全部 2 系列数据集统计 ==="`下已经打印出了一些关键信息 ，包括 k0，配位数为不同 {val} 的比例，以及col5为确定值且z1为不同值时，sum(col6)的值。
2. 现在我的需求是，除了打印出col5为确定值且 z1为不同值时，sum(col6)的值外，还需要打印出clo5为确定值且z1为不同值时，2系列数据集中相应行的数据（例如 clo5为3时，z1分别取0-3时，每个z1下包含哪些行 ），以便用户可以核查。另外，之后还需要输出clo5为确定值且 z1为不同值时，col8的和（例如 clo5为3时，z1取2时，所含行的col8的和），注意：col8的和需要分为两种，一种是未使用k0归一化前的（即通过初始输出数据的col8相应行求和得到），以及归一化后的（采用k0变换后的，类似data3中的col8变换）。新增部分的输出请放在  `"配位数 {val} 的比例 = {ratio_val:.4f}"`  之后，放在 `"=== data2(col5={val}) 的 z1={0}~{val} 分组统计 ==="` 之前。
3. 其余部分功能保持不变，如`"=== data3(col5={val}) === (按 {z1_name} 升序, col8 降序)` 等后续输出内容保持不变。
输出修改后的完整代码
```


2. 输入文件示例：体系中不含Al体系（CaO-SiO2-B2O3）

```
Environments for B  atoms:

N(tot)   N(Si)   N(B )   N(Ca)   N(O )          Number   or     Percent
  8        4       0       0       4          35.05000   or      19.691 %
  8        3       1       0       4           2.05000   or       1.152 %
  7        4       0       0       3           5.20000   or       2.921 %
  6        3       0       0       3          29.71000   or      16.691 %
```

- 环境变量：

```py
# 定义 cluster 字典，键为元素符号，值为对应的列数（列数等于列的索引+1）
cluster = {"Si": 2, "B": 3, "O": 5}

# 将列数转换为索引
col6 = 6 - 1  # B原子数所在列
col8 = 8 - 1  # 百分比所在列
col5 = 5 - 1  # O原子配位数所在列
# 指定要对比计算的列（例如 N(Si), N(Al), N(B) 等），其所在列数减1后得到索引
colist = [c - 1 for c in [2, 3]]

# 手动指定需要处理的 col5 值列表
# 假设我们想同时处理 O 原子配位数 = 3、4、5、6 的行
col5_list = [3, 4]
```


需要修改的环境变量包括 `Number Percent O` 、`Si B` 所在的列数 以及 中心原子配位的氧原子数列表 `col5_list`


3. 输入文件示例：体系中含Al体系（CaO-SiO2-Al2O3-B2O3）

```
Environments for B  atoms:

N(tot)   N(Si)   N(Al)   N(B )   N(Ca)   N(O )          Number   or     Percent
  6        3       0       0       0       3           8.88000   or       9.867 %
  6        0       1       1       0       4           0.01000   or       0.011 %
  5        2       0       0       0       3          14.99000   or      16.656 %
  7        3       0       0       0       4          10.28000   or      11.422 %
  8        4       0       0       0       4          10.60000   or      11.778 %
```

- 环境变量：

```py
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
col5_list = [3, 4]
```

需要修改的环境变量包括 `Number, Percent, O`、`Si, Al, B` 所在的列数 以及 中心原子配位的氧原子数列表 `col5_list`



### 5. `05_将空格分隔的列数据保存到excel文件.py`

- 功能：读取脚本所在目录下的 `B_isaacs.txt` 数据文件，忽略前三行，剩下的数据包含若干列，列和列之间使用空格分隔，将剩余数据写入到 `B_isaacs.xlsx` 数据文件中，使得txt文件中的每列数据在xlsx文件中也为1列。

```py
import pandas as pd

# 读取B_isaacs.txt文件，跳过前3行，并指定空格作为分隔符
df = pd.read_csv('B_isaacs.txt', sep='\s+', skiprows=3, header=None)

# 将数据写入B_isaacs.xlsx文件
df.to_excel('B_isaacs.xlsx', index=False, header=False)

print("数据已成功写入B_isaacs.xlsx文件。")
```


### 6. `06_将团簇分子式及占比txt数据转为xlsx文件格式.py`

- 功能：打印脚本所在目录下的所有文件名，提示用户输入文件名。逐行读取文件，逐行判断，如果该行含有`%`，则保留该行数据，每一行的多列之间使用空格分隔，最后将所有含有%的行写入到 `xlsx` 文件中，仍然使用原文件名。

txt格式的数据文件：`团簇百分比及分子式.txt`

```
a3 data (sorted by az1 ascending and col8 descending with cluster_combo):
    0  1  2  3  4  5       6   7       8  9  az1 cluster_combo
52  3  0  0  0  0  3   0.752  or   0.427  %    0            O3
81  6  0  2  1  0  3   0.424  or   0.241  %    3       Al2B1O3
63  6  1  0  2  0  3   0.133  or   0.076  %    3       Si1B2O3
b3 data (sorted by bz1 ascending and col8 descending with cluster_combo):
    0  1  2  3  4  5       6   7      8  9  bz1 cluster_combo
92  4  0  0  0  0  4   0.024  or  0.013  %    0            O4
42  8  3  0  1  0  4   1.067  or  0.606  %    4       Si3B1O4
50  8  0  4  0  0  4   0.824  or  0.468  %    4         Al4O4
86  8  1  1  2  0  4   0.024  or  0.013  %    4    Si1Al1B2O4
x5: 94.88400000000001, x6: 53.914
y5: 81.113, y6: 46.083
```

注意：生成的xlsx文件中，默认各列数据都是文本格式，excel可以直接转为数据格式。在排序过程中2，注意包含第一列数据，避免其不参与排序的问题。

<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20241029-091144.png" alt="Image Description" width="900">
</p>


### 7. `07_基于桥氧和总氧数提取多个txt文本中的指定大类团簇中各小类团簇百分比.py`

- 使用python编写脚本实现以下功能：
   - 脚本所在目录下有好几个txt数据文本，这些文本中含有好多行，每行含有多列，列和列之间使用空格分隔，只读取含有%的行，把每个文本中的这部分数据命名为data。data每行列数一定是相同的，如果不相同，给出提示，并结束程序运行，后续运算都是基于data数据。
   - 请依次读取这些data数据，首先为每个data数据构建一个字典，字典的键是data每行的最后一列（已确定data最后一列不会重复，如果重复请提示并结束），每个键的值是一个列表list，列表的元素依次是该行的倒数第7列值（list[0]），倒数第2列值（list[1]）和倒数第4列值（list[2]）。
   - 提示用户依次输入两个整数BO和TO，现在查找每个字典中同时满足 `list[0]=TO` 和 `list[1]=BO` 的键，并记录该键对应的 `list[2]`。
   - 最后请按照如下表格格式打印结果，并将结果以表格形式保存到xlsx文件中，命名为 `TO-BO.xlsx`。注意满足要求的部分键可能在一部分文本中存在，另外一部分文本中没有，没有时可以使用0作为替代。
   - 注意，如果某个键对应的行值全为0，则该行不需要打印，也不需要写入到xlsx文件中；在写入的excel文件中，能不能再重复写入一组转置后的的数据，即文本行作为列，键列作为行

- 新增功能：将键值中的元素符号和对应数字转换为指定格式，以便用于origin绘图。
   - 在转置后的数据表格中再新增一行，该行首先复制 键 对应的行，该行含有多个键，每个键都是由元素符号和数字组成，例如 键`"Si1Al1B2O4"`是由 `Si1 Al1 B2 O4`，这4部分构成，现在需要根据一定的规则将这个键转化成另外一种形式。
   - 注意每个键中，最多含有四种元素符号，分别是 `Si，Al，B，O`， 每个元素后紧邻的对应数字分别为`a，b，c，d`；最少含有一种元素符号。 
   - 首先计算，`x= d-a-b-c`，将键中原有的Si替换成`(SiO\-(4))`，将 Al 替换成 `(AlO\-(4))`，将B替换成 `(BO\-(3))`。注意新组成的键的格式为 `"B"+"O\-(x)"+"(BO\-(3))\-(c)"+"(AlO\-(4))\-(b)"+"(SiO\-(4))\-(a)"`。如果 `a，b，c，x` 中有值为0，则包含该值的 `" "` 相应部分要删除，例如b=0，则 `"(AlO\-(4))\-(b)"` 部分删除掉，若x=0，`"O\-(x)"`删掉，以此类推；
   - 如果 `a，b，c，x` 中有值为1，只需要将对应的`"\-()"`部分删除掉即可，例如 c=1，则 `"(BO\-(3))\-(c)"` 部分变成 `"(BO\-(3))"，b=1，"(AlO\-(4))\-(b)"`变成`(AlO\-(4))"`，对于 `a，b，c，x` 取非0和非1值，则按照   `"B"+"O\-(x)"+"(BO\-(3))\-(c)"+"(AlO\-(4))\-   - (b)"+"(SiO\-(4))\-(a)"` 格式的字符串拼接输出。

```
        文本1       文本2      文本3       文本4      ...
键1  list[2]       list[2]     list[2]        list[2]      ...
键2    ...
键3    ...
键4
...
```

注意：每个输入文本中包含了一个体系的各类团簇百分比，是`04_含Al掺杂的B最近邻和次近邻聚合度分析.py`的输出文件。每个输入文件的参考格式和内容如下：

```
a3 data (sorted by az1 ascending and col8 descending with cluster_combo):
    0  1  2  3  4       5   6       7  8  az1 cluster_combo
10  3  0  0  0  3   1.823  or   1.024  %    0            O3
7   4  1  0  0  3  18.745  or  10.531  %    1         Si1O3
......
5   6  2  1  0  3   1.428  or   0.802  %    3       Si2B1O3
24  6  1  2  0  3   0.021  or   0.011  %    3       Si1B2O3
b3 data (sorted by bz1 ascending and col8 descending with cluster_combo):
    0  1  2  3  4       5   6       7  8  bz1 cluster_combo
20  4  0  0  0  4   0.073  or   0.041  %    0            O4
14  5  1  0  0  4   2.178  or   1.223  %    1         Si1O4
......
19  8  2  2  0  4   0.219  or   0.123  %    4       Si2B2O4
x5: 90.401, x6: 50.78600000000001
y5: 87.59800000000001, y6: 49.211000000000006
```




### 8. `08_基于团簇分子式及占比同时计算最近邻和次近邻平均键级.py`

- 源码：[08_基于团簇分子式及占比同时计算最近邻和次近邻平均键级.py](08_基于团簇分子式及占比同时计算最近邻和次近邻平均键级.py)

- 使用python编写脚本实现以下功能：
   - 脚本所在目录下有好几个txt数据文本，这些文本中含有好多行，每行含有多列，列和列之间使用空格分隔，只读取含有%的行，把每个文本中的这部分数据命名为data。data每行列数一定是相同的，如果不相同，给出提示，并结束程序运行，后续运算都是基于data数据。
   - 请依次读取这些data数据，首先为每个data数据构建一个字典，字典的键是data每行的最后一列（已确定data最后一列不会重复，如果重复请提示并结束），每个键的值是一个列表list，列表的元素依次是该行的倒数第7列值（list[0]），倒数第2列值（list[1]）和倒数第4列值（list[2]）。
   - 每个键都是由元素符号和数字组成，例如 键`"Si1Al1B2O4"`是由 `Si1 Al1 B2 O4`，这4部分构成，现在需要根据一定的规则从这个键获取一些信息。
   - 注意每个键中，最多含有四种元素符号，分别是 `B，Si，Al，O`， 每个元素后紧邻的对应数字分别为`a，b，c，d`；最少含有一种元素符号。`i，j，k，l`是4个常数，在程序的开头分别赋值为`i=1.16，j=1.14，k=0.657，l=0.186`。
   - 对于每个键，首先计算，`x= d-a-b-c`，然后计算每个键的v值和w值，`v=0.01*list[2]*(a*i + b*j + c*k + x*l)`， `w=0.01**list[2]*(1.16*d)` 。对于每个data，将所有键的v值求和得到`sv`，将所有键的w值求和得到`sw`，打印出每个文本对应的sv和sw，并将每个文本的sv和sw写入到xlsx文件中，命名为 `"最近邻和次近邻_MBO_sum.xlsx"`。


注意：`08脚本`的输入文件与`07脚本`相同，都是`04_含Al掺杂的B最近邻和次近邻聚合度分析.py`的输出文件。





