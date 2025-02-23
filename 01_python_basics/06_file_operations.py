# 文件操作示例
# 本示例将展示Python中的文件操作
# 对比Java：Python的文件操作更简单直观，不需要显式关闭文件（使用with语句自动处理）

# 1. 文本文件写入
def write_text_file(filename, content):
    """写入文本文件示例"""
    try:
        # 使用with语句自动处理文件关闭
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"成功写入文件：{filename}")
    except IOError as e:
        print(f"写入文件失败：{str(e)}")

# 2. 文本文件读取
def read_text_file(filename):
    """读取文本文件示例"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # 读取全部内容
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")
    except IOError as e:
        print(f"读取文件失败：{str(e)}")

# 3. 按行读取文件
def read_file_lines(filename):
    """按行读取文件示例"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # 读取所有行到列表
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")

# 4. 文件追加内容
def append_to_file(filename, content):
    """向文件追加内容示例"""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(content)
        print(f"成功追加内容到文件：{filename}")
    except IOError as e:
        print(f"追加内容失败：{str(e)}")

# 5. 二进制文件操作
def copy_binary_file(source, destination):
    """复制二进制文件示例"""
    try:
        with open(source, 'rb') as src_file:
            with open(destination, 'wb') as dest_file:
                # 每次读取1MB
                buffer_size = 1024 * 1024
                while True:
                    buffer = src_file.read(buffer_size)
                    if not buffer:
                        break
                    dest_file.write(buffer)
        print(f"成功复制文件：{source} -> {destination}")
    except IOError as e:
        print(f"复制文件失败：{str(e)}")

# 6. 文件和目录操作
import os
import shutil

def file_directory_operations():
    """文件和目录操作示例"""
    # 创建目录
    os.makedirs("test_dir", exist_ok=True)
    print("创建目录：test_dir")
    
    # 列出目录内容
    files = os.listdir(".")
    print("当前目录内容：", files)
    
    # 检查文件是否存在
    if os.path.exists("test.txt"):
        print("文件test.txt存在")
    
    # 获取文件信息
    if os.path.exists("test_dir"):
        stats = os.stat("test_dir")
        print(f"目录信息：\n大小：{stats.st_size}字节\n创建时间：{stats.st_ctime}")
    
    # 重命名文件或目录
    try:
        os.rename("test_dir", "new_test_dir")
        print("重命名目录：test_dir -> new_test_dir")
    except OSError:
        print("重命名失败")
    
    # 删除文件和目录
    try:
        # 删除文件
        if os.path.exists("test.txt"):
            os.remove("test.txt")
            print("删除文件：test.txt")
        
        # 删除目录（包括内容）
        if os.path.exists("new_test_dir"):
            shutil.rmtree("new_test_dir")
            print("删除目录：new_test_dir")
    except OSError as e:
        print(f"删除操作失败：{str(e)}")

# 当作为主程序运行时执行的代码
if __name__ == "__main__":
    # 测试文本文件操作
    write_text_file("test.txt", "这是一个测试文件\n包含多行内容\n你好，Python！")
    
    content = read_text_file("test.txt")
    print("\n读取的文件内容：")
    print(content)
    
    append_to_file("test.txt", "\n这是追加的内容")
    
    lines = read_file_lines("test.txt")
    print("\n按行读取的内容：")
    for line in lines:
        print(f"行：{line.strip()}")
    
    # 测试二进制文件操作
    # 创建一个示例二进制文件
    with open("test.bin", "wb") as f:
        f.write(b"Hello, Binary World!")
    
    copy_binary_file("test.bin", "test_copy.bin")
    
    # 测试文件和目录操作
    file_directory_operations()