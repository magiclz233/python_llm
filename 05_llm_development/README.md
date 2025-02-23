# LLM应用开发学习指南

本模块专注于大语言模型（LLM）应用开发，特别是使用Langchain框架进行实践。

## 学习路径

### 1. OpenAI API基础 (01_openai_basics)
- OpenAI API密钥配置和环境设置
- ChatCompletion API使用
- 模型参数调优
    在OpenAI API中，模型参数调优主要包括以下几个关键参数：
    1. temperature（温度）：控制输出的随机性，取值0-2之间。值越高，回答越随机创新；值越低，回答越确定和集中。
    2. top_p（核采样）：另一种控制输出随机性的方法，与temperature类似但工作方式不同。通常设置0.1-1之间。
    3. max_tokens（最大令牌数）：控制回答的最大长度。
    4. presence_penalty（存在惩罚）：控制模型谈论新主题的倾向，正值使模型更倾向于讨论新话题。
    5. frequency_penalty（频率惩罚）：降低模型重复使用相同词语的倾向。
    6. n（返回数量）：指定为同一输入生成多少个候选回答。
    7. stop（停止序列）：指定在何处停止生成，可以是字符串或字符串数组。
    这些参数的合理调整可以帮助我们获得更好的模型输出效果。建议在实际应用中根据具体需求进行测试和调整。
- 基础对话应用开发

### 2. Langchain框架基础 (02_langchain_basics)
- Langchain核心概念
- LLMChain和PromptTemplate
- 内存管理和对话历史
- 工具和Agent使用
    

### 3. 向量数据库与检索增强 (03_vector_store)
- 文本向量化基础
- ChromaDB使用指南
- 文档加载和分块
- 相似度检索与问答系统

### 4. LlamaIndex应用开发 (04_llamaindex)
- LlamaIndex核心概念
- 文档索引构建
- 查询引擎开发
- 自定义检索策略

### 5. LLM应用开发实践 (05_llm_applications)
- 智能对话机器人开发
- 混合检索问答系统
- Agent工具开发
- RAG应用优化

## 项目实战
- 构建个性化知识库问答系统（基于LangChain）
- 开发智能文档助手（基于LlamaIndex）
- 实现混合增强Agent系统（LangChain + LlamaIndex）

## 学习建议
1. 确保已安装所有必要依赖（见根目录requirements.txt）
2. 按照模块顺序循序渐进学习
3. 每个示例代码都要动手实践
4. 注意API密钥的安全使用
5. 多参考官方文档和最佳实践

## 参考资源
- [Langchain官方文档](https://python.langchain.com/)
- [OpenAI API文档](https://platform.openai.com/docs)
- [ChromaDB文档](https://docs.trychroma.com/)

祝您学习愉快！