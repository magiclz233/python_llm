from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

"""
LangChain文档操作示例

本示例演示如何使用Langchain处理文档：
1. 文档加载器的使用
2. 文本分割器的应用
3. 向量存储和检索

确保在运行前：
1. 已安装必要的包：pip install langchain langchain-openai python-dotenv chromadb pypdf
2. 在.env文件中设置了OPENAI_API_KEY
3. 在当前目录下创建sample_docs文件夹并添加示例文档
"""

# 加载环境变量
load_dotenv()

def demonstrate_document_loading():
    """演示文档加载器的使用"""
    # 加载文本文件
    text_loader = TextLoader("sample_docs/sample.txt")
    text_docs = text_loader.load()
    
    # 加载PDF文件
    pdf_loader = PyPDFLoader("sample_docs/sample.pdf")
    pdf_docs = pdf_loader.load()
    
    print("=== 文本文件加载结果 ===")
    print(f"加载了 {len(text_docs)} 个文档")
    print("第一个文档内容预览：\n", text_docs[0].page_content[:200])
    
    print("\n=== PDF文件加载结果 ===")
    print(f"加载了 {len(pdf_docs)} 页PDF")
    print("第一页内容预览：\n", pdf_docs[0].page_content[:200])


def demonstrate_text_splitting():
    """演示文本分割器的使用"""
    # 创建一个示例文档
    long_text = """
    Python是一种面向对象的解释型编程语言。它具有简单易学的语法特点。
    Python支持多种编程范式，包括面向过程、面向对象和函数式编程。
    Python拥有丰富的标准库和第三方库，可以帮助开发者快速构建应用。
    """
    
    # 使用字符分割器
    char_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=50,
        chunk_overlap=10
    )
    char_splits = char_splitter.split_text(long_text)
    
    # 使用递归字符分割器
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=50,
        chunk_overlap=10
    )
    recursive_splits = recursive_splitter.split_text(long_text)
    
    print("=== 字符分割器结果 ===")
    for i, chunk in enumerate(char_splits, 1):
        print(f"块 {i}: {chunk}")
    
    print("\n=== 递归字符分割器结果 ===")
    for i, chunk in enumerate(recursive_splits, 1):
        print(f"块 {i}: {chunk}")


def demonstrate_vector_store():
    """演示向量存储和检索"""
    # 准备示例文档
    texts = [
        "Python是一种高级编程语言，以其简洁的语法和易读性著称。",
        "Java是一种广泛使用的编程语言，特别适合企业级应用开发。",
        "JavaScript是网页开发中不可或缺的编程语言。",
        "Python的包管理器pip让依赖管理变得简单。"
    ]
    
    # 创建向量存储
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        persist_directory="./vector_store"
    )
    
    # 相似度搜索
    query = "Python的特点是什么？"
    results = vectorstore.similarity_search(
        query=query,
        k=2  # 返回最相关的2条结果
    )
    
    print("=== 向量检索结果 ===")
    print(f"查询：{query}")
    for i, doc in enumerate(results, 1):
        print(f"\n结果 {i}：{doc.page_content}")


def main():
    print("=== 演示文档加载器的使用 ===")
    demonstrate_document_loading()
    
    print("\n=== 演示文本分割器的使用 ===")
    demonstrate_text_splitting()
    
    print("\n=== 演示向量存储和检索 ===")
    demonstrate_vector_store()


if __name__ == "__main__":
    main()