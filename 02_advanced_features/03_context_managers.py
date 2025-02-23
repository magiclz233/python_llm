# Python高级特性 - 上下文管理器
# 这个模块展示了Python中上下文管理器的使用，这是Java中try-with-resources的更强大版本

"""
与Java的主要区别：
1. Python的with语句比Java的try-with-resources更加灵活
2. Python可以通过类或生成器方式实现上下文管理器
3. Python的上下文管理器可以管理任何资源，不仅限于IO
"""

# 1. 基本文件操作上下文管理器
def file_operations():
    print("1. 基本文件操作示例：")
    # 使用with语句自动处理文件关闭
    with open('example.txt', 'w') as f:
        f.write('Hello, Context Manager!')
    
    with open('example.txt', 'r') as f:
        content = f.read()
        print(f"读取文件内容: {content}")

# 2. 自定义上下文管理器（类方式）
class Timer:
    """计时器上下文管理器"""
    def __init__(self, description):
        self.description = description
    
    def __enter__(self):
        import time
        self.start = time.time()
        print(f"开始 {self.description}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end = time.time()
        print(f"{self.description} 完成，耗时: {end - self.start:.2f}秒")
        return False  # 返回False则不会吞掉异常

# 3. 使用contextlib实现上下文管理器（装饰器方式）
from contextlib import contextmanager

@contextmanager
def temporary_attribute(obj, name, value):
    """临时修改对象属性的上下文管理器"""
    old_value = getattr(obj, name, None)
    setattr(obj, name, value)
    try:
        yield
    finally:
        if old_value is None:
            delattr(obj, name)
        else:
            setattr(obj, name, old_value)

# 4. 嵌套使用上下文管理器
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        print(f"连接到数据库 {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"关闭数据库 {self.db_name} 连接")
        return False

class Transaction:
    def __enter__(self):
        print("开始事务")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("提交事务")
        else:
            print(f"回滚事务: {exc_type.__name__}")
        return False

# 运行示例
if __name__ == "__main__":
    print("=== 上下文管理器示例 ===")
    
    # 1. 文件操作示例
    file_operations()
    
    # 2. 计时器示例
    print("\n2. 计时器上下文管理器示例：")
    with Timer("耗时操作"):
        import time
        time.sleep(1)  # 模拟耗时操作
    
    # 3. 临时属性修改示例
    print("\n3. 临时属性修改示例：")
    class Person:
        name = "原始名字"
    
    p = Person()
    print(f"原始名字: {p.name}")
    with temporary_attribute(p, 'name', '临时名字'):
        print(f"临时名字: {p.name}")
    print(f"恢复后的名字: {p.name}")
    
    # 4. 嵌套上下文管理器示例
    print("\n4. 嵌套上下文管理器示例：")
    try:
        with DatabaseConnection("MyDB") as db:
            with Transaction():
                print("执行数据库操作")
                # 模拟异常
                raise ValueError("操作失败")
    except ValueError:
        print("异常已被捕获")