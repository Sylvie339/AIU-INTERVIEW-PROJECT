import requests

# 1. 配置 Ollama 的 API 地址
API_URL = "http://127.0.0.1:11434/v1/chat/completions"
MODEL_NAME = "qwen2.5:7b"

# 2. 初始化对话历史
messages = [
    {"role": "system", "content": "你是一个有用的AI助手，请用中文回答。"}
]

print("=== 本地千问 CLI 对话 (输入 'quit' 退出) ===")

# 3. 循环对话
while True:
    user_input = input("\n你: ")
    if user_input.lower() == 'quit':
        print("再见！")
        break
        
    messages.append({"role": "user", "content": user_input})

    # 4. 发送请求给 Ollama
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }

    try:
        print("千问正在思考...", end="\r")
        response = requests.post(API_URL, json=payload)
        response.raise_for_status() 
        
        # 5. 提取并打印回复
        data = response.json()
        reply = data['choices'][0]['message']['content']
        
        print(f"千问: {reply}")
        
        messages.append({"role": "assistant", "content": reply})
        
    except Exception as e:
        print(f"\n出错了: {e}")
        print("请检查：1. Ollama 是否在后台运行；2. 模型名称是否正确。")
        messages.pop()