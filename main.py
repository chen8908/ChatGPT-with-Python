
import openai
from config import OPENAI_API_TOKEN
openai.api_key = OPENAI_API_TOKEN

question = input('請輸入詢問問題：')

response = openai.Completion.create(
    engine='text-davinci-003',  # 使用引擎
    prompt=question,  # 提問問題
    max_tokens=128,  # 期望回答字數上限
    temperature=0  # 隨機文字組合，範圍 0～1，預設 0.5，0 表示不隨機，1 表示完全隨機
)

completed_text = response["choices"][0]["text"]
print(completed_text)
