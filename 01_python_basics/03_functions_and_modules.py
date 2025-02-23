# 函数和模块示例
# 本示例将展示Python中函数的定义和使用，以及模块的基本概念
# 对比Java：Python的函数更加灵活，支持默认参数、可变参数、关键字参数等特性

# 1. 基本函数定义
def greet(name):
    """简单的问候函数
    
    Args:
        name (str): 要问候的人名
    
    Returns:
        str: 问候语
    """
    return f"你好，{name}！"

# 2. 默认参数
# Python支持默认参数，这在Java中需要通过方法重载实现
def greet_with_title(name, title="先生/女士"):
    return f"尊敬的{title} {name}，您好！"

# 3. 可变参数
# 类似Java的可变参数(...)
def sum_numbers(*numbers):
    """计算任意数量参数的和"""
    return sum(numbers)

# 4. 关键字参数
def create_person(**properties):
    """创建一个包含任意属性的人"""
    return properties

# 5. 模块级变量
APP_NAME = "Python学习"
APP_VERSION = "1.0.0"

# 6. 模块级函数
def get_app_info():
    """获取应用信息"""
    return f"{APP_NAME} v{APP_VERSION}"

# 当作为主程序运行时执行的代码
if __name__ == "__main__":
    # 测试基本函数
    print(greet("张三"))  # 输出：你好，张三！
    
    # 测试默认参数
    print(greet_with_title("李四"))  # 使用默认title
    print(greet_with_title("王五", "教授"))  # 自定义title
    
    # 测试可变参数
    print(sum_numbers(1, 2, 3, 4, 5))  # 输出：15
    
    # 测试关键字参数
    person = create_person(name="张三", age=25, city="北京")
    print(person)  # 输出：{'name': '张三', 'age': 25, 'city': '北京'}
    
    # 测试模块函数
    print(get_app_info())  # 输出：Python学习 v1.0.0