### 项目功能
---

```
基于cp2k的电子结构计算和波函数分析

```

### 项目文件结构
---

**01_SiP-E_diag.inp**
```
该
本地路径： C:\Users\sun78\Desktop\cp2k_model\44_SiP-E\460_diag

```


**Fe2O3.inp**
```
本地目录  C:\Users\sun78\Desktop\cp2k_model\60_Fe2O3-E\22test_Fe2O3_Findit\outputFile+5.0

inp控制文件输出部分：

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

