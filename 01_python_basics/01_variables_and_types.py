# Python基础 - 变量和数据类型
# 这个模块展示了Python中的基本数据类型和变量使用，特别标注了与Java的区别

"""
与Java的主要区别：
1. Python是动态类型语言，不需要显式声明变量类型
2. Python的基本数据类型更简单，如数字类型不区分int/long/float
3. Python有特殊的数据类型如元组(tuple)和字典(dict)
"""

# 1. 变量声明和基本类型
# Python不需要声明变量类型，直接赋值即可
def basic_types_demo():
    # 数字类型
    number = 42          # 整数 (在Java中需要写成: int number = 42;)
    pi = 3.14159        # 浮点数 (在Java中需要写成: double pi = 3.14159;)
    complex_num = 1 + 2j # 复数 (Java中没有内置的复数类型)
    
    # 字符串 - Python中的字符串是不可变的，类似Java的String
    name = "Python"      # 可以使用单引号或双引号
    multi_line = """     # 三引号支持多行字符串
    这是多行字符串，
    在Java中需要使用 + 连接多行
    """
    
    # 布尔值 - 注意Python中是True/False，而不是Java中的true/false
    is_python = True
    is_java = False
    
    # 打印各种类型
    print(f"数字类型示例：")
    print(f"整数: {number}, 类型: {type(number)}")
    print(f"浮点数: {pi}, 类型: {type(pi)}")
    print(f"复数: {complex_num}, 类型: {type(complex_num)}")
    print(f"\n字符串示例：")
    print(f"名称: {name}, 类型: {type(name)}")
    print(f"多行字符串:\n{multi_line}")
    print(f"\n布尔值示例：")
    print(f"is_python: {is_python}, 类型: {type(is_python)}")

# 2. Python特有的数据类型
def python_specific_types():
    # 列表 (类似Java的ArrayList)
    numbers = [1, 2, 3, 4, 5]  # 在Java中: List<Integer> numbers = new ArrayList<>();
    mixed = [1, "Python", True] # Python列表可以存储不同类型
    
    # 元组 - 不可变的序列类型（Java中没有直接对应的类型）
    coordinates = (10, 20)
    
    # 字典 (类似Java的HashMap)
    person = {            # 在Java中: Map<String, Object> person = new HashMap<>();
        "name": "Alice",
        "age": 30,
        "is_programmer": True
    }
    
    # 集合 (类似Java的HashSet)
    unique_numbers = {1, 2, 3, 3, 2, 1}  # 重复元素会被自动去除
    
    print(f"\nPython特有类型示例：")
    print(f"列表: {numbers}, 类型: {type(numbers)}")
    print(f"混合类型列表: {mixed}")
    print(f"元组: {coordinates}, 类型: {type(coordinates)}")
    print(f"字典: {person}, 类型: {type(person)}")
    print(f"集合: {unique_numbers}, 类型: {type(unique_numbers)}")

# 3. 类型转换
def type_conversion():
    # Python的类型转换比Java更简单
    number_str = "42"
    number_int = int(number_str)    # 在Java中: Integer.parseInt(numberStr)
    number_float = float(number_str) # 在Java中: Double.parseDouble(numberStr)
    
    # 列表、元组、集合之间的转换
    numbers_list = [1, 2, 3]
    numbers_tuple = tuple(numbers_list)
    numbers_set = set(numbers_list)
    
    print(f"\n类型转换示例：")
    print(f"字符串转整数: {number_str} -> {number_int}")
    print(f"字符串转浮点: {number_str} -> {number_float}")
    print(f"列表转元组: {numbers_list} -> {numbers_tuple}")
    print(f"列表转集合: {numbers_list} -> {numbers_set}")

# 运行示例
if __name__ == "__main__":
    print("=== Python变量和数据类型示例 ===")
    basic_types_demo()
    python_specific_types()
    type_conversion()