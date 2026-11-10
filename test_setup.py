import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-flash",                      # 关键：模型名
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",        # 关键：指向 DeepSeek
    temperature=0.7,
)

resp = llm.invoke("你好，介绍一下你自己")
print(resp.content)