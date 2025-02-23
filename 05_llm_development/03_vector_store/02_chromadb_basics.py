import chromadb
import os
from dotenv import load_dotenv
from typing import List, Dict

# 加载环境变量
load_dotenv()

class ChromaDBManager:
    def __init__(self, persist_directory: str = "chroma_db"):
        """初始化ChromaDB客户端"""
        self.client = chromadb.PersistentClient(path=persist_directory)

    def create_collection(self, collection_name: str) -> chromadb.Collection:
        """创建或获取已存在的集合"""
        try:
            # 尝试创建新集合
            collection = self.client.create_collection(name=collection_name)
            print(f"创建新集合：{collection_name}")
        except ValueError:
            # 如果集合已存在，则获取它
            collection = self.client.get_collection(name=collection_name)
            print(f"获取已存在的集合：{collection_name}")
        return collection

    def add_documents(self, collection: chromadb.Collection,
                     documents: List[str],
                     metadatas: List[Dict] = None,
                     ids: List[str] = None) -> None:
        """向集合中添加文档"""
        if ids is None:
            ids = [str(i) for i in range(len(documents))]
        if metadatas is None:
            metadatas = [{} for _ in documents]

        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"添加了 {len(documents)} 个文档到集合中")

    def query_documents(self, collection: chromadb.Collection,
                       query_texts: List[str],
                       n_results: int = 2,
                       where: Dict = None) -> Dict:
        """查询文档"""
        return collection.query(
            query_texts=query_texts,
            n_results=n_results,
            where=where
        )

def main():
    # 创建ChromaDB管理器实例
    db_manager = ChromaDBManager()

    # 示例1：创建集合
    print("\n示例1：创建和管理集合")
    collection = db_manager.create_collection("tutorial_collection")

    # 示例2：添加文档
    print("\n示例2：添加文档")
    documents = [
        "向量数据库是一种专门用于存储和检索向量的数据库系统",
        "ChromaDB是一个开源的向量数据库，专注于AI应用",
        "向量检索可以用于文本相似度搜索和推荐系统",
        "元数据过滤可以提高检索的精确度"
    ]
    metadatas = [
        {"type": "definition", "category": "database"},
        {"type": "product", "category": "database"},
        {"type": "application", "category": "search"},
        {"type": "technique", "category": "search"}
    ]
    db_manager.add_documents(collection, documents, metadatas)

    # 示例3：基本查询
    print("\n示例3：基本查询")
    query = ["什么是向量数据库？"]
    results = db_manager.query_documents(collection, query)
    print("查询结果：")
    for i, doc in enumerate(results['documents'][0]):
        print(f"文档 {i+1}: {doc}")
        print(f"距离: {results['distances'][0][i]}")

    # 示例4：带元数据过滤的查询
    print("\n示例4：带元数据过滤的查询")
    where_filter = {"category": "search"}
    filtered_results = db_manager.query_documents(
        collection,
        query_texts=["检索技术"],
        where=where_filter
    )
    print("过滤后的查询结果：")
    for i, doc in enumerate(filtered_results['documents'][0]):
        print(f"文档 {i+1}: {doc}")
        print(f"元数据: {filtered_results['metadatas'][0][i]}")

if __name__ == "__main__":
    main()