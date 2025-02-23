from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.base import Chain
from typing import Dict, List
from dotenv import load_dotenv
import time

"""
LangChain自定义Chain示例

本示例演示如何创建和使用自定义Chain：
1. 基本自定义Chain的创建
2. 错误处理和重试机制
3. 性能优化和缓存

确保在运行前：
1. 已安装必要的包：pip install langchain langchain-openai python-dotenv
2. 在.env文件中设置了OPENAI_API_KEY
"""

# 加载环境变量
load_dotenv()

class CodeReviewChain(Chain):
    """自定义代码审查Chain"""
    
    llm: ChatOpenAI
    code_review_prompt: PromptTemplate
    suggestion_prompt: PromptTemplate
    
    @property
    def input_keys(self) -> List[str]:
        return ["code"]
    
    @property
    def output_keys(self) -> List[str]:
        return ["review", "suggestions"]
    
    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        # 代码审查
        review_chain = LLMChain(llm=self.llm, prompt=self.code_review_prompt)
        review = review_chain.run(code=inputs["code"])
        
        # 改进建议
        suggestion_chain = LLMChain(llm=self.llm, prompt=self.suggestion_prompt)
        suggestions = suggestion_chain.run(review=review)
        
        return {"review": review, "suggestions": suggestions}


class RetryChain(Chain):
    """带有重试机制的Chain"""
    
    chain: Chain
    max_retries: int = 3
    delay: float = 1.0
    
    @property
    def input_keys(self) -> List[str]:
        return self.chain.input_keys
    
    @property
    def output_keys(self) -> List[str]:
        return self.chain.output_keys
    
    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        for attempt in range(self.max_retries):
            try:
                return self.chain(inputs)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise e
                time.sleep(self.delay * (attempt + 1))


def demonstrate_custom_chain():
    """演示自定义Chain的使用"""
    # 创建提示模板
    code_review_prompt = PromptTemplate(
        input_variables=["code"],
        template="请对以下Python代码进行代码审查：\n{code}\n请指出代码中的问题和可能的改进点。"
    )
    
    suggestion_prompt = PromptTemplate(
        input_variables=["review"],
        template="基于以下代码审查结果：\n{review}\n请提供具体的改进建议和最佳实践。"
    )
    
    # 创建自定义Chain
    code_review_chain = CodeReviewChain(
        llm=ChatOpenAI(temperature=0),
        code_review_prompt=code_review_prompt,
        suggestion_prompt=suggestion_prompt
    )
    
    # 示例代码
    sample_code = """
    def calculate_average(numbers):
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)
    """
    
    # 运行Chain
    result = code_review_chain({"code": sample_code})
    print("=== 代码审查结果 ===")
    print(result["review"])
    print("\n=== 改进建议 ===")
    print(result["suggestions"])


def demonstrate_retry_chain():
    """演示带重试机制的Chain"""
    # 创建一个可能失败的Chain
    unstable_prompt = PromptTemplate(
        input_variables=["query"],
        template="请回答以下问题：{query}"
    )
    unstable_chain = LLMChain(
        llm=ChatOpenAI(temperature=0.7),
        prompt=unstable_prompt
    )
    
    # 包装成带重试的Chain
    retry_chain = RetryChain(
        chain=unstable_chain,
        max_retries=3,
        delay=1.0
    )
    
    # 测试重试机制
    try:
        result = retry_chain.run("什么是Python的GIL？")
        print("\n=== 重试Chain结果 ===")
        print(result)
    except Exception as e:
        print(f"\n执行失败：{str(e)}")


def demonstrate_chain_optimization():
    """演示Chain的性能优化"""
    from langchain.cache import InMemoryCache
    import langchain
    
    # 启用内存缓存
    langchain.cache = InMemoryCache()
    
    # 创建Chain
    prompt = PromptTemplate(
        input_variables=["concept"],
        template="请用一句话解释{concept}这个编程概念。"
    )
    chain = LLMChain(
        llm=ChatOpenAI(temperature=0),
        prompt=prompt
    )
    
    # 测试缓存效果
    print("\n=== 测试缓存效果 ===")
    start_time = time.time()
    first_result = chain.run("Python装饰器")
    first_time = time.time() - start_time
    print(f"第一次运行（无缓存）：{first_time:.2f}秒")
    
    start_time = time.time()
    second_result = chain.run("Python装饰器")
    second_time = time.time() - start_time
    print(f"第二次运行（有缓存）：{second_time:.2f}秒")
    print(f"缓存加速比：{first_time/second_time:.2f}x")


def main():
    print("=== 演示自定义Chain的使用 ===")
    demonstrate_custom_chain()
    
    print("\n=== 演示重试机制 ===")
    demonstrate_retry_chain()
    
    print("\n=== 演示Chain优化 ===")
    demonstrate_chain_optimization()


if __name__ == "__main__":
    main()