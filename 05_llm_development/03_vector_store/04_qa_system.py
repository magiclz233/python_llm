from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from typing import List, Dict
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class QASystem:
    def __init__(self, persist_directory: str = "qa_system_db"):
        """初始化问答系统"""
        self.llm = ChatOpenAI()
        self.embeddings = OpenAIEmbeddings()
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.persist_directory = persist_directory
        self.vectorstore = None
        self.qa_chain = None

    def initialize_vectorstore(self, texts: List[str], metadatas: List[Dict] = None):
        """初始化向量存储"""
        self.vectorstore = Chroma.from_texts(
            texts=texts,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
            metadatas=metadatas
        )
        
        # 创建问答链
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(),
            memory=self.memory,
            return_source_documents=True
        )

    def ask(self, question: str) -> Dict:
        """处理用户问题并返回答案"""
        if not self.qa_chain:
            raise ValueError("请先初始化向量存储！")
        
        response = self.qa_chain({"question": question})
        return {
            "answer": response["answer"],
            "source_documents": response["source_documents"],
            "chat_history": self.memory.chat_memory.messages
        }

def main():
    # 创建问答系统实例
    qa_system = QASystem()

    # 示例1：初始化知识库
    print("\n示例1：初始化知识库")
    documents = [
        "向量数据库是一种专门用于存储和检索向量的数据库系统，主要用于AI和机器学习应用。",
        "ChromaDB是一个开源的向量数据库，它提供了简单易用的API和高效的检索功能。",
        "向量检索的核心是计算向量之间的相似度，常用的方法包括余弦相似度和欧氏距离。",
        "在实际应用中，向量数据库通常与大语言模型配合使用，用于构建智能问答系统。"
    ]
    metadatas = [
        {"source": "intro_doc", "page": 1},
        {"source": "tech_doc", "page": 1},
        {"source": "tech_doc", "page": 2},
        {"source": "application_doc", "page": 1}
    ]
    qa_system.initialize_vectorstore(documents, metadatas)

    # 示例2：单轮问答
    print("\n示例2：单轮问答")
    question = "什么是向量数据库？它有什么用途？"
    response = qa_system.ask(question)
    print(f"问题：{question}")
    print(f"答案：{response['answer']}")
    print("\n参考文档：")
    for doc in response['source_documents']:
        print(f"- 来源：{doc.metadata['source']}，页码：{doc.metadata['page']}")
        print(f"  内容：{doc.page_content}")

    # 示例3：多轮对话
    print("\n示例3：多轮对话")
    questions = [
        "ChromaDB是什么？",
        "它是如何实现向量检索的？"
    ]
    for question in questions:
        response = qa_system.ask(question)
        print(f"\n问题：{question}")
        print(f"答案：{response['answer']}")

if __name__ == "__main__":
    main()