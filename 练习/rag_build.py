"""
工具：rag_build.py —— RAG 建库脚本（阶段一，跑一次）
读切片 → 用本地 embedding 模型转向量 → 存进 chromadb 向量库

环境问题说明：chromadb 默认 embedding 模型要从 huggingface 下载，国内网络超时。
这里改用电脑上已有的本地模型 bge-small-en-v1.5（离线可用），所以多一个 embedding_function 参数。
"""

import json
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# 本地 embedding 模型路径（你电脑上已有的，不用下载）
MODEL_PATH = "C:/Users/21272/.cache/huggingface/hub/models--BAAI--bge-small-en-v1.5/snapshots/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"

# ① 读切片（昨天 split_notes.py 的产物）
with open("E:/应用/学习计划/练习/slices.json", "r", encoding="utf-8") as f:
    slices = json.load(f)

# ② 连上本地向量库，建一个叫 notes 的集合
#    embedding_function 指定用本地模型转向量（绕开网络下载）
client = chromadb.PersistentClient(path="E:/应用/学习计划/练习/rag_db")
embedding_fn = SentenceTransformerEmbeddingFunction(model_name=MODEL_PATH)
collection = client.get_or_create_collection(
    name="notes",
    embedding_function=embedding_fn,
)

# ③ 把每片存进去
ids = []
docs = []
for i, s in enumerate(slices):
    ids.append(str(i))
    docs.append(s["content"])

collection.add(ids=ids, documents=docs)

print("建库完成，存了", collection.count(), "片")
