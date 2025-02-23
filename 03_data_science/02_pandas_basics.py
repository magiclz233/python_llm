# 数据科学基础 - Pandas入门
# 这个模块展示了Pandas的基本用法，Pandas是Python中用于数据分析的核心库

import pandas as pd
import numpy as np

# 1. 创建数据结构
def create_data_structures():
    print("=== 1. 数据结构创建示例 ===")
    # 创建Series（一维数据结构）
    series = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(f"Series示例:\n{series}\n")
    
    # 创建DataFrame（二维数据结构）
    df = pd.DataFrame({
        '姓名': ['张三', '李四', '王五'],
        '年龄': [25, 30, 35],
        '城市': ['北京', '上海', '广州']
    })
    print(f"DataFrame示例:\n{df}\n")
    
    # 从字典创建DataFrame
    dates = pd.date_range('20230101', periods=6)
    df2 = pd.DataFrame(np.random.randn(6, 4), 
                      index=dates,
                      columns=list('ABCD'))
    print(f"带日期索引的DataFrame:\n{df2}")

# 2. 数据查看和选择
def data_inspection():
    print("\n=== 2. 数据查看和选择示例 ===")
    # 创建示例数据
    df = pd.DataFrame({
        '姓名': ['张三', '李四', '王五', '赵六'],
        '年龄': [25, 30, 35, 40],
        '城市': ['北京', '上海', '广州', '深圳'],
        '工资': [10000, 20000, 15000, 25000]
    })
    
    # 基本信息查看
    print(f"数据基本信息:\n{df.info()}\n")
    print(f"数据统计描述:\n{df.describe()}\n")
    
    # 数据选择
    print(f"选择'姓名'列:\n{df['姓名']}\n")
    print(f"选择前两行:\n{df.head(2)}\n")
    print(f"条件筛选（年龄>30的记录）:\n{df[df['年龄'] > 30]}")

# 3. 数据处理和清洗
def data_processing():
    print("\n=== 3. 数据处理和清洗示例 ===")
    # 创建包含缺失值的数据
    df = pd.DataFrame({
        '姓名': ['张三', '李四', None, '赵六'],
        '年龄': [25, np.nan, 35, 40],
        '城市': ['北京', '上海', '广州', None]
    })
    print(f"原始数据（包含缺失值）:\n{df}\n")
    
    # 处理缺失值
    print(f"删除包含缺失值的行:\n{df.dropna()}\n")
    print(f"填充缺失值:\n{df.fillna({'姓名': '未知', '年龄': df['年龄'].mean(), '城市': '未知'})}")

# 4. 数据分组和聚合
def grouping_aggregation():
    print("\n=== 4. 数据分组和聚合示例 ===")
    # 创建销售数据
    df = pd.DataFrame({
        '部门': ['销售', '技术', '销售', '技术', '市场', '市场'],
        '年份': [2022, 2022, 2023, 2023, 2022, 2023],
        '收入': [100, 150, 200, 180, 120, 160]
    })
    print(f"原始数据:\n{df}\n")
    
    # 按部门分组
    dept_group = df.groupby('部门')['收入'].agg(['mean', 'sum'])
    print(f"各部门收入统计:\n{dept_group}\n")
    
    # 按部门和年份分组
    dept_year_group = df.groupby(['部门', '年份'])['收入'].sum()
    print(f"各部门各年份收入:\n{dept_year_group}")

# 5. 数据合并和连接
def merging_joining():
    print("\n=== 5. 数据合并和连接示例 ===")
    # 创建员工基本信息
    employees = pd.DataFrame({
        '工号': ['001', '002', '003', '004'],
        '姓名': ['张三', '李四', '王五', '赵六'],
        '部门': ['销售', '技术', '市场', '销售']
    })
    
    # 创建工资信息
    salaries = pd.DataFrame({
        '工号': ['001', '002', '003', '004'],
        '基本工资': [8000, 12000, 10000, 8000],
        '奖金': [2000, 3000, 2000, 1500]
    })
    
    # 合并数据
    print(f"员工基本信息:\n{employees}\n")
    print(f"工资信息:\n{salaries}\n")
    
    # 使用merge合并
    result = pd.merge(employees, salaries, on='工号')
    print(f"合并后的完整信息:\n{result}")

# 运行所有示例
if __name__ == "__main__":
    create_data_structures()
    data_inspection()
    data_processing()
    grouping_aggregation()
    merging_joining()