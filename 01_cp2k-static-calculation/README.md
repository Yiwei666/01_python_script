### 项目功能
---

```
1. 晶体电子结构计算和波函数分析
2. 熔体电子结构计算和波函数分析

```

### 项目文件结构
---

**Fe2O3.inp**

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
    dftd3.dat
    Fe2O3.inp
    GTH_POTENTIALS
    slurm-2969346.out
    sub.sh
    tem.out

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





**01_SiP-E_diag.inp**
```
该
本地路径： C:\Users\sun78\Desktop\cp2k_model\44_SiP-E\460_diag

```

