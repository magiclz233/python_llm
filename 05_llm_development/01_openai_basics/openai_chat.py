from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载环境变量中的API密钥
load_dotenv()

def init_openai_client():
    """初始化OpenAI客户端
    
    确保在.env文件中设置了OPENAI_API_KEY
    可选：在.env中设置OPENAI_BASE_URL来自定义API地址
    """
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    )
    return client

def simple_chat(client, user_message, model=None, temperature=0.7):
    """简单的对话函数
    
    Args:
        client: OpenAI客户端实例
        user_message: 用户输入的消息
        model: 使用的模型名称，如果为None则从环境变量读取
        temperature: 温度参数，控制响应的随机性
    
    Returns:
        assistant的回复内容
    """
    try:
        model = model or os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"调用API时发生错误: {str(e)}")
        return None

def chat_with_memory(client, messages, model=None, temperature=0.7):
    """带上下文记忆的对话函数
    
    Args:
        client: OpenAI客户端实例
        messages: 消息历史列表
        model: 使用的模型名称，如果为None则从环境变量读取
        temperature: 温度参数
    
    Returns:
        assistant的回复内容和更新后的消息历史
    """
    try:
        model = model or os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=messages,
            stream=True  # 启用流式响应
        )
        
        # 用于存储完整的响应文本
        full_response = ""
        
        # 逐个处理流式响应的内容
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(content, end='', flush=True)  # 实时打印内容
                full_response += content
        
        print()  # 打印换行
        messages.append({"role": "assistant", "content": full_response})
        return full_response, messages
    except Exception as e:
        print(f"\n调用API时发生错误: {str(e)}")
        return None, messages

def interactive_chat(client, system_message=None, model=None, temperature=0.7):
    """交互式对话函数
    
    Args:
        client: OpenAI客户端实例
        system_message: 系统提示信息，用于设置AI助手的角色和行为
        model: 使用的模型名称，如果为None则从环境变量读取
        temperature: 温度参数
    """
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    
    print("=== 开始交互式对话 ===")
    print('输入问题开始对话，直接按回车键结束对话')
    
    while True:
        user_input = input("\n用户: ").strip()
        if not user_input:  # 如果用户输入为空，结束对话
            print("\n=== 对话结束 ===")
            break
        
        messages.append({"role": "user", "content": user_input})
        response, messages = chat_with_memory(client, messages, model, temperature)
        
        if response:
            print(f"\nAI: {response}")
        else:
            print("\nAI: 抱歉，处理您的问题时出现错误。")
            break

def main():
    # 初始化客户端
    client = init_openai_client()
    
    # # 简单对话示例
    # print("=== 简单对话示例 ===")
    # response = simple_chat(client, "你好，请介绍一下自己")
    # print(f"AI: {response}\n")
    
    # # 带记忆的对话示例
    # print("=== 带记忆的对话示例 ===")
    # messages = [
    #     {"role": "system", "content": "你是一个友好的AI助手，擅长解释技术概念。"},
    #     {"role": "user", "content": "请解释一下什么是大语言模型？"}
    # ]
    
    # response, messages = chat_with_memory(client, messages)
    # print(f"AI: {response}\n")
    
    # # 继续对话，AI会记住上下文
    # messages.append({"role": "user", "content": "这些模型主要应用在哪些场景？"})
    # response, messages = chat_with_memory(client, messages)
    # print(f"AI: {response}\n")
    
    # 交互式对话示例
    interactive_chat(client, "你是一个友好的AI助手，擅长解释各种问题。")

if __name__ == "__main__":
    main()