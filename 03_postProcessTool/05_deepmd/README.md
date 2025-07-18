# a. 项目功能

针对deepmd-kit进行深度势能训练的数据处理脚本

# b. 文件结构

```py
01_extract_poscar-from-vmd_frames.py             # vmd导出的poscar文件标准化及指定帧提取
02_frc_unit_converter_hartree_bohr.py            # frc.xyz文件单位转换
03_extract_xyz_every_n_frames.py                 # xyz文件每10帧提取一帧
04_plot_lcurve.py                                # X 轴和 Y 轴都用对数刻度（plt.loglog），适合同时跨越大范围的步数和损失值
04-2_xyPlot_lcurve.py                            # X、Y 轴均为线性刻度（plt.plot），用于数据变化幅度较小且接近线性的情况
04-3_ySemi_plot_lcurve.py                        # X 轴线性、Y 轴对数刻度（plt.semilogy），强调损失值的指数级变化，而保留步数的线性分布
05-1_plot_energy_correlation.py                  # 能量预测，该脚本在超算上进行绘图，绘图前请加载 deepmd-kit 虚拟环境
05-2_plot_force_correlation.py                   # 力(xyz分量)预测，该脚本在超算上进行绘图，绘图前请加载 deepmd-kit 虚拟环境
06-1_split_cp2k_multi-trajectories_o3_one-process.py              # 适用于多个体系/组分训练集和验证集的划分，所有体系中均满足 print_level 为medium，且frc单位为 hartree/bohr
06-2_split_cp2k_multi-trajectories_mix_N_systems_Si-slag.py       # 适用于多个体系/组分训练集和验证集的划分，部分体系可以为 print_level low，且frc单位可以为 [amu·Å/fs²]，但在调用本脚本前需转换。注意：1 [amu·Å/fs²] = 2.015529556643 [Hartree/Bohr]
```




# 1. 01_extract_poscar-from-vmd_frames.py

[01_extract_poscar-from-vmd_frames.py](01_extract_poscar-from-vmd_frames.py)

- vmd导出的poscar文件标准化及指定帧提取

## 1. vmd输出poscar数据格式

```
B   O   Si  Ca  
      1.000000000000
     14.875200271606        0.000000000000        0.000000000000
      0.000000000000       14.875200271606        0.000000000000
      0.000000000000        0.000000000000       14.875200271606
 8  135  40  43 
Direct
      0.324629924852       0.882626102256       0.598300539987 
      0.789967070951       0.599929361733       0.317764043058 
      0.729609627730       0.101514779862       0.645540473778 
      0.661922871322       0.918706113140       0.684908517098 
      0.051849785110       0.098404000236       0.491051033038 
      0.428460739728       0.341228346756       0.857410459362 
      ...
      0.497273169294       0.747559171569       0.408897504504 
      0.667677408923       0.220784348258       0.290419314854 
      0.235927066022       0.090740761280       0.813329180605 
      0.875539708284       0.144658328898       0.924219270206 
B   O   Si  Ca  
      1.000000000000
     14.875200271606        0.000000000000        0.000000000000
      0.000000000000       14.875200271606        0.000000000000
      0.000000000000        0.000000000000       14.875200271606
 8  135  40  43 
Direct
      0.325318676801       0.883975268785       0.599541357750 
      0.789858914520       0.600849749240       0.317666272722 
      0.730018916797       0.101273198977       0.644143992817 
      0.662715676553       0.919356526295       0.684786063759 
      0.052275406632       0.098939677498       0.491217018219 
      0.427974388403       0.341230526553       0.856245421624 
      0.607148338693       0.517345483440       0.890189936028 
      ...
      0.235929309931       0.090390390862       0.813695514836 
      0.875653570656       0.143907709162       0.924109190424 
B   O   Si  Ca  
      1.000000000000
     14.875200271606        0.000000000000        0.000000000000
      0.000000000000       14.875200271606        0.000000000000
      0.000000000000        0.000000000000       14.875200271606
 8  135  40  43 
Direct
      0.325991785497       0.885430796617       0.600835388220 
      0.789693185786       0.601703973476       0.317604757549 
      0.730377237065       0.101011438937       0.642726867891 
      0.663513738944       0.919983154011       0.684655019452 
      0.052674261520       0.099442593682       0.491433523416 
      ...
      0.875821415076       0.143196197561       0.924089508134 
...
```


## 2. 编程思路

我有一个vmd导出的多帧 poscar 文件（部分内容如上所示），我想要提取其中的某些帧分别保存为单独的poscar文件，能否帮我编写一个python脚本实现上述功能？需求如下：
1. 打印当前目录（不含子目录）下的所有文件名，提示用户输入需要处理的数据文件名（提示用户：vmd导出的poscar文件）
2. 该poscar文件中，每一帧的原子数相同，因此统计 Direct (或Cartesian) 关键词的数量就可以知道该poscar文件中的帧数。通过判断相邻两个Direct (或Cartesian) 关键词间隔的行数就可以知道不同帧的原子数是否相同
3. 基于文件的总行数除以总帧数，就可以得到每帧的行数（必须满足整除，否则可能不同帧原子数不同），基于此就可以确定每帧的起始和结束行数
4. 打印文件的总帧数。提示用户输入想要提取的帧数，支持如下2种方式：
   - 输入具体帧数的索引，使用英文逗号分隔，使用"-"代表范围，例如：0,10,15,99,150-155,200，其中150-155代表从150到155的帧数索引。
   - 指定帧数范围a到b，每隔c提取一帧，类似于python的range函数，即list(range(a,b,c))列表中的帧数索引，提示用户输入a,b,c三个数，使用英文逗号分隔
5. 在提取前打印出用户输入的帧数索引及总数，请用户输入y进行确认
6. 按照 `index_"对应索引"_POSCAR` 方式命名，将相应帧写入到对应文件中。注意各帧写入时，应当将各帧第一行内容复制，然后插入到第6行，原第6及之后的行要各自后移一行，以满足现在poscar文件的要求（第6行是元素符号）




# 2. 02_frc_unit_converter_hartree_bohr.py

[02_frc_unit_converter_hartree_bohr.py](02_frc_unit_converter_hartree_bohr.py)

- frc.xyz文件单位转换

## 1. 编程思路

1. 打印当前目录下的所有文件名（不含子文件夹中的文件），提示用户输入需要读取的文件名（通常是 `*.frc.xyz` 文件）。
2. 读取该文件的所有行，从第一行开始遍历，如果该行包含4列，列和列之间使用空格分隔，且第一列为字符串，后三列为数值，则需要将后三列的数值分别乘以一个系数，该系数是 2.015529557777。这是因为，该文件中默认这三列的单位是 `amu·Å/fs²`，乘以该系数后，单位转换为 `Hartree/Bohr`，转换后的数值应当与转换前的数值具有相同的小数位数（小数点后保留10位）。
3. 进行一致性检验，检索文档中字符"time"出现的次数a，计数文档非空行的总行数b，计数文档中需要进行数值转换的行数为c。如果a，b和c满足 `2*a+c=b`一致性检验，则进行上述数值转换，否则结束程序运行，并给出提示。
4. 完成上述数值转换后，保存到新文件 "Hartree-Bohr_"+原文件名。



# 3. 03_extract_xyz_every_n_frames.py

[03_extract_xyz_every_n_frames.py](03_extract_xyz_every_n_frames.py)

- xyz文件每10帧提取一帧

## 1. 编程思路

编写一个python脚本，实现以下需求：

1. 打印当前目录下的所有文件名（不含子文件夹中的文件），提示用户输入需要读取的文件名（通常是 `*.xyz` 文件）。
2. 由于该文件是一个多帧的xyz文件，并且每一帧的原子数相同，均为文件第一行的数值（假设为a）。因此，第1帧行数范围是 [1,a+2]，第2帧行数范围是 [a+3,2*(a+2)]，第i帧的行数范围是 [(i-1)*(a+2)+1,i*(a+2)]，请确认第i帧的行数范围计算是否正确。
3. 现在需要每n帧提取一帧，提示用户输入参数n，输入Enter默认为n为10，打印参数n的值。假如文件共有30帧，如果n为10，则提取第10，20，30帧。打印提取的总帧数b。
4. 将提取的相应帧写入到 0-b_every_10th_line.xyz 文件中。




# 4. lcurve.out 绘图

### 1. `04_plot_lcurve.py`

X 轴和 Y 轴都用对数刻度（plt.loglog），适合同时跨越大范围的步数和损失值。


<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20250626-092217.png" alt="Image Description" width="500">
</p>



### 2. `04-2_xyPlot_lcurve.py`

X、Y 轴均为线性刻度（plt.plot），用于数据变化幅度较小且接近线性的情况。


<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20250626-092251.png" alt="Image Description" width="500">
</p>




### 3. `04-3_ySemi_plot_lcurve.py`

X 轴线性、Y 轴对数刻度（plt.semilogy），强调损失值的指数级变化，而保留步数的线性分布。

<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20250626-092309.png" alt="Image Description" width="500">
</p>




# 5. 能量和力(xyz分量)预测/单体系


## 1. `05-1_plot_energy_correlation.py`

注意：该脚本在超算上进行绘图，绘图前请加载 deepmd-kit 虚拟环境

1. 从 DeepMD 格式的数据集中读取 DFT 能量，并使用训练好的深度势模型（graph.pb）对能量进行预测。

2. 将真实 DFT 能量与预测能量绘制散点图，添加 y=x 参考线后保存为 `energy_scatter.png`。

<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20250626-102622.png" alt="Image Description" width="500">
</p>




## 2. `05-2_plot_force_correlation.py`

注意：该脚本在超算上进行绘图，绘图前请加载 deepmd-kit 虚拟环境

1. 同样读取 DeepMD 数据并对力张量进行预测，然后将每个原子在 x、y、z 三个方向上的参考力与预测力分别展开为一维数组。

2. 针对每个分量绘制散点图并添加 y=x 参考线，标注单位、标题后保存为对应的 `force_x_scatter.png、force_y_scatter.png、force_z_scatter.png`。

<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20250626-102637.png" alt="Image Description" width="500">
</p>





# 6. 多条aimd轨迹转换


## 1. `06-1_split_cp2k_multi-trajectories_o3_one-process.py `

[06-1_split_cp2k_multi-trajectories_o3_one-process.py ](06-1_split_cp2k_multi-trajectories_o3_one-process.py )

适用于多个体系/组分训练集和验证集的划分，所有体系中均满足 print_level 为medium，且frc单位为 hartree/bohr


### 1. 编程思路

- 单条xyz轨迹划分脚本

```py
import dpdata
import numpy as np

# 1. 读取 CP2K AIMD 输出并统计总帧数
data = dpdata.LabeledSystem('./', cp2k_output_name='tem.out', fmt='cp2kdata/md')
total_frames = len(data)
print(f'# 原始数据包含 {total_frames} 帧')

# 2. 随机抽取 20 帧作为验证集索引（不重复）
index_validation = np.random.choice(total_frames, size=20, replace=False)
print(f'# 验证集索引（共 {len(index_validation)} 帧）：{sorted(index_validation)}')

# 3. 其余帧中每隔 5 帧提取 1 帧作为训练集索引
remaining = sorted(set(range(total_frames)) - set(index_validation))
index_training = remaining[::5]
print(f'# 训练集索引（共 {len(index_training)} 帧）：{index_training}')

# 4. 根据索引拆分子系统
data_training   = data.sub_system(index_training)
data_validation = data.sub_system(index_validation)

# 5. 保存为 DeepMD-kit 格式
data_training.to_deepmd_npy('./00.data/training_data')
data_validation.to_deepmd_npy('./00.data/validation_data')

print(f'# 训练数据包含 {len(data_training)} 帧，已保存到 "./00.data/training_data"')
print(f'# 验证数据包含 {len(data_validation)} 帧，已保存到 "./00.data/validation_data"')
```


上述python脚本是使用dpdata/cp2kdata提取tem.out等文件中的原子坐标、力、能量等信息，转化为deepmd-kit支持的npy格式，并划分训练集和验证集。上述脚本假设tem.out等文件位于当前目录下，且只包含单条xyz轨迹文件信息(因为仅包含一个路径和tem.out文件)。现在我想要针对多个轨迹文件进行训练集和验证集的划分、合并，下面有两个相关、可以作为参考的脚本：




- [多条轨迹划分脚本](https://docs.deepmodeling.com/projects/dpdata/en/stable/systems/multi.html)

```py
from dpdata import LabeledSystem, MultiSystems
from glob import glob

"""
process multi systems
"""
fs = glob("./*/OUTCAR")  # remeber to change here !!!
ms = MultiSystems()
for f in fs:
    try:
        ls = LabeledSystem(f)
    except:
        print(f)
    if len(ls) > 0:
        ms.append(ls)

ms.to_deepmd_raw("deepmd")
ms.to_deepmd_npy("deepmd")
```





- [多条轨迹划分脚本](https://github.com/deepmodeling/dpdata/issues/378)

```py
from dpdata import System, LabeledSystem, MultiSystems
import numpy as np

####### 读入轨迹 #######
ls1=LabeledSystem('./Walker_0', cp2k_output_name='cp2k.log', fmt="cp2kdata/md")
ls2=LabeledSystem('./Walker_1', cp2k_output_name='cp2k.log', fmt="cp2kdata/md")
ls3=LabeledSystem('./Walker_2', cp2k_output_name='cp2k.log', fmt="cp2kdata/md")

####### 验证集结构数 #######
#a1 = np.random.choice(len(ls1),size=30,replace=False) #随机选100个作测试集
a2 = np.random.choice(len(ls2),size=30,replace=False)
a3 = np.random.choice(len(ls3),size=40,replace=False)

####### 训练集结构数 #######
#w1 = list(set(range(1,len(ls1)))-set(a1))[10:-1:30]
w2 = list(set(range(1,len(ls2)))-set(a2))[10:-1:15]
w3 = list(set(range(1,len(ls3)))-set(a3))[10:-1:15]

####### 训练集 #######
ms= MultiSystems()
#ms.append(ls1.sub_system(w1))
ms.append(ls2.sub_system(w2))
ms.append(ls3.sub_system(w3))

ms.to_deepmd_raw('deepmd')
ms.to_deepmd_npy('deepmd',set_size=5000)

#print('There are %d frames for training' % len(ls1.sub_system(w1)))
print('There are %d frames for training' % len(ls2.sub_system(w2)))
print('There are %d frames for training' % len(ls3.sub_system(w3)))

####### 测试集 #######
v= MultiSystems()
#v.append(ls1.sub_system(a1))
v.append(ls2.sub_system(a2))
v.append(ls3.sub_system(a3))

v.to_deepmd_raw('deepmd_validation')
v.to_deepmd_npy('deepmd_validation',set_size=300)

#print('There are %d frames for validation' % len(ls1.sub_system(a1)))
print('There are %d frames for validation' % len(ls2.sub_system(a2)))
print('There are %d frames for validation' % len(ls3.sub_system(a3)))
```




- 现在需要修改上述脚本，需求如下：

1. 现在有两条轨迹，分别位于两个目录 dir1 和 dir2，2个tem.out文件也分别位于这两个目录下
```
dir1 = 'C:\Users\sun78\Desktop\cp2k_model\80-1_B-slag_dpmd'
dir2 = 'C:\Users\sun78\Desktop\cp2k_model\80_B-slag\deepmd_aimd\non-equilib-initial-config\5000-steps'
```

2. 分别打印出两个目录下的轨迹都包含多少帧。

3. dir1 随机抽取 25 帧作为验证集索引（不重复），dir2 随机抽取 35 帧作为验证集索引（不重复），打印出每条轨迹验证集帧数。

4. dir1 其余帧中每 6 帧提取 1 帧作为训练集索引，dir2其余帧中每 8 帧提取 1 帧作为训练集索引，打印出每条轨迹训练集帧数。

5. 根据索引拆分子系统，分别将dir1和dir2中的验证集合并到一起，dir1和dir2中的训练集合并到一起。

6. 保存为 DeepMD-kit 格式。并打印出训练数据包含帧数，验证数据包含帧数，以及相应保存路径。


注意：请采用变量赋值的方式管理代码（tem.out所在路径，单条轨迹验证集索引帧数，提取训练集所隔帧数等），提高其可移植性和扩展性，确保代码不仅仅适用于两条轨迹的划分转换，也可以适用于多条轨迹的转换划分。



### 2. 环境变量

- 需要根据实际情况修改的参数

```py
# ----- 用户可配置参数 -----
trajectory_dirs = [
    r"C:\Users\sun78\Desktop\cp2k_model\80-1_B-slag_dpmd",
    r"C:\Users\sun78\Desktop\cp2k_model\80_B-slag\deepmd_aimd\non-equilib-initial-config\5000-steps"
]
cp2k_output_name = "tem.out"         # 每条轨迹的 CP2K 输出文件名
fmt = "cp2kdata/md"                  # dpdata 格式
validation_counts = [25, 35]         # 对应每条轨迹的验证集帧数
training_intervals = [6, 8]          # 对应每条轨迹的训练集抽帧间隔
random_seed = 42                     # 随机种子，保证可复现
```


- 输出目录树结构

```
├── training_data
    ├── B42O136Si24Ca25
        ├── set.000
            ├── box.npy
            ├── coord.npy
            ├── energy.npy
            └── force.npy
        ├── type.raw
        └── type_map.raw
    └── B8O135Si40Ca43
        ├── set.000
            ├── box.npy
            ├── coord.npy
            ├── energy.npy
            └── force.npy
        ├── type.raw
        └── type_map.raw
└── validation_data
    ├── B42O136Si24Ca25
        ├── set.000
            ├── box.npy
            ├── coord.npy
            ├── energy.npy
            └── force.npy
        ├── type.raw
        └── type_map.raw
    └── B8O135Si40Ca43
        ├── set.000
            ├── box.npy
            ├── coord.npy
            ├── energy.npy
            └── force.npy
        ├── type.raw
        └── type_map.raw
```



## 2. `06-2_split_cp2k_multi-trajectories_mix_N_systems_Si-slag.py`

[06-2_split_cp2k_multi-trajectories_mix_N_systems_Si-slag.py](06-2_split_cp2k_multi-trajectories_mix_N_systems_Si-slag.py)

适用于多个体系/组分训练集和验证集的划分，部分体系可以为 print_level low，且frc单位可以为 [amu·Å/fs²]，但在调用本脚本前需转换。注意：1 [amu·Å/fs²] = 2.015529556643 [Hartree/Bohr]


### 1. 编程思路


`06-1_split_cp2k_multi-trajectories_o3_one-process.py` 脚本如下

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Multi‐trajectory DeepMD‑kit data preparation:
– 分别读取多个 CP2K AIMD 输出（tem.out）轨迹
– 随机抽取指定帧数作为验证集
– 按指定间隔抽取训练集
– 合并各轨迹的训练/验证子系统
– 保存为 DeepMD‑kit 支持的 npy 格式
"""

import os
import numpy as np
from dpdata import LabeledSystem, MultiSystems

# ----- 用户可配置参数 -----
trajectory_dirs = [
    r"C:\Users\sun78\Desktop\cp2k_model\80-1_B-slag_dpmd",
    r"C:\Users\sun78\Desktop\cp2k_model\80_B-slag\deepmd_aimd\non-equilib-initial-config\5000-steps"
]
cp2k_output_name = "tem.out"         # 每条轨迹的 CP2K 输出文件名
fmt = "cp2kdata/md"                  # dpdata 格式
validation_counts = [100, 100]         # 对应每条轨迹的验证集帧数
training_intervals = [10, 10]          # 对应每条轨迹的训练集抽帧间隔
random_seed = 42                     # 随机种子，保证可复现

training_out_dir = "./00.data/training_data"
validation_out_dir = "./00.data/validation_data"

# 检查参数长度一致性
assert len(trajectory_dirs) == len(validation_counts) == len(training_intervals), \
    "trajectory_dirs、validation_counts、training_intervals 三个列表长度必须相同"

# 创建输出目录
os.makedirs(training_out_dir, exist_ok=True)
os.makedirs(validation_out_dir, exist_ok=True)

# 初始化 MultiSystems 容器
ms_train = MultiSystems()
ms_validation = MultiSystems()

# 计数器，用于最终汇总
total_train_frames = 0
total_validation_frames = 0

# 固定随机种子
np.random.seed(random_seed)

for traj_dir, val_count, interval in zip(trajectory_dirs, validation_counts, training_intervals):
    # 1. 读取单条轨迹
    ls = LabeledSystem(traj_dir, cp2k_output_name=cp2k_output_name, fmt=fmt)
    total_frames = len(ls)
    print(f"# 轨迹目录: {traj_dir}")
    print(f"# 总帧数: {total_frames}")

    # 2. 随机抽取验证集索引
    val_idx = np.random.choice(total_frames, size=val_count, replace=False)
    val_idx_sorted = sorted(val_idx)
    print(f"# 验证集索引（共 {len(val_idx_sorted)} 帧）：{val_idx_sorted}")

    # 3. 剩余帧中按间隔抽取训练集索引
    remaining = sorted(set(range(total_frames)) - set(val_idx))
    train_idx = remaining[::interval]
    print(f"# 训练集索引（每隔 {interval} 帧，共 {len(train_idx)} 帧）：{train_idx}\n")

    # 累加计数
    total_validation_frames += len(val_idx)
    total_train_frames += len(train_idx)

    # 4. 拆分并添加到 MultiSystems
    ms_validation.append(ls.sub_system(val_idx))
    ms_train.append(ls.sub_system(train_idx))

# 5. 保存为 DeepMD‑kit npy 格式
ms_train.to_deepmd_npy(training_out_dir)
ms_validation.to_deepmd_npy(validation_out_dir)

# 6. 打印最终汇总
print(f"# 训练数据包含 {total_train_frames} 帧，已保存到 \"{training_out_dir}\"")
print(f"# 验证数据包含 {total_validation_frames} 帧，已保存到 \"{validation_out_dir}\"")
```


上述`06-1_split_cp2k_multi-trajectories_o3_one-process.py`脚本适用于 均采用 `ls = LabeledSystem(traj_dir, cp2k_output_name=cp2k_output_name, fmt=fmt)` 命令读取单条轨迹的情况，如果还有另外一条或者多条轨迹采用如下方式读取，上述代码该如何修改呢？下面是两外两条采用其他方式读取。

```py
import os
import dpdata
import numpy as np

cp2kmd_dir = r"C:\Users\sun78\Desktop\cp2k_model\63_SiB\dpdata-temp"
cp2kmd_output_name = None

cells = np.array([[9.34477,0,0],
                [0,9.34477,0],
                [0,0,9.34477]])
dp = dpdata.LabeledSystem(cp2kmd_dir, cp2k_output_name=cp2kmd_output_name, cells=cells, ensemble_type="NVT", fmt="cp2kdata/md")
```


```py
import os
import dpdata
import numpy as np

cp2kmd_dir = r"C:\Users\sun78\Desktop\cp2k_model\64_B2O3\dpdata-temp"
cp2kmd_output_name = None

cells = np.array([[9.402,0,0],
                [0,9.402,0],
                [0,0,9.402]])
dp = dpdata.LabeledSystem(cp2kmd_dir, cp2k_output_name=cp2kmd_output_name, cells=cells, ensemble_type="NVT", fmt="cp2kdata/md")
```


如何将上述轨迹读取方式整合到最上面的python代码中，使得python代码具有更好的健壮性，支持更多的轨迹读取方式呢？输出修改后的完整代码。



### 2. 环境变量

注意修改：

- `traj_dir`  日志、轨迹等文件所在路径
- `val_count` 验证集帧数
- `interval`  除掉验证集外提取一帧训练集间隔的帧数，需提前计算好训练集大小
- `cells`     盒子边长，针对`print level`为`low`的情况，往往需要将frc单位提前转换



```py
# ----- 用户可配置参数 -----
trajectory_configs = [
    # 普通 CP2K 输出轨迹
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\80-1_B-slag_dpmd",
        "cp2k_output_name": "tem.out",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    },
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\80_B-slag\deepmd_aimd\non-equilib-initial-config\5000-steps",
        "cp2k_output_name": "tem.out",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    },
    # 需要指定 cell 矩阵和 ensemble_type
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\63_SiB\dpdata-temp",
        "cp2k_output_name": None,
        "cells": np.array([[9.34477, 0, 0],
                           [0, 9.34477, 0],
                           [0, 0, 9.34477]]),
        "ensemble_type": "NVT",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    },
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\64_B2O3\dpdata-temp",
        "cp2k_output_name": None,
        "cells": np.array([[9.402, 0, 0],
                           [0, 9.402, 0],
                           [0, 0, 9.402]]),
        "ensemble_type": "NVT",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    }
]

random_seed = 42
training_out_dir = "./00.data/training_data"
validation_out_dir = "./00.data/validation_data"
```










