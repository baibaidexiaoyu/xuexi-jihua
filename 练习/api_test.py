import requests
r=requests.get("http://jsonplaceholder.typicode.com/posts/1",timeout=8)
print("状态码:",r.status_code)
data=r.json()
print("标题:",data["title"])
print("作者编号:",data["userId"])
