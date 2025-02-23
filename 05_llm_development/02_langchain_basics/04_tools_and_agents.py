from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.tools import Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

"""
LangChain工具和Agent示例

本示例演示如何使用Langchain的工具和Agent：
1. 内置工具使用
2. 自定义工具创建
3. Agent的使用和配置

确保在运行前：
1. 已安装必要的包：pip install langchain langchain-openai python-dotenv wikipedia-api
2. 在.env文件中设置了OPENAI_API_KEY
"""

# 加载环境变量
load_dotenv()

def demonstrate_built_in_tools():
    """演示内置工具的使用"""
    # 初始化语言模型
    llm = ChatOpenAI(temperature=0)

    # 加载内置工具
    tools = load_tools(
        ["llm-math", "wikipedia"],  # 使用数学计算和维基百科工具
        llm=llm
    )

    # 初始化Agent
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # 使用Agent回答问题
    question = "Python的发明者是谁？他在哪一年发明了Python？"
    response = agent.run(question)
    print("\n回答：", response)


def create_custom_tool():
    """创建自定义工具"""
    # 创建一个简单的代码生成器
    prompt = PromptTemplate(
        input_variables=["task"],
        template="为以下任务生成Python代码：\n{task}\n只返回代码，不要解释。"
    )

    # 创建用于生成代码的Chain
    code_chain = LLMChain(
        llm=ChatOpenAI(temperature=0),
        prompt=prompt
    )

    # 定义工具
    return Tool(
        name="Python代码生成器",
        description="当你需要生成Python代码时使用这个工具。输入应该是对所需代码的描述。",
        func=lambda x: code_chain.run(x)
    )


def demonstrate_custom_tools():
    """演示自定义工具的使用"""
    # 创建自定义工具
    code_generator = create_custom_tool()

    # 初始化Agent
    agent = initialize_agent(
        [code_generator],
        ChatOpenAI(temperature=0),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # 使用Agent生成代码
    task = "创建一个函数，接受一个列表作为参数，返回列表中所有偶数的和。"
    response = agent.run(task)
    print("\n生成的代码：\n", response)


def demonstrate_agent_configuration():
    """演示Agent的高级配置"""
    # 初始化语言模型
    llm = ChatOpenAI(temperature=0)

    # 加载多个工具
    tools = [
        create_custom_tool(),  # 自定义代码生成器
        *load_tools(["llm-math"], llm=llm)  # 数学计算工具
    ]

    # 配置Agent
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=3,  # 限制最大迭代次数
        early_stopping_method="generate"  # 设置提前停止方法
    )

    # 测试复杂任务
    task = "1. 生成一个计算斐波那契数列第n项的函数\n2. 然后计算这个函数在n=10时的返回值"
    response = agent.run(task)
    print("\n执行结果：\n", response)


def main():
    print("=== 演示内置工具的使用 ===")
    demonstrate_built_in_tools()

    print("\n=== 演示自定义工具的使用 ===")
    demonstrate_custom_tools()

    print("\n=== 演示Agent的高级配置 ===")
    demonstrate_agent_configuration()


if __name__ == "__main__":
    main()