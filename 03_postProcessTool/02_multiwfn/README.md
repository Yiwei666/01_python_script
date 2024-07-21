# 1. 项目功能

可视化multiwfn输出的数据文件

# 2. 文件结构



### 1. `01_NCI_plot.py`

- 源码：[01_NCI_plot.py](01_NCI_plot.py)
- 功能：读取multiwfn NCI 分析输出的output.txt文件，选取第4列和第5列作为x和y绘制散点图，x属于[-0.05,0.05]，y属于[0,2]，对于x属于[-0.05,0.05]，使用颜色渐变，色系是`rainbow`。
