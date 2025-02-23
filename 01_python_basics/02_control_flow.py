# Python基础 - 控制流程
# 这个模块展示了Python中的控制流程语句，并与Java进行对比

"""
与Java的主要区别：
1. Python使用缩进来表示代码块，而不是花括号{}
2. Python没有switch语句，但有更灵活的match语句（Python 3.10+）
3. Python的for循环主要用于迭代，而不是计数
4. Python有列表推导式，这是Java中没有的特性
"""

# 1. if语句
def if_statement_demo(score):
    # Python的if语句不需要括号，使用缩进表示代码块
    if score >= 90:    # 在Java中: if (score >= 90) {
        grade = 'A'
    elif score >= 80:  # 在Java中: else if (score >= 80) {
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    
    # 条件表达式（三元运算符）
    result = "通过" if score >= 60 else "不通过"  # 在Java中: result = score >= 60 ? "通过" : "不通过";
    
    print(f"分数: {score}, 等级: {grade}, 结果: {result}")

# 2. for循环
def for_loop_demo():
    # 遍历列表
    fruits = ['苹果', '香蕉', '橙子']
    print("\n遍历列表：")
    for fruit in fruits:    # 在Java中: for (String fruit : fruits) {
        print(fruit)
    
    # 使用range生成数字序列
    print("\n使用range：")
    for i in range(3):     # 在Java中: for (int i = 0; i < 3; i++) {
        print(f"计数: {i}")
    
    # 带索引的遍历
    print("\n带索引的遍历：")
    for index, fruit in enumerate(fruits):  # Java中需要手动维护索引
        print(f"索引 {index}: {fruit}")
    
    # 列表推导式 - Python特有特性
    squares = [x**2 for x in range(5)]  # 生成平方数列表
    print(f"\n使用列表推导式生成平方数: {squares}")

# 3. while循环
def while_loop_demo():
    print("\nwhile循环示例：")
    count = 0
    while count < 3:    # 在Java中: while (count < 3) {
        print(f"计数: {count}")
        count += 1      # Python中没有count++的语法
    
    # break和continue的使用
    print("\nbreak和continue示例：")
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num == 2:
            continue    # 跳过2
        if num == 4:
            break       # 遇到4时退出循环
        print(num)

# 4. match语句（Python 3.10+）
def match_statement_demo(command):
    # match语句类似于Java的switch，但更强大
    print(f"\nmatch语句示例，命令: {command}")
    match command.lower():    # 在Java中使用switch
        case "start":
            print("开始执行")
        case "stop":
            print("停止执行")
        case "restart":
            print("重新启动")
        case _:              # 默认情况，相当于Java的default
            print("未知命令")

# 运行示例
if __name__ == "__main__":
    print("=== Python控制流程示例 ===")
    
    print("\n1. if语句示例")
    if_statement_demo(85)
    
    print("\n2. for循环示例")
    for_loop_demo()
    
    print("\n3. while循环示例")
    while_loop_demo()
    
    print("\n4. match语句示例")
    match_statement_demo("start")
    match_statement_demo("unknown")