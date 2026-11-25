with open("E:/应用/学习计划/练习/text.txt","w",encoding="utf-8")as f:
    f.write("第一句")
with open("E:/应用/学习计划/练习/text.txt","r",encoding="utf-8")as f:
    x=f.read()
    print(x)
with open("E:/应用/学习计划/练习/text.txt","w",encoding="utf-8")as f:
    f.write("第二句")
with open("E:/应用/学习计划/练习/text.txt","r",encoding="utf-8")as f:
    x=f.read()
    print(x)
with open("E:/应用/学习计划/练习/text.txt","a",encoding="utf-8")as f:
    f.write("第三句")
with open("E:/应用/学习计划/练习/text.txt","r",encoding="utf-8")as f:
    x=f.read()
    print(x)
