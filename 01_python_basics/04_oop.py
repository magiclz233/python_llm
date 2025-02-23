# 面向对象编程示例
# 本示例将展示Python中类的定义和使用，以及面向对象编程的核心概念
# 对比Java：Python的类定义更简洁，但核心概念（封装、继承、多态）是一致的

# 1. 基本类定义
class Animal:
    """动物基类
    
    对比Java：
    - Python使用class关键字定义类，但不需要public等访问修饰符
    - Python的构造函数固定为__init__
    - self参数相当于Java中的this
    """
    
    # 类变量（静态变量）
    species_count = 0
    
    def __init__(self, name, species):
        # 实例变量
        self.name = name
        self.species = species
        Animal.species_count += 1
    
    def make_sound(self):
        """发出声音（抽象方法）"""
        raise NotImplementedError("子类必须实现此方法")
    
    @classmethod
    def get_species_count(cls):
        """获取物种数量（类方法）"""
        return cls.species_count

# 2. 继承
class Dog(Animal):
    """狗类，继承自Animal"""
    
    def __init__(self, name, breed):
        # 调用父类构造函数
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        return f"{self.name}：汪汪！"
    
    def fetch(self, item):
        """特有方法"""
        return f"{self.name}去捡{item}了"

# 3. 多态
class Cat(Animal):
    """猫类，继承自Animal"""
    
    def __init__(self, name):
        super().__init__(name, species="Cat")
    
    def make_sound(self):
        return f"{self.name}：喵喵！"

# 4. 封装（使用属性装饰器）
class BankAccount:
    """银行账户类
    
    展示Python中的封装特性，使用@property装饰器实现getter/setter
    """
    
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # 使用下划线表示私有属性
        self._balance = balance
    
    @property
    def balance(self):
        """余额getter"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """余额setter，包含验证逻辑"""
        if value < 0:
            raise ValueError("余额不能为负数")
        self._balance = value

# 当作为主程序运行时执行的代码
if __name__ == "__main__":
    # 测试继承和多态
    dog = Dog("旺财", "金毛")
    cat = Cat("咪咪")
    
    # 多态调用
    animals = [dog, cat]
    for animal in animals:
        print(animal.make_sound())
    
    # 测试特有方法
    print(dog.fetch("球"))  # 输出：旺财去捡球了
    
    # 测试类方法
    print(f"当前动物数量：{Animal.get_species_count()}")  # 输出：2
    
    # 测试封装
    account = BankAccount("1234567890")
    account.balance = 1000  # 使用setter
    print(f"账户余额：{account.balance}")  # 使用getter
    
    try:
        account.balance = -100  # 尝试设置负数余额
    except ValueError as e:
        print(f"错误：{e}")