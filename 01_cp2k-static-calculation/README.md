# 1. 项目功能


1. 晶体电子结构计算和波函数分析
2. 熔体电子结构计算和波函数分析

🟢 **PDOS计算流程**

1. cp2k进行静态电子结构计算，输出原始的pdos文件   
2. 使用 `new.py` 脚本对原始pdos文件进行平滑处理，并将费米能级移至 0 处   
3. 使用`spdf_sumPDOS.py`脚本获取 `s p d f` 等轨道数据   
4. 注意上述获得的pdos数据是同类（多个）原子总的pdos，如果各类原子数不同，通过峰的强弱比较成键强弱时需要归一化。

<p align="center">
<img src="https://19640810.xyz/05_image/01_imageHost/20241109-154408.png" alt="Image Description" width="1000">
</p>

5. 可以通过电负性差异辅助判断成键类型，电负性数据如下所示。
   - 当两个原子电负性差值约为1.7时，单键约具有50%的离子性，这是一个重要的参考数据。
   - 如果两个原子电负性差值大于1.7时，可判断它们之间主要形成离子键，该物质是离子型化合物；如果两个原子电负性差值小于1.7，则可判断它们之间主要形成共价键，该物质为共价化合物。
   - 例如钠的电负性为0.93，氯的电负性为3.16，两原子的电负性差值为2.23，当它们互相结合成NaCl时，其键的离子性百分数约为70％。因此可以判断氯化钠中钠离子与氯离子之间主要是形成离子键，氯化钠为离子型化合物。



# 2. 项目文件结构

💎 **文件结构**

```
Pt_silicate.inp       # 含 Pt 硅酸盐体系电子结构计算，对角化方法
01_SiP-E_diag.inp     # 含 P 硅熔体电子结构计算，对角化方法
Fe2O3.inp             # Fe2O3 晶体电子结构计算，磁性初猜、开壳层体系
```


### 1. pdos绘图脚本

```
pdos_Plot.py:
        绘制指定x轴范围内的多列y数据曲线，处理对象为经过平滑后的pdos.txt文件
        写一个python脚本处理数据文件，提示用户输入txt文件名，然后读取该数据文件，第一行有n个标签，对应n列数据，
        从第二行起全是数据，然后以第一列数据为x轴数据，其余的n-1 列的数据分别为y1，y2，y3，...数据，然后绘制曲线

spdf_sumPDOS.py（sumPlot_pdos.py）：
        写一个python脚本处理数据文件，提示用户输入txt文件名，然后读取该数据文件，读取数据的时候忽略#字开头的行，因为#字开头的可能是标签。
        注意，数据文件可能有2列，5列，10列或者17列。假如有17列，就按照将第1列数据作为1列，第2列数据作为1列，第3-5列数据的和作为1列，
        第6-10列数据和作为1列，第11-17列数数据和作为1列，将这些列的数据另存到一个txt文件中。
        现在需要给输出的txt文件在第一行加一个表头，按照如下顺序加在不同列的开头， Energy_[eV]     s     p     d       f   ，
        比如输出的数据有3列就是Energy_[eV]     s     p ， 有5列就是Energy_[eV]     s     p     d       f
        上面的代码在读取数据的时候忽略了#字开头行，现在能不能改为忽略第一行即可，因为我发现所有数据格式都是标准的，只需要忽略第一行就可以了

注意：spdf_sumPDOS.py可以不用txt第一行表头进行注释，默认忽略；sumPlot_pdos.py忽略txt文件以#字符开头的行，其余功能与spdf_sumPDOS.py一样。

处理后的数据格式：
        Energy_[eV]	s	p	d	f
        -63.13182587	0.00000000	0.0	0.0	0.0
        -63.10461324	0.00000000	0.0	0.0	0.0
        -63.07740060	0.00000000	0.0	0.0	0.0
        -63.05018797	0.00000000	0.0	0.0	0.0

数据处理对象：经过 new.py 处理后的标准pdos文件（第一行为表头）
```

### 2. pdos后处理脚本

**1. new.py**

- 源码：[new.py](new.py)

```
将离散的CP2K PDOS点通过卷积高斯函数转换为平滑曲线。
同时将能量以费米能量为基准进行平移（使费米能量之后为0），并通过该种类的原子数进行归一化处理。

使用命令举例：
python new.py -s 0.01 file1.pdos  > dos.txt
python new.py -s 0.01 file1.pdos  file2.pdos  > dos.txt

```

**2. pdos.py 和 get-smearing-pdos.py**

注意：`pdos.py` 和 `get-smearing-pdos.py`是放在一起使用的，`get-smearing-pdos.py`会调用`pdos.py`中的方法和函数

```
get-smearing-pdos.py:

读取一个或一对 alpha、beta 自旋文件（ CP2K PDOS 格式），并返回一个名为 "smeared.dat" 的文件，其中包含平滑化的 DOS（态密度）。

使用命令举例：  
Usage: ./get-smearing-pdos.py ALPHA.pdos BETA.pdos
        or
        ./get-smearing-pdos.py file.pdos 

 Output: 
         smeared.dat: smeared DOS
```

### 3. 开壳层-磁性初猜inp文件

- Fe2O3.inp：UKS开壳层计算，MAGNETIZATION初猜

本地目录  `C:\Users\sun78\Desktop\cp2k_model\60_Fe2O3-E\22test_Fe2O3_Findit\outputFile+5.0`

inp控制文件输出部分，输出包括DOS态密度，PDOS分波态密度，MOLDEN文件，ELF电子局域化函数，MULLIKEN电荷以及MOMENTS

```bash
    &PRINT
      &DOS
      &END DOS 
      &PDOS
          NLUMO -1
          COMPONENTS
      &END PDOS   
      &MO_MOLDEN #Exporting .molden file containing wavefunction information
        NDIGITS 9 #Output orbital coefficients if absolute value is larger than 1E-9
        GTO_KIND SPHERICAL #Spherical-harmonic type of basis functions
      &END MO_MOLDEN
      &ELF_CUBE
        STRIDE 1 #Stride of exported cube file
      &END ELF_CUBE
      &MULLIKEN
        PRINT_ALL F #If T, then printing full net AO and overlap population matrix
      &END MULLIKEN
      &MOMENTS
        PERIODIC T #Use Berry phase formula (T) or simple operator (F), the latter normally applies to isolated systems
      &END MOMENTS
    &END PRINT
```

下面是输入文件以及计算完成后的输出文件
```
输入文件：
    dftd3.dat
    Fe2O3.inp
    GTH_POTENTIALS
    slurm-2969346.out
    sub.sh
    tem.out

输出文件：
    alpha-Fe2O3-multiwfn-1.dos
    alpha-Fe2O3-multiwfn-ALPHA_k1-1.pdos
    alpha-Fe2O3-multiwfn-ALPHA_k2-1.pdos
    alpha-Fe2O3-multiwfn-ALPHA_k3-1.pdos
    alpha-Fe2O3-multiwfn-BETA_k1-1.pdos
    alpha-Fe2O3-multiwfn-BETA_k2-1.pdos
    alpha-Fe2O3-multiwfn-BETA_k3-1.pdos
    alpha-Fe2O3-multiwfn-ELF_S1-1_0.cube
    alpha-Fe2O3-multiwfn-ELF_S2-1_0.cube
    alpha-Fe2O3-multiwfn-MOS-1_0.molden
    alpha-Fe2O3-multiwfn-RESTART.wfn
    alpha-Fe2O3-multiwfn-RESTART.wfn.bak-1

```

总结：

```
ALPHA_k1-1~3是各元素的上自旋pdos，BETA_k1-1~3是各元素的下自旋pdos

ELF_S1-1和ELF_S2分别是最高占据轨道和最低空轨道的ELF

```

### 4. 金属体系对角化不收敛

- 解决办法：
  - 通过减小 `ALPHA` 值来实现收敛
  - 适当调大 `ELECTRONIC_TEMPERATURE`，例如由默认的300 K增大到400 K。对于金属体系或有部分填充能带的体系，适当的电子温度（例如几十到几百开尔文）可以帮助费米-狄拉克展开，使得能量计算更稳定。而对于绝缘体或宽带隙半导体，电子温度的影响相对较小，但仍需合理设置以确保计算收敛。
  - 通过增大 `MAX_SCF` 值来实现收敛

```bash
&SCF
    MAX_SCF    500
    EPS_SCF    1.0e-5
    SCF_GUESS  RESTART
    &DIAGONALIZATION
        ALGORITHM STANDARD #Algorithm for diagonalization. DAVIDSON is faster for large systems
    &END DIAGONALIZATION
    &MIXING #How to mix old and new density matrices
        METHOD BROYDEN_MIXING #PULAY_MIXING is also a good alternative
        ALPHA 0.1 #Default. Mixing 40% of new density matrix with the old one
        NBROYDEN 8 #Default is 4. Number of previous steps stored for the actual mixing scheme
    &END MIXING
    &SMEAR
        METHOD FERMI_DIRAC
        ELECTRONIC_TEMPERATURE 300 #Electronic temperature of Fermi-Dirac smearing in K
    &END SMEAR
    ADDED_MOS    500  #Number of virtual MOs to solve
    &PRINT
        &RESTART ON
        &END RESTART
    &END PRINT
&END SCF
```





# 3. 输出文件分析

alpha-Fe2O3-multiwfn-ALPHA_k2-1.pdos 文件的部分结果如下所示   

```
# Projected DOS for atomic kind O at iteration step i = 0, E(Fermi) =     0.343049 a.u.
#     MO Eigenvalue [a.u.]      Occupation                 s                py                pz                px               d-2               d-1                d0               d+1               d+2
       1         -3.159035        1.000000        0.00487488        0.01008856        0.00581955        0.01008845        0.00069501        0.00179932        0.00014453        0.00179930        0.00069501
       2         -3.159035        1.000000        0.00471728        0.00986803        0.00607570        0.00986793        0.00067725        0.00180023        0.00016035        0.00180022        0.00067725
       3         -3.159035        1.000000        0.00471729        0.00986804        0.00607567        0.00986791        0.00067725        0.00180024        0.00016035        0.00180022        0.00067725
       4         -3.159035        1.000000        0.00455618        0.00965519        0.00633921        0.00965507        0.00065959        0.00180064        0.00017581        0.00180063        0.00065959
       5         -3.159034        1.000000        0.00407512        0.01072941        0.00720572        0.01088279        0.00118107        0.00139466        0.00026702        0.00130759        0.00126578
       6         -3.159034        1.000000        0.00407512        0.01095947        0.00720571        0.01065271        0.00130817        0.00126395        0.00026702        0.00143830        0.00113868
       7         -3.159034        1.000000        0.00407563        0.01072628        0.00720412        0.01088302        0.00118071        0.00139512        0.00026694        0.00130739        0.00126579
```


# 4. 熔体电子结构计算


**01_SiP-E_diag.inp**
```
本地路径： C:\Users\sun78\Desktop\cp2k_model\44_SiP-E\460_diag

```

```bash
        &PRINT
            &MO_MOLDEN
                NDIGITS 8
                GTO_KIND SPHERICAL
            &END MO_MOLDEN
            &PDOS
                NLUMO -1
                COMPONENTS
            &END PDOS
                                                           #  Printing which kind of atomic charge?
            &HIRSHFELD  SILENT
                FILENAME hirshfeld
            &END  
            &MULLIKEN  SILENT
                FILENAME MullIKEN
            &END MULLIKEN
            &VORONOI                                       # VORONOI atomic charge
                VORONOI_RADII Covalent
            &END VORONOI  
            &LOWDIN
                PRINT_ALL F                                    # If T, then printing full net AO and overlap population matrix
            &END LOWDIN
                                                           # Output cube file for which function?
            &ELF_CUBE
                FILENAME elf
                STRIDE 1 1 1
            &END ELF_CUBE
            &E_DENSITY_CUBE
                FILENAME density_cube
                STRIDE 1 1 1
            &END E_DENSITY_CUBE
            &MO_CUBES
                NHOMO  2                                      # 最高和次高占据轨道
                NLUMO  2                                      # 最低和次低占据轨道
            &END MO_CUBES
            &V_XC_CUBE                                        # Exchange-correlation potential
                STRIDE 1                                      # Stride of exported cube file
            &END V_XC_CUBE
            &V_HARTREE_CUBE
                STRIDE 1                                      # Stride of exported cube file
            &END V_HARTREE_CUBE 
        &END PRINT

```

# 5. cp2k电子结构关键词


```
说明：最该高占据轨道和最低空轨道

NHOMO
        NHOMO {Integer}
        If the printkey is activated controls the number of homos that dumped as a cube (-1=all), eigenvalues are always all dumped  [Edit on GitHub]
        This keyword cannot be repeated and it expects precisely one integer.
        Default value: 1

NLUMO
        NLUMO {Integer}
        If the printkey is activated controls the number of lumos that are printed and dumped as a cube (-1=all)  [Edit on GitHub]
        This keyword cannot be repeated and it expects precisely one integer.
        Default value: 0
```






