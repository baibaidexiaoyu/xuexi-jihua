shuliang = int(input("输入数量: "))
jiage = 30
tol = 0
for i in range(1, shuliang + 1):
    if i == 2:
        price = jiage * 0.5
    elif i == 10:
        price = 0
    else:
        price = jiage
    tol = tol + price
print(tol)
