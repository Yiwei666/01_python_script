# 1. 项目功能

VMD可视化渲染脚本



# 2. 文件结构

```
showcub.vmd                    # 电荷密度差分渲染，适用于.cub文件
visualize_xyz.vmd              # xyz文件可视化渲染
```




# 3. 环境配置

### 1. `showcub.vmd`

- 将`showcub.vmd`拷贝到VMD目录下，并在`vmd.rc`文件的末尾插入`source showcub.vmd`。

- 可选：将VMD安装目录写入到系统环境变量中，然后将`showcub.vmd`拷贝到cub文件所在目录，使用cmd命令行启动vmd，使用`cub EDD 0.0004`命令来可视化`EDD.cub`文件，其中等值面设置为`0.0004`。


### 2. `visualize_xyz.vmd`

- 将`visualize_xyz.vmd`拷贝到VMD目录下，并在`vmd.rc`文件的末尾插入`source visualize_xyz.vmd`。

- 可选：将VMD安装目录写入到系统环境变量中，然后将`visualize_xyz.vmd`拷贝到xyz文件所在目录，使用cmd命令行启动vmd，使用`xyz example`命令来可视化`example.xyz`文件。



```
cub  EDD.cub  0.008      # EDD.cub文件
xyz slagF135             # slagF135.xyz文件
```








