import json

with open("E:/应用/学习计划/练习/demo1.md", "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("## ")

slices = []
for p in parts:
    if p.strip() != "":
        slices.append({"content": p.strip()})

with open("E:/应用/学习计划/练习/slices.json", "w", encoding="utf-8") as f:
    json.dump(slices, f, ensure_ascii=False, indent=2)

print("切好了，共", len(slices), "片")
