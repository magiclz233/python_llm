# Python高级特性 - 多线程和并发
# 这个模块展示了Python中多线程和并发的使用，以及与Java的对比

"""
与Java的主要区别：
1. Python有GIL（全局解释器锁），这影响了多线程的性能
2. Python的threading模块比Java的Thread类使用更简单
3. Python提供了多进程（multiprocessing）作为并行计算的替代方案
4. Python的concurrent.futures提供了类似Java ExecutorService的功能
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing

# 1. 基本线程示例
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"线程 {self.name} 开始运行")
        time.sleep(2)
        print(f"线程 {self.name} 运行完成")

# 2. 线程同步
class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:  # 相当于Java的synchronized块
            current = self.count
            time.sleep(0.1)  # 模拟耗时操作
            self.count = current + 1

# 3. 线程池
def worker_function(x):
    print(f"处理数据: {x}")
    time.sleep(1)
    return x * x

# 4. 多进程示例
def process_worker(name):
    print(f"进程 {name} 开始运行")
    time.sleep(1)
    print(f"进程 {name} 运行完成")

# 5. 生产者-消费者模式
def producer(queue):
    for i in range(5):
        print(f"生产数据: {i}")
        queue.put(i)
        time.sleep(0.5)

def consumer(queue):
    while True:
        try:
            data = queue.get(timeout=2)
            print(f"消费数据: {data}")
        except:
            break

# 运行示例
if __name__ == "__main__":
    print("=== 多线程和并发示例 ===")

    # 1. 基本线程示例
    print("\n1. 基本线程示例：")
    threads = [MyThread(f"Thread-{i}") for i in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # 2. 线程同步示例
    print("\n2. 线程同步示例：")
    counter = Counter()
    threads = [threading.Thread(target=counter.increment) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"最终计数: {counter.count}")

    # 3. 线程池示例
    print("\n3. 线程池示例：")
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(worker_function, range(5)))
    print(f"线程池处理结果: {results}")

    # 4. 多进程示例
    print("\n4. 多进程示例：")
    processes = [multiprocessing.Process(target=process_worker, args=(f"Process-{i}",))
                for i in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # 5. 生产者-消费者示例
    print("\n5. 生产者-消费者示例：")
    queue = multiprocessing.Queue()
    prod = multiprocessing.Process(target=producer, args=(queue,))
    cons = multiprocessing.Process(target=consumer, args=(queue,))

    prod.start()
    cons.start()
    prod.join()
    cons.join()