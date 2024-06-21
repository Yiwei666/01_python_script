# 1. 目录

1. [无监督学习](/02_GPT/03_MachLearn/3-001.md)


# 2. 常见无监督学习算法

1. 降维算法 (Dimensionality Reduction Algorithms):

   - 主成分分析 (Principal Component Analysis, PCA)：一种用于找到数据低维表示的方法，同时保留尽可能多的变异性 。

   - 奇异值分解 (Singular Value Decomposition, SVD)：通过降低原特征矩阵的秩来学习数据的底层结构 。

   - 随机投影 (Random Projection)：通过高斯矩阵或稀疏矩阵将高维空间的点投影到低维空间 。

   - 流形学习 (Manifold Learning)：
     - 等距映射 (Isomap)：通过估计每个点及其邻居之间的测地距离来嵌入高维空间到低维空间 。
     - t-分布随机邻域嵌入 (t-distributed Stochastic Neighbor Embedding, t-SNE)：将高维数据嵌入到二维或三维空间，以便进行可视化 。

   - 字典学习 (Dictionary Learning)：学习数据的表示，通过加权和重构原始特征 。

   - 独立成分分析 (Independent Component Analysis, ICA)：将混合的信号分离成独立成分，常用于信号处理 。

   - 隐含狄利克雷分配 (Latent Dirichlet Allocation, LDA)：通过学习未观察到的元素来解释数据集的结构，常用于文本数据 。

2. 聚类算法 (Clustering Algorithms):

   - k均值聚类 (k-Means Clustering)：将数据分成k个簇，通过最小化每个簇内的变异性来优化分组 。

   - 层次聚类 (Hierarchical Clustering)：创建数据的层次结构，以形成聚类 。

   - DBSCAN (Density-Based Spatial Clustering of Applications with Noise)：基于密度的聚类算法，能够识别任意形状的簇，并处理噪声点 。

3. 特征提取 (Feature Extraction):

   - 自动编码器 (Autoencoders)：一种神经网络，通过层次化的表示学习原始特征 。

4. 生成对抗网络 (Generative Adversarial Networks, GANs)：由两个神经网络组成，一个生成数据，另一个判别数据，常用于生成接近真实的数据或进行异常检测 。
