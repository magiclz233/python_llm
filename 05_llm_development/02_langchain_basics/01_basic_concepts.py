from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

"""
LangChain基础概念示例

本示例演示Langchain的核心概念：
1. 模型（Model）：LLM和ChatModel的使用
2. 提示（Prompt）：构建和管理提示
3. 输出解析（Output Parser）：处理模型输出

确保在运行前：
1. 已安装必要的包：pip install langchain langchain-openai python-dotenv
2. 在.env文件中设置了OPENAI_API_KEY
"""

# 加载环境变量
load_dotenv()

def demonstrate_chat_model():
    """演示ChatModel的基本使用"""
    # 初始化ChatOpenAI，设置模型和温度
    chat = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.7
    )

    # 构建消息列表
    messages = [
        SystemMessage(content="你是一个专业的Python教程助手。"),
        HumanMessage(content="请用一句话解释什么是装饰器？")
    ]

    # 获取回复
    response = chat(messages)
    print("ChatModel回复：", response.content)


def demonstrate_prompt_management():
    """演示提示管理"""
    from langchain.prompts import PromptTemplate

    # 创建提示模板
    prompt = PromptTemplate(
        input_variables=["concept"],
        template="请用通俗易懂的语言解释{concept}这个编程概念。"
    )

    # 格式化提示
    formatted_prompt = prompt.format(concept="面向对象编程")
    print("格式化后的提示：", formatted_prompt)


def demonstrate_output_parsing():
    """演示输出解析"""
    from langchain.output_parsers import CommaSeparatedListOutputParser
    from langchain.prompts import PromptTemplate

    # 创建输出解析器
    output_parser = CommaSeparatedListOutputParser()

    # 创建带格式说明的提示模板
    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template="列出Python中的5个内置函数。\n{format_instructions}",
        input_variables=[],
        partial_variables={"format_instructions": format_instructions}
    )

    # 使用ChatModel和解析器
    chat = ChatOpenAI(temperature=0)
    response = chat([HumanMessage(content=prompt.format())])
    
    # 解析输出
    parsed_output = output_parser.parse(response.content)
    print("解析后的输出：", parsed_output)


def main():
    print("=== 演示ChatModel的基本使用 ===")
    demonstrate_chat_model()
    
    print("\n=== 演示提示管理 ===")
    demonstrate_prompt_management()
    
    print("\n=== 演示输出解析 ===")
    demonstrate_output_parsing()


if __name__ == "__main__":
    main()