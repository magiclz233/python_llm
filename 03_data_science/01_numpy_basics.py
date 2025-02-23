# 数据科学基础 - NumPy入门
# 这个模块展示了NumPy的基本用法，NumPy是Python中用于数值计算的核心库

import numpy as np

# 1. 创建数组
def array_creation_demo():
    print("=== 1. 数组创建示例 ===")
    # 从列表创建数组
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"一维数组:\n{arr1}")
    
    # 创建二维数组
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n二维数组:\n{arr2}")
    
    # 特殊数组
    zeros = np.zeros((3, 3))  # 创建3x3的零矩阵
    ones = np.ones((2, 2))    # 创建2x2的单位矩阵
    rand = np.random.rand(2, 3)  # 创建2x3的随机数组
    
    print(f"\n零矩阵:\n{zeros}")
    print(f"\n单位矩阵:\n{ones}")
    print(f"\n随机数组:\n{rand}")

# 2. 数组操作
def array_operations():
    print("\n=== 2. 数组操作示例 ===")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    # 基本属性
    print(f"数组形状: {arr.shape}")
    print(f"数组维度: {arr.ndim}")
    print(f"数组类型: {arr.dtype}")
    
    # 重塑数组
    reshaped = arr.reshape(3, 2)
    print(f"\n重塑后的数组:\n{reshaped}")
    
    # 数组切片
    print(f"\n第一行: {arr[0]}")
    print(f"第二列:\n{arr[:, 1]}")

# 3. 数组计算
def array_calculations():
    print("\n=== 3. 数组计算示例 ===")
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    
    # 基本运算
    print(f"数组相加:\n{arr1 + arr2}")
    print(f"数组相乘:\n{arr1 * arr2}")
    print(f"数组平方:\n{arr1 ** 2}")
    
    # 统计运算
    print(f"\n平均值: {arr1.mean()}")
    print(f"标准差: {arr1.std()}")
    print(f"最大值: {arr1.max()}")
    print(f"最小值: {arr1.min()}")

# 4. 广播机制
def broadcasting_demo():
    print("\n=== 4. 广播机制示例 ===")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    scalar = 2
    
    # 标量运算会广播到整个数组
    print(f"数组乘以标量:\n{arr * scalar}")
    
    # 不同形状数组的广播
    row_vector = np.array([1, 0, 1])
    print(f"\n数组与向量相加:\n{arr + row_vector}")

# 5. 线性代数运算
def linear_algebra_demo():
    print("\n=== 5. 线性代数运算示例 ===")
    # 创建矩阵
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    # 矩阵乘法
    print(f"矩阵乘法:\n{np.dot(A, B)}")
    
    # 计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"\n特征值:\n{eigenvalues}")
    print(f"特征向量:\n{eigenvectors}")

# 运行所有示例
if __name__ == "__main__":
    array_creation_demo()
    array_operations()
    array_calculations()
    broadcasting_demo()
    linear_algebra_demo()