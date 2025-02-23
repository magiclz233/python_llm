from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv

"""
LangChain对话历史管理示例

本示例演示如何使用Langchain的内存组件：
1. 基本对话历史管理
2. 滑动窗口记忆
3. 自定义记忆组件

确保在运行前：
1. 已安装必要的包：pip install langchain langchain-openai python-dotenv
2. 在.env文件中设置了OPENAI_API_KEY
"""

# 加载环境变量
load_dotenv()

def demonstrate_basic_memory():
    """演示基本的对话历史管理"""
    # 创建带有记忆的对话链
    conversation = ConversationChain(
        llm=ChatOpenAI(temperature=0.7),
        memory=ConversationBufferMemory()
    )

    # 进行多轮对话
    print("=== 第一轮对话 ===")
    response1 = conversation.predict(input="你好，我想学习Python，请给我一些建议。")
    print("AI：", response1)

    print("\n=== 第二轮对话 ===")
    response2 = conversation.predict(input="考虑到我是初学者，应该先学习哪些基础概念？")
    print("AI：", response2)

    # 查看记忆中存储的对话历史
    print("\n当前对话历史：")
    print(conversation.memory.buffer)


def demonstrate_window_memory():
    """演示滑动窗口记忆"""
    # 创建只记住最近2轮对话的对话链
    conversation = ConversationChain(
        llm=ChatOpenAI(temperature=0.7),
        memory=ConversationBufferWindowMemory(k=2)
    )

    # 进行多轮对话
    questions = [
        "Python中的列表和元组有什么区别？",
        "那字典和集合呢？",
        "这些数据结构各自适用于什么场景？",
        "你能总结一下前面讲的要点吗？"  # 由于窗口大小限制，模型只能记住最近两轮对话
    ]

    for i, question in enumerate(questions, 1):
        print(f"\n=== 第{i}轮对话 ===")
        response = conversation.predict(input=question)
        print("问：", question)
        print("AI：", response)


def demonstrate_custom_memory():
    """演示自定义记忆组件"""
    from langchain.memory import CombinedMemory
    from langchain.memory import ConversationSummaryMemory

    # 创建组合记忆：使用对话缓冲和对话摘要
    buffer_memory = ConversationBufferMemory()
    summary_memory = ConversationSummaryMemory(llm=ChatOpenAI())
    combined_memory = CombinedMemory(memories=[buffer_memory, summary_memory])

    # 创建使用组合记忆的对话链
    conversation = ConversationChain(
        llm=ChatOpenAI(temperature=0.7),
        memory=combined_memory
    )

    # 进行对话
    print("=== 使用组合记忆进行对话 ===")
    responses = [
        conversation.predict(input="请介绍Python的异常处理机制。"),
        conversation.predict(input="try-except块如何使用？"),
        conversation.predict(input="finally子句的作用是什么？")
    ]

    for i, response in enumerate(responses, 1):
        print(f"\n第{i}轮回复：", response)


def main():
    print("=== 演示基本的对话历史管理 ===")
    demonstrate_basic_memory()

    print("\n=== 演示滑动窗口记忆 ===")
    demonstrate_window_memory()

    print("\n=== 演示自定义记忆组件 ===")
    demonstrate_custom_memory()


if __name__ == "__main__":
    main()