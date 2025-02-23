from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Union
import os
from pathlib import Path

class DocumentProcessor:
    def __init__(self):
        """初始化文档处理器"""
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

    def load_document(self, file_path: Union[str, Path]) -> List[str]:
        """加载不同格式的文档"""
        file_path = Path(file_path)
        if file_path.suffix == '.pdf':
            loader = PyPDFLoader(str(file_path))
            documents = loader.load()
            return [doc.page_content for doc in documents]
        elif file_path.suffix == '.txt':
            loader = TextLoader(str(file_path))
            documents = loader.load()
            return [doc.page_content for doc in documents]
        else:
            raise ValueError(f"不支持的文件格式：{file_path.suffix}")

    def split_text(self, text: str) -> List[str]:
        """将文本分割成较小的块"""
        return self.text_splitter.split_text(text)

    def preprocess_text(self, text: str) -> str:
        """文本预处理：清理和标准化"""
        # 移除多余的空白字符
        text = ' '.join(text.split())
        # 移除特殊字符（根据需要保留一些标点符号）
        text = ''.join(char for char in text if char.isprintable())
        return text

def main():
    processor = DocumentProcessor()

    # 示例1：加载和预处理文本
    print("\n示例1：文本加载和预处理")
    sample_text = """这是一个示例文本。\n\n它包含一些  多余的空格和\t制表符。

我们需要对其进行预处理。"""
    processed_text = processor.preprocess_text(sample_text)
    print("原始文本：")
    print(sample_text)
    print("\n预处理后的文本：")
    print(processed_text)

    # 示例2：文本分块
    print("\n示例2：文本分块")
    long_text = """
    向量数据库是一种专门用于存储和检索向量的数据库系统。它在机器学习和人工智能领域有广泛应用。
    主要用途包括相似度搜索、推荐系统、图像检索等。向量数据库的核心功能是高效地进行向量相似度计算。
    常见的向量数据库包括Milvus、Faiss、ChromaDB等。这些数据库都支持高维向量的存储和快速检索。
    在实际应用中，向量数据库通常与深度学习模型配合使用，用于存储和检索特征向量。
    """
    chunks = processor.split_text(long_text)
    print(f"分块数量：{len(chunks)}")
    for i, chunk in enumerate(chunks, 1):
        print(f"\n块 {i}:")
        print(chunk)

    # 示例3：文档加载（需要实际的PDF或TXT文件）
    print("\n示例3：文档加载")
    print("注意：需要提供实际的PDF或TXT文件路径才能运行此示例")
    print("支持的文件格式：.pdf, .txt")

if __name__ == "__main__":
    main()