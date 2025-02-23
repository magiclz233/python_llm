# 异常处理示例
# 本示例将展示Python中的异常处理机制
# 对比Java：Python的异常处理更简洁，但基本概念（try-catch）是一致的

# 1. 基本异常处理
def divide(a, b):
    """除法运算，演示基本的异常处理"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零！")
        return None

# 2. 多个异常处理
def process_data(data):
    """处理数据，演示多个异常的处理"""
    try:
        # 尝试将输入转换为整数并进行计算
        number = int(data)
        result = 100 / number
        return result
    except ValueError:
        print("错误：输入必须是数字！")
    except ZeroDivisionError:
        print("错误：输入不能为零！")
    except Exception as e:
        # 捕获其他所有异常
        print(f"发生未知错误：{str(e)}")
    finally:
        # 类似Java中的finally，总是执行
        print("数据处理完成")

# 3. 自定义异常
class InvalidAgeError(Exception):
    """自定义异常：年龄无效"""
    def __init__(self, age, message="年龄必须在0-150岁之间"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def verify_age(age):
    """验证年龄，演示自定义异常的使用"""
    if not (0 <= age <= 150):
        raise InvalidAgeError(age)
    return f"年龄{age}验证通过"

# 4. 异常的传播
def outer_function():
    """演示异常的传播和捕获"""
    try:
        middle_function()
    except Exception as e:
        print(f"外层函数捕获到异常：{str(e)}")

def middle_function():
    """中间函数，传递异常"""
    inner_function()

def inner_function():
    """内层函数，产生异常"""
    raise ValueError("这是一个内部错误")

# 当作为主程序运行时执行的代码
if __name__ == "__main__":
    # 测试基本异常处理
    print(divide(10, 2))  # 输出：5.0
    print(divide(10, 0))  # 输出错误信息
    
    # 测试多个异常处理
    process_data("10")    # 正常执行
    process_data("abc")   # 数字格式错误
    process_data("0")     # 除零错误
    
    # 测试自定义异常
    try:
        print(verify_age(25))    # 正常情况
        print(verify_age(200))   # 触发自定义异常
    except InvalidAgeError as e:
        print(f"错误：{e.message}，输入的年龄：{e.age}")
    
    # 测试异常传播
    outer_function()