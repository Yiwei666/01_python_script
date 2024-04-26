# 1. 常用脚本


- 58_[47类]轨迹分析和绘图.py
- 49_[扩展Beta]单质或化合物或多相混合体系密度计算.py
- 42_[扩展]化合物各类原子数统计.py



# 2. 脚本说明

### `63_scatterHeatmap.py`

实现了从一个名为 "extract.xyz" 的文件中读取2列数据，基于这两列数据绘制了散点图和热力图


### `62_Heatmap.py`(相关系数矩阵计算与热力图绘制)

:dart: 脚本功能

```
1. 计算多列数据表格中任意两列数据的线性相关系数（-1到1），并绘制热力图
2. 要求表格数据结构满足如下格式

Element  Distribution  X-O_BL  X-Si_BL
P         -1.277         1.57    2.33
Ti        -0.1411        1.79    2.59
Mg         0.3604        1.99    2.82

```



### `61_离子对PMF和解离能障计算.py`


计算公式： $\frac{1}{k_{B}\ T} W^{e f f}(r)=-\ln g_{\alpha \beta}(r)-2 \ln \left(\frac{r}{r_{\min }}\right)$.

```
   基于ISAACS输出的径向分布函数g(r)文件，如g(r)[Ti,Si]，计算 平均力势曲线，定义式如上所示，注意计算的是公式右边的部分。
   数据处理过程中忽略了@开头的注释行，对于g(r)为0的部分采用nan进行填充，处理后的数据保存在pmf.txt文件中
   1. 提示输入文件名，支持ISACAS导出的g(r)[Ti,Si]
   2. 提示输入原子对的截断半径，需提前获取
```

### `60_[指定x和y范围]自由能面投影图及等高线绘制.py`
```

```

### `59_[指定x和y范围]自由能面二维投影图绘制.py`
```

```

### `58_[47类]轨迹分析和绘图.py` 是 `47_[类]轨迹分析和绘图.py` 升级版本
```
  本脚本的功能如下:
      01: 添加盒子信息到多帧xyz文件并输出各类原子范围。输入的xyz文件主要是基于VMD周期性处理过的，输出适用于plumed软件分析的xyz轨迹文件（依赖于其他方法）
      02: 添加盒子信息，针对单帧/多帧xyz轨迹文件，且每一帧的原子数可以不相同（不依赖于其他方法）
      03: 计算xyz轨迹文件某一帧的原子序号分布（不依赖于其他方法）,主要是用于辅助plumed输入文件编写
      04: 提取xyz轨迹文件某些范围帧数，如 1,3,5-10,30,每帧原子数可不同
      05: cp2k输出的ener文件温度、势能随步数绘图，标准ener文件格式即可
      06: 提取多帧xyz文件特定编号原子周围半径r范围内的原子[未考虑周期性]
      07: 对xyz轨迹文件进行周期性扩增
      08: 提取多帧xyz文件特定编号原子周围半径r范围内的原子[考虑周期性]，功能 06升级版
      09: 计算总的径向分布函数TRDF
      10: 返回xyz轨迹文件盒子周期性扩增前后某一帧的原子序号分布（依赖于07方法，需要每一帧中同类原子连续分布）
      11: xyz文件某一帧转data文件，data文件可用于lammps经典分子动力学模拟
      12: colvar数据文件等绘图（自选列数），标准colvar文件格式即可
      13: 计算xyz文件所有帧中某个原子到某个平面的距离，平面由三个原子的序号确定
      14: 基于不同原子对的截断半径Rij，提取多帧xyz文件特定编号原子周围半径Rij范围内的配位原子[考虑周期性]，功能 08升级版
      
      -1: 测试
      
      
  注意：
      01: 该脚本的06，08，14功能可用于提取xyz轨迹文件中某个原子的轨迹（将截断半径设置为趋近于0的值的一个值，使得该截断半径内不出现配位原子），得到类似如下的多帧xyz轨迹文件，行数以3为周期，搭配 54_多帧轨迹文件中特定原子的xyz分坐标提取.py 脚本即可提取每一帧中的xyz分坐标。
                  1
                  This is number:1
                   B         0.303598        4.846121        6.626125
                  1
                  This is number:2
                   B         0.345071        4.648057        6.391401
                  1
                  This is number:3
                   B         0.351086        4.235202        6.350704
                  ...
```


### `57_[指定x和y范围]自由能三维曲面及二维填色图绘制.py`
```

```


### `56_isaacs_order.py`
```
该脚本实现对 金属熔体中 特定杂质原子，如 X 原子周围配位的基体原子数量即占比的分析，基于百分比权重能计算平均配位数

这段代码的功能是：
    获取当前目录下的所有文件并打印文件名。
    提示用户输入待处理的数据文本名。
    读取数据文本中的有效数据，并打印所有列的数据。
    按照第一列的数值进行递增排序，并打印第一列及其对应的倒数第二列数据。
    计算每一行中第一列和倒数第二列乘积的求和，并打印结果。
这段代码主要实现了文件操作、数据处理和统计计算的功能。

注意：该脚本在计算过程中忽略空行和#开头的行，并打印每一行中的第一列和倒数第二列乘积的求和（平均配位数），处理的数据参考格式如下

-------------------------------------------------------

# Environments for Mg atoms:

# N(tot)   N(Mg)   N(Si)          Number   or     Percent
 10        0      10           1.30464   or      16.308 %
 11        0      11           1.71523   or      21.440 %
 13        0      13           1.42384   or      17.798 %
 12        0      12           1.90728   or      23.841 %
 14        0      14           0.72185   or       9.023 %
  9        0       9           0.53642   or       6.705 %
 15        0      15           0.16556   or       2.070 %
 16        0      16           0.04636   or       0.579 %
  8        0       8           0.14570   or       1.821 %
  7        0       7           0.01325   or       0.166 %
  6        0       6           0.00662   or       0.083 %
 17        0      17           0.01325   or       0.166 %

```

### `55_[指定x和y范围]自由能面局域极小值计算.py`
```

```

### `55_自由能面局域极小值计算.py`
```

```

### `54_多帧轨迹文件中特定原子的xyz分坐标提取.py`
```
  本脚本的功能如下:
      01: 提取每一帧只有1个原子的xyz轨迹文件中该原子的x或y或z分坐标，输出文件有两列，第一列为帧数，第二列为分坐标
      注意：单原子轨迹文件可基于本文件夹下47或58脚本获取
      
```

### `53_无偏自由能面绘制.py`

```
      01: 导入必要的模块：使用import语句导入numpy和matplotlib.pyplot模块。
      02: 定义常量和变量：设置一些常量和变量，如长度单位转换因子、玻尔到埃单位转换因子、玻尔兹曼常数等。
      03: 加载colvar文件：使用np.loadtxt()函数加载指定路径下的colvar文件，并将数据存储在colvar_raw变量中。
      04: 提取CVs数据：从colvar_raw中提取两个关键变量（CVs）的数据，分别存储在d1和d2变量中。
      05: 创建二维直方图：使用np.histogram2d()函数根据d1和d2的数据生成二维直方图，将结果存储在cv_hist变量中。
      06: 打印直方图的bin边缘和频率：通过打印cv_hist的元素来显示直方图的bin边缘和频率信息。
      07: 计算概率：将直方图中的频率归一化，得到每个bin的概率，存储在prob变量中。
      08: 计算自由能表面：根据概率值，使用玻尔兹曼常数和温度计算自由能表面，并将结果存储在fes变量中。
      09: 转换能量单位为kJ/mol：将自由能表面的能量单位从eV转换为kJ/mol，得到fes_kjmol变量。
      10: 绘制并保存自由能表面图像：根据计算得到的自由能表面数据，使用plt.imshow()函数绘制图像，并使用plt.colorbar()添加颜色条。然后设置坐标轴标签和图像标题，并使用plt.show()显示图像。注释掉的代码部分是用于保存图像的。
```


### `51_两相模型构建及自由能面绘制.py`

```
  两相模型构建流程：
      01: 确定单相/均相的总原子数及各组元（化合物）的质量百分数，基于脚本  49_[扩展Beta]单质或化合物或多相混合体系密度计算.py  计算各组元的摩尔数及体系的密度
      02：基于结合42_[扩展]化合物各类原子数统计.py 计算体系中各类原子数量，利用material studio进行建模，获取.cell文件
      03：结合ovito或脚本48_[类]cell文件转data文件.py 导出 xyz格式的初始结构模型，进行标准AIMD获取平衡结构，提取某两帧平衡结构model1.xyz和model2.xyz作为搭建两相结构的初始结构模型
      04：利用本脚本功能1对上述其中一个model2.xyz模型的z分坐标加上一个常数（model1.xyz模型的晶格常数C + 两相界面真空层厚度0.3~0.5 Å），获取modify_model2.txt模型文件
      05：利用本脚本02功能对上述 model1.xyz 和 modify_model2.txt 进行合并，得到两相模型 model_merge.xyz，注意添加两相模型总原子数以及晶格参数
      06：利用本脚本03和04功能获取model_merge.xyz中z轴方向需要在边界处固定的原子编号，添加到cp2k的inp文件中
      07：利用上述model_merge.xyz 进行无偏分子动力学模拟，获取两相模型的平衡结构 merge_equilibrium.xyz
      08：在inp文件中设置偏置参数，利用上述merge_equilibrium.xyz模型进行元动力学模拟


  本脚本的功能如下:
      01: txt文件特定列加上常数，忽略 空行 和 # 开头行，打印总行数（总行数不计空行和 # 字开头行）
      02: 将两个txt文件合并，忽略 空行 和 # 开头行，打印总行数（总行数不计空行和 # 字开头行）
      03: 输出txt文件某列 大于 等于某个数的行号，行号包含#开头行
      04: 输出txt文件某列 小于 等于某个数的行号，行号包含#开头行
      05: 生成10000行自定义曲面函数的data.txt文件
      06: 绘制3列（x,y,z）数据组成的曲面图及其二维填色图
      
      -1: 测试
```


### `50_[类]基于势函数数据库导出lammps运行控制in文件.py`
```
  本脚本的功能如下:
      01: 创建json势参数数据库文件，初始内容为 {"charge": {}, "parameter": {}}
      02: 添加势函数原子电荷信息到数据库文件中
      03: 添加势函数原子对势参数信息到数据库文件中
      04: 查看势参数数据库内容，满足所有json格式数据库的查看
      05: 输出控制lammps运行的in文件(目前主要为元素相互作用势参数部分)
      
      -1: 测试
```


### `49_[扩展Beta]单质或化合物或多相混合体系密度计算.py` 

:heart: 新增功能


1. 该脚本相比于 `49_[扩展]单质或化合物或多相混合体系密度计算.py` 新增功能 `05: 基于各组分质量比计算各原子数量`
2. 新版脚本位于`C:\Users\sun78\Desktop\cp2k_model\50_SiV\49_[扩展Beta]单质或化合物或多相混合体系密度计算.py` 目录下


:star: 脚本说明

```
  本脚本的功能如下:
      01: 查看数据库内容
      02: 手动修改、添加或删除化合物原子组成数据库中的数据
      03: 手动修改、添加或删除密度数据库中密度数据，并保存为新的数据库文件
      04: 基于factsage体积数据计算单组元密度
      05: 基于各组分质量比计算各原子数量
      06: 计算多组元混合体系密度
      
      -1: 测试
```



### `49_[扩展]单质或化合物或多相混合体系密度计算.py` 

该脚本是 `38_单质或化合物或多相混合体系密度计算.py` 升级版本

```
  本脚本的功能如下:
      01: 查看数据库内容
      02: 手动修改、添加或删除化合物原子组成数据库中的数据
      03: 手动修改、添加或删除密度数据库中密度数据，并保存为新的数据库文件
      04: 基于factsage体积数据计算单组元密度
      05: 计算多组元混合体系密度
      
      -1: 测试
```


- `49_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json`

化合物原子组成数据库，对应上述脚本功能2

```json
{"CaO": {"Ca": "1", "O": "1", "total": "2"}, "SiO2": {"Si": "1", "O": "2", "total": "3"}, "B2O3": {"B": "2", "O": "3", "total": "5"}, "P2O5": {"P": "2", "O": "5", "total": "7"}, "MgO": {"Mg": "1", "O": "1", "total": 2}, "Al2O3": {"Al": "2", "O": "3", "total": 5}, "K2O": {"K": "2", "O": "1", "total": 3}, "TiO2": {"Ti": "1", "O": "2", "total": 3}, "V2O5": {"V": "2", "O": "5", "total": 7}, "Cr2O3": {"Cr": "2", "O": "3", "total": 5}, "MnO": {"Mn": "1", "O": "1", "total": 2}, "MnO2": {"Mn": "1", "O": "2", "total": 3}, "FeO": {"Fe": "1", "O": "1", "total": 2}, "Fe3O4": {"Fe": "3", "O": "4", "total": 7}, "Fe2O3": {"Fe": "2", "O": "3", "total": 5}, "Co2O3": {"Co": "2", "O": "3", "total": 5}, "NiO": {"Ni": "1", "O": "1", "total": 2}, "Cu2O": {"Cu": "2", "O": "1", "total": 3}, "CuO": {"Cu": "1", "O": "1", "total": 2}, "ZrO2": {"Zr": "1", "O": "2", "total": 3}, "CaF2": {"Ca": "1", "F": "2", "total": 3}, "BaO": {"Ba": "1", "O": "1", "total": 2}, "La2O3": {"La": "2", "O": "3", "total": 5}, "Ce2O3": {"Ce": "2", "O": "3", "total": 5}, "MoO2": {"Mo": "1", "O": "2", "total": 3}}
```


- `49_[扩展-2化合物密度数据库]单质或化合物或多相混合体系密度计算.json`

化合物密度数据库，对应上述脚本功能3，这些氧化物的密度数据有些是从书本中查询得到的，有些是利用factsage计算得到的

```json
{"SiO2": ["2.335", "g/cm3", "null", "SiO2", "null", "null", "null"], "CaO": ["2.8581", "g/cm3", "null", "CaO", "null", "null", "null"], "B2O3": ["2.55", "g/cm3", "null", "B2O3", "null", "null", "null"], "V2O5": ["3.357", "g/cm3", "null", "V2O5", "null", "null", "null"], "MnO2": ["5.2", "g/cm3", "null", "MnO2", "null", "null", "null"], "Fe2O3": ["5.277", "g/cm3", "null", "Fe2O3", "null", "null", "null"], "TiO2": [4.245019666206016, "g/cm3", "null", "TiO2", "null", "null", "null"], "Al2O3": [3.987067500879834, "g/cm3", "null", "Al2O3", "null", "null", "null"]}
```



### `48_[类]cell文件转data文件.py`
```
  本脚本的功能如下:
      01: Material Studio分数坐标cell文件转 Multiwfn标准格式的xyz笛卡尔坐标文件
      02: Material Studio分数坐标cell文件转 lammps标准格式的data结构文件
      
      -1: 测试
```


### `42_[扩展]化合物各类原子数统计.py` 是 `42_化合物各类原子数统计.py` 升级版本
```
请输入待处理字典，或字符串，如 {'CaO': '11', 'SiO2': '10', 'B2O3': '1'} 或 str,CaO,11,SiO2,10,B2O3,1  ,其中开头的 str 必不可少

代码实现了一个化学计算器，可以根据输入的化学式和化合物的数量，计算出凝聚态体系中各种化合物的原子组成。具体实现过程如下：

1. chemicalsSplit()函数将输入的化学式字符串转换为字典，字典的键为分子式，值为该分子式的原子组成。
2. loadData()函数从json文件中读取数据，返回一个字典，该字典包含了各种分子式的原子组成。
3. 判断输入的分子式的组成是否都在数据库中，如果有缺失的分子式，则调用chemicalsSplit()函数，为其添加原子组成，并将更新后的字典写入到json文件中。
4. atomCount(atomDict,compoundDict)函数根据输入的分子式的组成字典和原子组成数据库，返回一个列表，列表的元素是字典，每个字典是每种化合物的各原子构成。
5. dict_Sum(ini_dict)函数将列表中多个字典进行合并，键相同的值相加。

综上所述，该代码实现了一个化学计算器，可以方便地计算出凝聚态体系中各种化合物的原子组成。 
```


### `41_基于字典的键级计算测试版.py`

```
请输入包含有中心原子和配位原子的字典，如 {'1': ['16', '27'], '2': ['12']} 格式，该字典可以基于脚本40计算出来
推荐使用 脚本40 进行计算
```

### `40_每列数据最小值和最大值.py`


```
1. txt中的数据格式参考 40_键级密度百分比.py 注释中列出的键级数据，每列数据中可能就会有"--"字符串，不同列之间使用tab进行分隔
2. 使用dataframe数据结构读取该数据文件，然后打印出每列数据的最大值和最小值
```


### `40_各类化学键数量百分比.py`

:pushpin:  脚本说明

```
1. 数据来源与 [40_键级密度百分比.py] 脚本相同
2. 统计各偶数列的的数据个数，即模拟体系中各类化学键的数量，计算各类化学键的百分比
3. 可以直接将运行结果中的最后数据列部分复制到origin中绘制饼图
```

:dart:  结果展示

```
请输入要处理的键级txt文件名: Ti-O.txt
列2中化学键的个数：158,  '--'的个数：133
列4中化学键的个数：291,  '--'的个数：0
列6中化学键的个数：38,  '--'的个数：253
每一列的总行数：291
总的化学键数量为： 487.0
列2中化学键的百分比：32.44 %
列4中化学键的百分比：59.75 %
列6中化学键的百分比：7.8 %
32.44
59.75
7.8
```

### `40_键级密度百分比.py`

:pushpin:  数据来源

```
如下所示是一个体系中不同原子对的键长-键级分布数据，奇数列是键长数据，偶数列是键级数据
由于同一体系中不同类型化学键的数量不同，因此采用'--'符号填补缺失的数据，使得所有列的数据个数一致
下面的数据通常是从origin中复制粘贴过来的，origin中可以使用'--'符号填补空白

1.654	0.983	3.382	0.033	1.76	1.656
1.656	1.493	2.936	0.04	1.756	1.028
1.566	1.075	3.137	0.036	1.887	0.722
1.612	1.318	2.324	0.282	1.813	1.105
1.728	0.956	2.835	0.145	2.093	0.783
1.664	1.472	2.151	0.467	1.766	1.732
1.766	0.929	2.492	0.115	2.09	0.574
1.572	1.037	2.855	0.131	--	--
1.791	0.842	2.375	0.286	--	--
1.707	1.234	2.399	0.115	--	--
1.644	1.278	2.023	0.53	--	--
1.552	1.419	2.377	0.14	--	--
1.699	0.982	2.254	0.309	--	--
1.717	0.967	2.299	0.371	--	--
--	--	3.1	0.039	--	--
--	--	2.363	0.259	--	--
--	--	2.174	0.384	--	--
--	--	2.649	0.122	--	--
--	--	2.462	0.299	--	--
--	--	2.775	0.088	--	--
--	--	3.016	0.008	--	--
--	--	2.663	0.093	--	--
--	--	3.18	0.022	--	--
```

:fire:  基本概念

```
总键级（TBO）：体系中各类化学键的键级数据求和。
总键级密度（TBOD）：TBO/V，总键级/模拟盒子体积，体积的长度单位通常采用 Å。
Partial bond order density（PBOD）：各类键的键级总和/模拟盒子体积。
键级密度百分比：各类键的PBOD/TBOD*100% , 也等于 各类键的各类键的键级总和/总键级*100%

参考文献：https://doi.org/10.1063/1.4987033
```

:bulb: 脚本说明

```
1. 这段代码的目的是处理包含键级数据的文本文件，计算偶数列的总和、总和占比和键序密度等信息，并将这些信息输出到控制台。
2. 由于需要计算键序密度，因此计算过程中需要输入模拟盒子的边长，默认采用立方体盒子。
```

:bell: 结果展示

```
请输入要处理的键级txt文件名: Ti-O.txt
请输入电子结构计算的立方模型盒子边长，单位, Å：15.0
[184.48100000000002, 57.681000000000004, 35.66099999999999]
各偶数列的和: [184.48100000000002, 57.681000000000004, 35.66099999999999]
总和: 277.82300000000004
各偶数列的和占总和的百分比: [66.4, 20.76, 12.84]
体系中各化学键的键序密度： [0.0547, 0.0171, 0.0106]
总键序密度： 0.0823
```



### `40_同种原子键级计算.py` 和 `40_同种原子键级计算_2nd.py`
```
1. 上述两个脚本的功能是一样的，用于清洗 [40_Mayer键级与键长_升级版.py] 脚本输出的同类原子对无效或重复的键级数据

2. 基于 [40_Mayer键级与键长_升级版.py] 脚本计算同类原子键级数据时，输出的 [bondOrder.txt] 文件中同类原子数据会有重复，
   以SiP体系为例，假如有a个Si原子，b个P原子，计算Si-Si的键级，如果 [40_Mayer键级与键长_升级版.py] 输出的Si-Si键级数据有
   c 组，那么实际有效的Si-Si原子对数量为 (c-a)/2, 无效的键级数据有 a + (c-a)/2 = (c+a)/2，其中 a 组数据是原子和原子本身的键级，
   如，Si1-Si1，Si2-Si2，...，另外 (c-a)/2 是被重复计算的数据，如 Si1-Si2 和 Si2-Si1 应当只保留其中之一，故实际有效
   的Si-Si原子对数量为 (c-a)/2。

3. 运行上述代码需要将 40_Mayer键级与键长_升级版.py 计算出来的同种原子对键级数据保存到一个新的txt文件中，不包含表头，参考数据可格式如下

   1:1    0.0    4.153
   1:5    2.76   0.598
   1:164  2.508  0.753
   1:182  2.371  0.873
   1:213  2.395  0.853   
   ......

4. 脚本清洗无效和重复数据的原理。通过分析上述第一列数据中原子对的编号是否相同，以及原子对互换后是否与其他数据重复来实现数据清洗。

5. 两个脚本保存数据的文件名依次为 bondOrder_retain.txt 和 bondOrder_retain_2nd.txt。
```


### `40_Mayer键级与键长_升级版.py`
```
注意：该脚本是在40_Mayer键级多中心原子综合版.py基础上进一步开发的

   1. 升级版除了能够计算键级外，还能够计算相应原子对的键长，从而绘制键长和键级的变化关系图。
   2. 计算完后原子对，键长以及键级数据会以追加的形式写入到bondOrder.txt文件，复制到origin进行绘图即可，数据的结构如下所示，共有3列，分别为原子对编号，键长和键级。

   atomPair  bondLength  bondOrder 
   1:1    0.0    4.153
   1:5    2.76   0.598
   1:164  2.508  0.753
   1:182  2.371  0.873
   1:213  2.395  0.853
   ......

   3. 该脚本计算非同类原子键级时，如Si-O，输出的数据无需清洗，可直接用于绘图；如果计算的是同类原子键级，输出的键级数据中会有部分重复数据，需要基于 40_同种原子键级计算.py
      脚本 或者 40_同种原子键级计算_2nd.py 脚本进行清洗。

```



### `40_Mayer键级多中心原子综合版.py`
```
注意本脚本是基于multiwfn输出的bndmat.txt文件进行计算的

   1. 首先提示用户输入xyz轨迹文件明，输入用于电子结构计算的xyz文件名即可
   2. 提示输入模拟盒子尺寸，默认是正方形盒子，用于考虑周期性边界
   3. 提示输入中心原子和配位原子
   4. 提示输入原子对的截断半径
   5. 提示输入含有键级数据的矩阵文件名，默认是multiwfn输出的bndmat.txt文件
   6. 最后输出键级数据文件bondOrder.txt，包含每一个中心原子及其配位原子的键级数据，平均值，方差，截断半径等。

注意：该脚本仅能计算 中心原子和配位原子 不是同类原子的键级数据，如Si-O原子对，对于同类原子对的键级，如Si-Si原子对，则需要采用 40_Mayer键级与键长_升级版.py 脚本来计算。

```


### `39_单质密度和相对原子质量查询.py`

```

```


### `38_单质或化合物或多相混合体系密度计算.py`

```
请选择单质数据库，1 2, or 3?  
1= pureDensityGasDict                  (单质密度数据库，适用于合金熔体体系，暂不能计算含有H,N,O,F,Cl,Ar等元素的混合体系密度),
2= pureDensitySolidDict                (单质密度数据库，适用于熔体体系中含有H,N,O,F,Cl,Ar等非金属元素体系)，非金属元素的密度基于氧化物密度倒推校正获得，暂不完善
3= pureSolidOxideDensityDict           (纯固态氧化物密度数据库)，参考手册 The Oxide Handbook，HRC等
4= pureLiquidOxideDensityFactsageDict  (纯液态氧化物密度数据库), 源于factsage倒退修正,1800k
5= pureOxideDensityMSDict              (纯固态氧化物密度数据库),参考 Material Project晶体结构数据库
6= mixOxideSimpleSubstanceDensityDict  (金属和氧化物混合体系密度数据库，适合两相混合体系计算，参考1和4)，推荐使用该数据库
合金混合体系相对分子质量计算和Factsage密度计算可以任选1和2数据库
```

### `37_获取元素密度和相对原子质量(文本转字典).py`

```

```


### `36_分数坐标cell文件转xyz笛卡尔坐标文件.py`
```
1. 将 Materianl Studio 建模导出的.cell文件转换为同名的.xyz文件，并统计各原子的数量，保留晶胞长度信息。
2. 可视化软件Ovito能实现类似的格式转换

```


### `35_Mayer键级.py`

该脚本的缺点在于未考虑盒子的周期性

```
以下是代码的功能分条总结：

1. 从文件中读取坐标数据并将其绘制为散点图。
2. 提示用户选择文件路径或手动输入文件名。
3. 读取文件并计算原子数。
4. 创建原子数原子数的多维矩阵。
5. 从文件中读取键级数据并将其填充到矩阵中。
6. 提取用户指定的中心原子和配位原子的键级数据。
7. 计算键级数据的平均值。
8. 将键级数据和平均值写入文件。
```


### `34_晶面指数计算.py`

```
该代码主要实现了以下功能：

1. 导入了时间模块，并显示了当前时间。
2. 提示用户输入三个点的坐标和晶格常数a，并将输入的字符串转换为浮点数。
3. 根据输入的三个点的坐标，计算出平面方程的系数A、B、C、D，并显示方程形式和系数。
4. 根据平面方程的系数，计算出x、y、z轴截距，进而计算出晶面指数h、k、l，并显示晶面指数。
5. 根据晶面指数和晶格常数a，计算出立方晶系晶面间距d，并显示结果。
6. 根据平面方程的系数，计算出原点到平面的距离r，并显示结果。
7. 计算r/d的值，并显示结果。
8. 显示任务完成，并计算程序运行时间。
```


### `02_某几帧.py`

对于xyz轨迹文件，输入想要提取的起始帧数和截止帧数来提取某一帧或者连续的几帧，相关升级功能已经耦合到 `58_[47类]轨迹分析和绘图.py` 的功能`04`中

