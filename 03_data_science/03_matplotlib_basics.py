# 数据科学基础 - Matplotlib入门
# 这个模块展示了Matplotlib的基本用法，这是Python中最常用的数据可视化库

import matplotlib.pyplot as plt
import numpy as np

# 1. 基本折线图
def line_plot_demo():
    print("=== 1. 基本折线图示例 ===")
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)')
    plt.plot(x, y2, label='cos(x)')
    plt.title('正弦和余弦函数')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# 2. 散点图
def scatter_plot_demo():
    print("\n=== 2. 散点图示例 ===")
    np.random.seed(42)
    x = np.random.normal(0, 1, 100)
    y = 2 * x + np.random.normal(0, 0.5, 100)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.5)
    plt.title('散点图示例')
    plt.xlabel('X 值')
    plt.ylabel('Y 值')
    plt.grid(True)
    plt.show()

# 3. 柱状图
def bar_plot_demo():
    print("\n=== 3. 柱状图示例 ===")
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values)
    plt.title('柱状图示例')
    plt.xlabel('类别')
    plt.ylabel('数值')
    plt.show()

# 4. 子图和多图
def subplot_demo():
    print("\n=== 4. 子图示例 ===")
    plt.figure(figsize=(12, 8))
    
    # 2x2的子图布局
    # 1. 折线图
    plt.subplot(2, 2, 1)
    x = np.linspace(0, 5, 100)
    plt.plot(x, np.sin(x))
    plt.title('正弦函数')
    
    # 2. 散点图
    plt.subplot(2, 2, 2)
    x = np.random.normal(0, 1, 50)
    y = np.random.normal(0, 1, 50)
    plt.scatter(x, y)
    plt.title('随机散点')
    
    # 3. 柱状图
    plt.subplot(2, 2, 3)
    x = ['A', 'B', 'C']
    y = [1, 2, 3]
    plt.bar(x, y)
    plt.title('简单柱状图')
    
    # 4. 饼图
    plt.subplot(2, 2, 4)
    sizes = [30, 20, 50]
    labels = ['A', 'B', 'C']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('饼图')
    
    plt.tight_layout()
    plt.show()

# 5. 高级定制
def advanced_customization():
    print("\n=== 5. 高级定制示例 ===")
    # 创建数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # 创建自定义样式的图表
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'r--', linewidth=2, label='sin(x)')
    plt.plot(x, y2, 'b-.', linewidth=2, label='cos(x)')
    
    # 添加标题和标签
    plt.title('自定义样式图表', fontsize=14, fontweight='bold')
    plt.xlabel('X 轴', fontsize=12)
    plt.ylabel('Y 轴', fontsize=12)
    
    # 自定义图例
    plt.legend(loc='upper right', frameon=True, shadow=True)
    
    # 自定义网格
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 添加文本注释
    plt.text(5, 0.5, '重要点', fontsize=12, 
             bbox=dict(facecolor='yellow', alpha=0.5))
    
    plt.show()

# 运行所有示例
if __name__ == "__main__":
    line_plot_demo()
    scatter_plot_demo()
    bar_plot_demo()
    subplot_demo()
    advanced_customization()