import torch

# 1. 创建张量(Tensor Creation)
# 1.1 从列表生成
tensor_1d = torch.tensor([1, 2, 3, 4])
tensor_2d = torch.tensor([[1, 2], [3, 4]])

# 1.2 特殊张量
# 2行3列全0
zeros_t = torch.zeros((2, 3))
# print(zeros_t)
# 全1
ones_t = torch.ones((2, 3))
# print(ones_t)
# 全部填充5
full_t = torch.full((2, 3), 5)
# print(full_t)
# 3阶单位矩阵
eye_t = torch.eye(3)
# print(eye_t)
# 起步、终点、步长(注意: PyTorch的步长必须是整数)
arange_t = torch.arange(0, 10, 2)
# print(arange_t)
# 0-1均匀生成5个点
linspace_t = torch.linspace(0, 1, 5)
# print(linspace_t)
# [0, 1)均匀随机(生成3行4列)
rand_t = torch.rand(3, 4)
# print(rand_t)
# 标准正态随机
randn_t = torch.randn(3, 4)
# print(randn_t)


# 2. 形状与变形(Shape and Reshaping)
print("tensor_1d 形状:", tensor_1d.shape)
print("tensor_1d 维度:", tensor_1d.dim())
print("tensor_1d 元素总数:", tensor_1d.numel())

# reshape vs view: view() 要求张量在内存中连续, reshape() 更灵活
reshape_t = tensor_2d.reshape(4, 1)
view_t = tensor_2d.view(4, 1)
# 摊平成一堆
flat_t = tensor_2d.flatten()


# 3. 索引与切片 (Indexing and Slicing)
# 提取单个元素 (返回0维张量)
val1 = tensor_1d[0]
# print(val1)
# 一维切片
slice_t = tensor_1d[1:3]
# print(slice_t)
# 二维张量定位 (第0行第1列)
val2 = tensor_2d[0, 1]
# print(val2)
# 二维张量切片 (所有行, 第0列)
col0 = tensor_2d[:, 0]
# print(col0)
# 布尔索引 / 条件筛选
mask_t = tensor_1d[tensor_1d > 2]
# print(mask_t)


# 4. 数学运算
t_plus = tensor_1d + 1
# print(t_plus)
# 对应位置元素相加
t_add = tensor_1d + tensor_1d
# print(t_add)
sum_val = torch.sum(tensor_1d)
# print(sum_val)
# 求平均值 (注意: 必须转为浮点数才能求平均值)
mean_val = torch.mean(tensor_1d.float())
# print(mean_val)
max_val = torch.max(tensor_1d).values
min_val = torch.min(tensor_1d).values
# 求平方根 / 正弦
sqrt_t = torch.sqrt(tensor_1d.float())
sin_t = torch.sin(tensor_1d.float())
# 求标准差
std_val = torch.std(tensor_1d.float())
# print(std_val)

# 矩阵乘法(注: '*'是逐元素乘, '@'或torch.matmul()才是矩阵乘法)
dot_val = torch.matmul(tensor_2d, tensor_2d)
# print(dot_val)
dot_val_short = tensor_2d @ tensor_2d
# print(dot_val_short)


# 5. 张量拼接与堆叠 (Concatenation and Stacking)
# 垂直拼接 (沿着维度0上下文拼接)
concat_v = torch.cat([tensor_2d, tensor_2d], dim=0)
# print(concat_v)
# 水平拼接 (沿着维度1左右拼接)
concat_h = torch.cat([tensor_2d, tensor_2d], dim=1)
# print(concat_h)
# 堆叠 (注意: stack会增加一个新的维度, 这里会变成三位张量)
stack_t = torch.stack([tensor_2d, tensor_2d], dim=0)
# print(stack_t)


# 6. PyTorch核心特性: 设备管理与自动求导 (Device & Autograd)
# 6.1 设备管理 (CPU vs GPU)
device = 'cuda' if torch.cuda.is_available() else "cpu"
tensor_gpu = tensor_1d.to(device)
print(f"当前使用的设备: {device}")

# 6.2 自动求导 (Autograd)
# requires_grad=True 告诉PyTorch追踪该张量上的所有运算, 用于计算梯度
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x ** 2 + 2 * x
# 反向传播求梯度 (相当于求导 dy / dx)
y.sum().backward()
# 打印梯度 (数学原理: y = x ^ 2 + 2x的导数2x+2)
print("梯度 x.grad:", x.grad)