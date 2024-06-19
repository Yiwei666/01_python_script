# 1. 项目功能

1. 基于xyz轨迹文件计算每一帧中指定原子对的配位数，用于绘制配位数随模拟时间的变化曲线
2. 通过 python 的 multiprocessing 模块多进程加速配位数计算，分别基于 piecewise 和 sigmoid 函数实现
3. 同样适用于长、宽、高不等的长方体模拟盒子，在周期性扩增判断条件中，考虑到了两个原子的镜像问题，即在原子对配位数计算时，两个原子在xyz三个方向上的分坐标差值不能超过长方体相应边长的一半

# 2. 文件结构

```
piecewiseCalc.py                                  # 函数模块，仅包含函数
58_sigmoidXYZ轨迹文件配位数多进程计算.py            # 主函数，基于sigmoid计算配位数
58_piecewiseXYZ轨迹文件配位数多进程计算.py          # 基于piecewise阶跃函数计算配位数
```

# 3. 环境配置




# 参考资料

- python多进程并行计算：https://github.com/Yiwei666/12_blog/blob/main/888/8-006.md



