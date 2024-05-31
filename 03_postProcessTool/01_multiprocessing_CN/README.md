# 1. 项目功能

通过 python 的 multiprocessing 模块多进程加速配位数计算，分别基于 piecewise 和 sigmoid 函数实现

# 2. 文件结构

```
piecewiseCalc.py                                   # 函数模块，仅包含函数
58_sigmoidXYZ轨迹文件配位数多进程计算.py            # 主函数，基于sigmoid计算配位数
58_piecewiseXYZ轨迹文件配位数多进程计算.py          # 基于piecewise阶跃函数计算配位数
```

# 3. 环境配置

1. 在Windows系统中，由于缺乏Unix系统中的`fork()`系统调用，Python必须序列化并通过一个新的Python解释器实例来重载整个父进程的状态。
2. 为了避免启动多个进程时代码无限循环执行，通常需要在`if __name__ == '__main__':`块中启动进程。这样可以确保只有在该脚本作为主程序执行时才会运行多进程代码，而不是在每次导入模块时都运行。




# 参考资料

- python多进程并行计算：https://github.com/Yiwei666/12_blog/blob/main/888/8-006.md



