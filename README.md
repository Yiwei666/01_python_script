### 01_python_script 分子动力学模拟python数据处理脚本
<br>

```
   最常用的脚本包括：
      58_[47类]轨迹分析和绘图.py
      49_[扩展Beta]单质或化合物或多相混合体系密度计算.py
      42_[扩展]化合物各类原子数统计.py

```

<br>

- **58_[47类]轨迹分析和绘图.py** 是 **47_[类]轨迹分析和绘图.py** 升级版本
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
```


- **56_isaacs_order.py**
```
上述代码实现了以下功能：
    首先，代码列出了同级目录下的所有文件，并将它们打印出来，以便用户知道可以选择哪个数据文本文件进行处理。
    然后，代码提示用户输入待处理的数据文本名，并读取该文本文件的内容。
    在读取文本文件时，代码会忽略空行和以 '#' 开头的行，以确保只处理有效的数据行。
    接下来，代码打印了所有列的数据。它将每一行分割成不同的列，并将每列的数据打印出来。
    最后，代码按照第一列数据的递增顺序对数据进行排序，并打印出第一列及其对应的倒数第二列的数据。它首先将数据解析成列，然后根据第一列的值进行排序，并将排序后的结果打印出来。
通过这些步骤，代码可以处理指定数据文本文件中的数据，并提供了打印所有列数据以及按照第一列排序的功能。
```


- **51_两相模型构建及自由能面绘制.py**
```
  本脚本的功能如下:
      01: txt文件特定列加上常数，忽略 空行 和 # 开头行，打印总行数（忽略空行和 # 字开头的）
      02: 将两个txt文件合并，忽略 空行 和 # 开头行，打印总行数（忽略空行和 # 字开头的）
      03: 输出txt文件某列 大于 等于某个数的行号，忽略#开头行
      04: 输出txt文件某列 小于 等于某个数的行号，忽略#开头行
      05: 生成10000行自定义曲面函数的data.txt文件
      06: 绘制3列（x,y,z）数据组成的曲面图及其二维填色图
      
      -1: 测试
```


- **50_[类]基于势函数数据库导出lammps运行控制in文件.py**
```
  本脚本的功能如下:
      01: 创建json势参数数据库文件，初始内容为 {"charge": {}, "parameter": {}}
      02: 添加势函数原子电荷信息到数据库文件中
      03: 添加势函数原子对势参数信息到数据库文件中
      04: 查看势参数数据库内容，满足所有json格式数据库的查看
      05: 输出控制lammps运行的in文件(目前主要为元素相互作用势参数部分)
      
      -1: 测试
```


- **49_[扩展Beta]单质或化合物或多相混合体系密度计算.py**  
该脚本相比于**49_[扩展]单质或化合物或多相混合体系密度计算.py**新增功能**05: 基于各组分质量比计算各原子数量**  
新版脚本位于C:\Users\sun78\Desktop\cp2k_model\50_SiV\49_[扩展Beta]单质或化合物或多相混合体系密度计算.py 目录下
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


- **49_[扩展]单质或化合物或多相混合体系密度计算.py** 的功能如下， 是 **38_单质或化合物或多相混合体系密度计算.py** 升级版本
```
  本脚本的功能如下:
      01: 查看数据库内容
      02: 手动修改、添加或删除化合物原子组成数据库中的数据
      03: 手动修改、添加或删除密度数据库中密度数据，并保存为新的数据库文件
      04: 基于factsage体积数据计算单组元密度
      05: 计算多组元混合体系密度
      
      -1: 测试
```


- **48_[类]cell文件转data文件.py**
```
  本脚本的功能如下:
      01: Material Studio分数坐标cell文件转 Multiwfn标准格式的xyz笛卡尔坐标文件
      02: Material Studio分数坐标cell文件转 lammps标准格式的data结构文件
      
      -1: 测试
```


- **42_[扩展]化合物各类原子数统计.py** 是 **42_化合物各类原子数统计.py 升级版本**
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


- **41_基于字典的键级计算测试版.py**
```

```


- **40_Mayer键级多中心原子综合版.py**
```

```


- **39_单质密度和相对原子质量查询.py**
```

```


-  **38_单质或化合物或多相混合体系密度计算.py**
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

- **37_获取元素密度和相对原子质量(文本转字典).py**
```

```


- **36_分数坐标cell文件转xyz笛卡尔坐标文件.py**
```

```


- **35_Mayer键级.py**
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


- **34_晶面指数计算.py**
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





