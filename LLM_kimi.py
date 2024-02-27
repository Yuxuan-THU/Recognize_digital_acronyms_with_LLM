from openai import OpenAI
from pathlib import Path


def get_file_correct():
    file_path = "./acronyms_correct.txt"
    lines = Path(file_path).read_text(encoding="utf-8").split("\n")
    return lines

def get_file_wrong():
    file_path = "./acronyms_wrong.txt"
    lines = Path(file_path).read_text(encoding="utf-8").split("\n")
    return lines

client = OpenAI(
    api_key="sk-7EYzGzVMk3u0BtJ2MS4gCOcURNhtV7XxEuMg1FIOle7fvyvH",
    base_url="https://api.moonshot.cn/v1",
)

correct_ones = get_file_correct()
print(correct_ones)
correct_str = ', '.join(correct_ones)

wrong_ones = get_file_wrong()
print(wrong_ones)
wrong_str = ', '.join(wrong_ones)

completion = client.chat.completions.create(

  model="moonshot-v1-128k",
  messages=[
    {
        "role": "system",
        "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一些涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
    },
    {
        "role": "user",
        "content": f"定义一种话语类型为“数字缩略语”，形如 {correct_str} 的词语满足该定义，形如{wrong_str}的词语不符合该定义。"
                   f"你可以注意到，符合定义的词语中会包含数字，而这个数字背后代表着特定的含义，如“四个全面”中的“四”代表着“全面建设社会主义现代化国家，全面深化改革，全面依法治国，全面从严治党”，所以“四个全面”符合定义。“兵农合一”中的“一”不代表特定的词汇，所以不符合定义。"
                   f"请问“”满足数字缩略语的定义吗？请回答是或否。"
    }
  ],
  temperature=1,
)

print(completion.choices[0].message)
