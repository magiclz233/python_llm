from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

"""
LangChain中的LLMChain示例

本示例演示如何使用LLMChain：
1. 创建和使用LLMChain
2. 链式调用
3. 批量处理

确保在运行前：
1. 已安装必要的包：pip install langchain langchain-openai python-dotenv
2. 在.env文件中设置了OPENAI_API_KEY
"""

# 加载环境变量
load_dotenv()

def demonstrate_basic_chain():
    """演示基本的LLMChain使用"""
    # 创建提示模板
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="给我5个关于{topic}的编程练习题目。"
    )

    # 初始化语言模型
    llm = ChatOpenAI(
        model_name=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        temperature=0.7,
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        )

    # 创建chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # 运行chain
    result = chain.run("Python装饰器")
    print("基本Chain输出：\n", result)


def demonstrate_chain_composition():
    """演示链式组合"""
    # 创建第一个chain：生成练习题
    exercise_prompt = PromptTemplate(
        input_variables=["topic"],
        template="给我一道{topic}的编程练习题。"
    )
    exercise_chain = LLMChain(
        llm=ChatOpenAI(temperature=0.7),
        prompt=exercise_prompt
    )

    # 创建第二个chain：生成答案
    solution_prompt = PromptTemplate(
        input_variables=["question"],
        template="为下面的编程题目提供详细的Python解决方案：\n{question}"
    )
    solution_chain = LLMChain(
        llm=ChatOpenAI(temperature=0.3),
        prompt=solution_prompt
    )

    # 链式调用
    exercise = exercise_chain.run("Python列表推导式")
    solution = solution_chain.run(question=exercise)

    print("练习题：\n", exercise)
    print("\n解决方案：\n", solution)


def demonstrate_batch_processing():
    """演示批量处理"""
    # 创建用于解释概念的chain
    explain_prompt = PromptTemplate(
        input_variables=["concept"],
        template="用一句话解释{concept}这个Python概念。"
    )
    explain_chain = LLMChain(
        llm=ChatOpenAI(temperature=0.5),
        prompt=explain_prompt
    )

    # 准备多个输入
    concepts = [
        "装饰器",
        "生成器",
        "上下文管理器"
    ]

    # 批量处理
    results = explain_chain.apply([
        {"concept": concept} for concept in concepts
    ])

    # 打印结果
    for concept, result in zip(concepts, results):
        print(f"{concept}：{result['text']}")


def main():
    print("=== 演示基本的LLMChain使用 ===")
    demonstrate_basic_chain()

    print("\n=== 演示链式组合 ===")
    demonstrate_chain_composition()

    print("\n=== 演示批量处理 ===")
    demonstrate_batch_processing()


if __name__ == "__main__":
    main()