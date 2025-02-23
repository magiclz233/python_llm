# Python高级特性 - 生成器和迭代器
# 这个模块展示了Python中生成器和迭代器的使用，这些是Java中较为复杂的概念在Python中的简化实现

"""
与Java的主要区别：
1. Python的生成器使用yield关键字，比Java的Iterator实现更简洁
2. Python的迭代器协议更简单，只需要实现__iter__和__next__方法
3. Python的for循环可以直接遍历任何可迭代对象
"""

# 1. 基本生成器
def number_generator(n):
    """生成0到n-1的数字序列"""
    for i in range(n):
        yield i

# 2. 无限生成器
def fibonacci_generator():
    """生成斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 3. 生成器表达式
def generator_expression_demo():
    # 生成器表达式（类似列表推导式，但更节省内存）
    squares = (x * x for x in range(10))
    print("生成器表达式生成的平方数：")
    for square in squares:
        print(square, end=' ')
    print()

# 4. 自定义迭代器
class CountDown:
    """实现一个倒计时迭代器"""
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# 5. yield from 示例
def nested_generator():
    """演示yield from的使用"""
    yield from range(3)  # 等价于: for i in range(3): yield i
    yield from 'ABC'     # 可以yield from任何可迭代对象

# 运行示例
if __name__ == "__main__":
    print("=== 生成器和迭代器示例 ===")
    
    print("\n1. 基本生成器示例：")
    for num in number_generator(5):
        print(num, end=' ')
    print()
    
    print("\n2. 斐波那契数列生成器示例：")
    fib = fibonacci_generator()
    for _ in range(10):
        print(next(fib), end=' ')
    print()
    
    print("\n3. 生成器表达式示例：")
    generator_expression_demo()
    
    print("\n4. 自定义迭代器示例：")
    countdown = CountDown(5)
    for num in countdown:
        print(num, end=' ')
    print()
    
    print("\n5. yield from示例：")
    for item in nested_generator():
        print(item, end=' ')
    print()

    # 生成器的内存效率演示
    print("\n6. 生成器vs列表的内存使用对比：")
    import sys
    list_comp = [x * x for x in range(1000)]
    gen_exp = (x * x for x in range(1000))
    print(f"列表占用内存: {sys.getsizeof(list_comp)} bytes")
    print(f"生成器占用内存: {sys.getsizeof(gen_exp)} bytes")