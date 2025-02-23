# Python高级特性 - 装饰器
# 这个模块展示了Python中装饰器的使用，这是Java中没有的特性

"""
装饰器是Python中的一个重要特性，它允许我们修改函数或类的行为
相当于Java中的注解（Annotation）的加强版，但更加灵活和强大
"""

# 1. 基本装饰器
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"执行函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完成")
        return result
    return wrapper

# 使用装饰器
@log_execution
def greet(name):
    print(f"Hello, {name}!")

# 2. 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def print_message(message):
    print(message)

# 3. 类装饰器
class Timer:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数 {self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@Timer
def expensive_operation():
    print("执行耗时操作...")

# 4. 多个装饰器的组合
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def format_text(text):
    return text

# 运行示例
if __name__ == "__main__":
    print("=== 装饰器示例 ===")
    
    print("\n1. 基本装饰器示例：")
    greet("Alice")
    
    print("\n2. 带参数的装饰器示例：")
    print_message("这条消息会重复3次")
    
    print("\n3. 类装饰器示例：")
    expensive_operation()
    expensive_operation()
    
    print("\n4. 多个装饰器组合示例：")
    result = format_text("Hello World")
    print(result)  # 输出: <b><i>Hello World</i></b>