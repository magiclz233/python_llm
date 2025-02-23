from openai import OpenAI
import numpy as np
from typing import List
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化OpenAI客户端
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_embedding(text: str, model="text-embedding-ada-002") -> List[float]:
    """使用OpenAI API获取文本的向量表示"""
    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding

def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """计算两个向量之间的余弦相似度"""
    v1_np = np.array(v1)
    v2_np = np.array(v2)
    return np.dot(v1_np, v2_np) / (np.linalg.norm(v1_np) * np.linalg.norm(v2_np))

def find_most_similar(query: str, texts: List[str]) -> tuple[str, float]:
    """在文本列表中找到与查询最相似的文本"""
    # 获取查询文本的向量表示
    query_embedding = get_embedding(query)
    
    # 获取所有文本的向量表示
    text_embeddings = [get_embedding(text) for text in texts]
    
    # 计算相似度并找到最相似的文本
    similarities = [cosine_similarity(query_embedding, text_embedding) 
                   for text_embedding in text_embeddings]
    max_similarity_idx = np.argmax(similarities)
    
    return texts[max_similarity_idx], similarities[max_similarity_idx]

def main():
    # 示例文本
    texts = [
        "机器学习是人工智能的一个子领域",
        "深度学习是机器学习的一种方法",
        "自然语言处理是人工智能的重要应用",
        "计算机视觉主要处理图像和视频数据"
    ]
    
    # 示例1：获取文本向量
    print("\n示例1：文本向量化")
    text = texts[0]
    embedding = get_embedding(text)
    print(f"文本: {text}")
    print(f"向量维度: {len(embedding)}")
    print(f"向量前5个维度: {embedding[:5]}")
    
    # 示例2：计算文本相似度
    print("\n示例2：文本相似度计算")
    text1 = "机器学习和深度学习"
    text2 = "深度学习是机器学习的一种方法"
    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)
    similarity = cosine_similarity(embedding1, embedding2)
    print(f"文本1: {text1}")
    print(f"文本2: {text2}")
    print(f"相似度: {similarity:.4f}")
    
    # 示例3：相似文本检索
    print("\n示例3：相似文本检索")
    query = "什么是机器学习？"
    most_similar_text, similarity = find_most_similar(query, texts)
    print(f"查询: {query}")
    print(f"最相似的文本: {most_similar_text}")
    print(f"相似度: {similarity:.4f}")

if __name__ == "__main__":
    main()