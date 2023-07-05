### 项目功能
---

```
1. 晶体电子结构计算和波函数分析
2. 熔体电子结构计算和波函数分析

```

### 项目文件结构
---

**1. new.py**
```
将离散的CP2K PDOS点通过卷积高斯函数转换为平滑曲线。
同时将能量以费米能量为基准进行平移（使费米能量之后为0），并通过该种类的原子数进行归一化处理。

使用命令举例：
python new.py -s 0.01 file1.pdos  > dos.txt
python new.py -s 0.01 file1.pdos  file2.pdos  > dos.txt

```






**Fe2O3.inp：UKS开壳层计算，MAGNETIZATION初猜**

本地目录  C:\Users\sun78\Desktop\cp2k_model\60_Fe2O3-E\22test_Fe2O3_Findit\outputFile+5.0

inp控制文件输出部分，输出包括DOS态密度，PDOS分波态密度，MOLDEN文件，ELF电子局域化函数，MULLIKEN电荷以及MOMENTS

```
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

### 输出文件分析

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








**01_SiP-E_diag.inp**
```
该
本地路径： C:\Users\sun78\Desktop\cp2k_model\44_SiP-E\460_diag

```

