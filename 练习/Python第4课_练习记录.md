# Python 第 4 课 练习记录：异常处理（try/except）

日期：2026-11-26
形式：讲解 + 3 道题 + 概念追问
状态：异常处理已过，进入 API 调用

## 讲解要点

- **异常** = 程序运行时出的错，中文叫"异常"，英文叫 Exception。之前踩过的全是异常：`ValueError`（值不对）、`KeyError`（键不存在）、`TypeError`（类型不对）、`IndexError`（下标越界）、`FileNotFoundError`（文件没找到）
- **try/except 语法**：`try:` 下缩进放可能出错的代码；`except 类型:` 下缩进放"出错后怎么办"。没出错跳过 except，出错跳到 except，两种情况程序都不崩
- **类型必须对上**：`int("abc")` 抛 ValueError，若写 `except KeyError:` 接不住 → 程序照样崩（类型写错 = 等于没写 except）
- **万能兜底**：`except Exception:` 或 `except:` 接住所有错误，不用管类型，零基础/工具脚本够用
- **识别错误类型**：报错最后一行 `类型名: 说明`，冒号前的单词直接抄进 except；看不懂英文也能用

## 三道题成绩

| # | 题目 | 我的答案 | 判定 |
|---|---|---|---|
| 1 | `int("abc")` 配 `except KeyError` 会不会崩 | "接不住会报错，但程序不会崩、会打印继续"——前半对，后半错 | ⚠️ 实测崩了、没打印继续；讲透"异常没接住=程序当场停止，后面代码不执行"后理解 |
| 2 | 补全 int 转换 + 错误类型 | 初用 int 报错 → 换成 str 消除报错；经点破"报错是要接住的信号、不是要消灭的失败"后理解 | ⚠️ 关键思维转弯，见下 |
| 3 | try/except 包住打开文件，文件不存在打印提示 | `try: f=open("lianxi","r",encoding="utf-8")` / `except Exception: print("没有该文件")`，实测输出"没有该文件"、退出码 0 | ✅ 一次跑通（缩进/拼写全对） |

## 核心思维转弯（本课最大收获）

用户原话："我一开始用 int 然后报错了，我想了想用 str 他就没报错，是我没读懂题意了。"

- **其实第一反应是对的**：用 int 触发 ValueError 正是题目要的，报错不是写错了，是"用户输入非数字"这个本来就可能发生的外部情况
- **换 str = 把报警器拆了**：错误消失，但也永远检测不到"输入不是数字"了
- **正确思路**：保留 int，用 try/except 提前准备"出错了怎么办"——错误发生但被接住，程序不崩
- **旧习惯 vs 新思维**：旧"报错=我写错了=消灭它"；新"外部不确定导致的报错=正常=管理它"
- **判断标准**：错误来自外部不确定（用户输入/网络/文件）→ try/except 接住；错误来自自己写错（拼写/缩进/变量名）→ 真该改代码

## 概念追问（已解答）

- "看不懂英文怎么识别错误类型" → 看报错最后一行冒号前的单词，抄进 except；或用 `except Exception:` 万能兜底；常见类型混脸熟即可（ValueError/KeyError/TypeError/IndexError/FileNotFoundError）
- "异常没接住是不是还能继续" → 不能，程序当场终止，后面的代码一行都不跑（实测退出码 1）

## 七、API 调用（11-26 下午）

### 讲解要点

- **API = 用代码"点外卖"**：你的程序发请求（下单）→ 服务器处理后返回响应（外卖）
- **请求里带**：地址 URL + 内容 + 身份密钥（API key）
- **三步走**：`import requests` → `r = requests.get(网址, timeout=8)` → `data = r.json()`
- `r.status_code` 看状态码（200=成功）；`r.json()` 把响应的 JSON 文本转成**字典**（= 昨天 `json.dump` 的反向操作）
- 响应是嵌套字典，取值用昨天练的 `data["title"]` / `data["choices"][0]["message"]["content"]`
- GET = "给我数据"（参数在网址里）；POST = "我给你数据处理"（参数在请求体里，DeepSeek 用 POST）

### API 第一题：api_test.py（GET 免 key 接口）

```python
import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=8)
print("状态码:", r.status_code)
data = r.json()
print("标题:", data["title"])
print("作者编号:", data["userId"])
```

实测输出：状态码 200 / 一行英文标题 / 作者编号 1。commit `493cf26`。

### ⚠️ 新增坑：多个 Python 环境，库装错解释器

- **现象**：命令行测 requests 已装（2.34.2，在 3.13.14），但用户 IDLE 跑 `import requests` 报 `ModuleNotFoundError`
- **根因**：系统有多个 Python。命令行=WorkBuddy 自带 3.13.14（有 requests）；IDLE=用户自己的 3.12.10（`C:\Users\21272\AppData\Local\Programs\Python\Python312\python.exe`，无 requests）。库是装给**某个解释器**的，不是装给电脑的
- **修法**：给谁运行就给谁装——`Python312\python.exe -m pip install requests`（已执行，装好 2.34.2）。用 3.12 实跑用户脚本，输出正确
- **记住**：以后 `ModuleNotFoundError` 先想"是不是装到另一个 Python 去了"；`py -0p` 可列出所有解释器。这也是为什么"我这边能跑你那边不能"——不是代码问题，是环境不同
- **连带教训**：助手说"已装好"要说明**装在哪个解释器**，否则误导用户（这次就发生了）

## 衔接

异常处理、API GET 已过。剩下：API POST（带 key 调 DeepSeek）→ 工具 A `gen_content.py` → Git 远程 push。API key 需用户去 platform.deepseek.com 注册获取（助手无法代做）；key 到手前用免 key 的 jsonplaceholder 接口练 HTTP 流程。
