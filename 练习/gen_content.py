"""
工具 A：内容生成脚本 gen_content.py
输入一个主题，调用 DeepSeek API，输出一段文案。

这是「内容流水线 agent」的第一个真工具。
用到已学：input/int、函数、文件读写、异常处理、字典、requests、JSON。
"""

import requests

API_URL = "https://api.deepseek.com/chat/completions"
KEY_FILE = "E:/应用/学习计划/练习/my_key.txt"


def 读密钥():
    """从 my_key.txt 读出 API key（文件只有一行）"""
    with open(KEY_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


def 生成文案(主题):
    """把主题发给 DeepSeek，拿回它写的文案"""
    key = 读密钥()

    # 请求头：Authorization 是"身份验证"，证明你付过钱
    请求头 = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json",
    }

    # 请求体：要发给服务器的数据，是字典（会自动转成 JSON）
    # 模型名照官方文档填（2026-11 核实）：deepseek-flash 便宜快，deepseek-v4-pro 更强更贵
    请求体 = {
        "model": "deepseek-flash",#model不能更改这是官方规定的键
        "messages": [
            {"role": "user", "content": "请围绕主题「" +主题 + "」写一段 100 字左右的短文。"}
        ],#用+把主题套进去
        "stream": False,
        "thinking": {"type": "disabled"},   # 关掉思考模式，只要最终文案
    }

    # 发 POST 请求：把问题交出去，拿回回答
    响应 = requests.post(API_URL, json=请求体, headers=请求头, timeout=30)#将dee seek传回来的结果赋值给响应

    # 先看状态码，把常见错误翻译成人话（延续异常处理那一课）
    if 响应.status_code == 401:
        raise Exception("key 不对或没填对，检查 my_key.txt")
    if 响应.status_code == 402:
        raise Exception("余额不足，去 platform.deepseek.com 充值")

    # 响应转成字典，再一层层取出模型回复的文字
    数据 = 响应.json()#将响应内的东西以json的格式转换成字典
    return 数据["choices"][0]["message"]["content"]#数据类型可以查询官方文档


# ===== 主程序 =====
主题 = input("请输入主题: ")
try:
    文案 = 生成文案(主题)
    print("===== 生成的文案 =====")
    print(文案)
except FileNotFoundError:
    print("没找到 my_key.txt——请先创建它，把 DeepSeek API key 粘贴进去保存。")
except Exception as e:
    print("调用失败:", type(e).__name__, e)
