# 向量数据库与检索增强学习模块

本模块专注于向量数据库的使用和检索增强技术的实践，主要包含以下内容：

## 1. 文本向量化基础（01_text_embedding.py）
- 使用OpenAI Embedding API进行文本向量化
- 不同Embedding模型的对比和选择
- 向量相似度计算方法
- 向量化最佳实践

## 2. ChromaDB基础操作（02_chromadb_basics.py）
- ChromaDB环境配置
- 集合（Collection）的创建和管理
- 文档存储和检索操作
- 元数据过滤和查询

## 3. 文档处理（03_document_processing.py）
- 支持多种格式的文档加载器
- 文本分块策略和实现
- 块大小和重叠度的优化
- 文档预处理和清洗

## 4. 检索问答系统（04_qa_system.py）
- 构建基于向量数据库的问答系统
- 相似度检索策略实现
- 上下文增强的回答生成
- 系统性能优化

## 5. 高级应用（05_advanced_features.py）
- 混合检索策略
- 动态索引更新
- 多模态数据处理
- 检索结果排序和过滤

## 使用说明
1. 确保已安装所需依赖：
```bash
pip install chromadb openai langchain numpy
```

2. 配置必要的环境变量：
- OPENAI_API_KEY：用于访问OpenAI API
- CHROMADB_PATH：向量数据库存储路径

3. 按顺序运行示例代码，每个示例都包含详细的注释说明

## 注意事项
- 向量数据库文件会占用较大存储空间，注意定期清理
- 建议使用SSD存储向量数据库以提升性能
- 大规模文档处理时注意内存使用
- 及时更新索引以保持数据一致性

## 参考资源
- [ChromaDB官方文档](https://docs.trychroma.com/)
- [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings)
- [LangChain文档 - 向量存储](https://python.langchain.com/docs/modules/data_connection/vectorstores/)