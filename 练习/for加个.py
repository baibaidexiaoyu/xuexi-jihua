shuliang=int(input("输入数量: "))
jiage=30
tol=0
for i in range(1,shuliang+1):
    if i==2:
        shu=jiage*0.5
    elif i==10:
        shu=0
    else:
        shu=jiage
    tol=tol+shu
print(tol)
