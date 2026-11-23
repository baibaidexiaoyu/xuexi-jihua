price=30
shuliang=input("请输入数量: ")
shuliang=int(shuliang)
if(shuliang<=1):
    total=shuliang*30
elif(shuliang>=2 and shuliang<10):
    total=(shuliang-1)*price+price*0.5
else:
    total=price*(shuliang-2)+price*0.5
print("一共",shuliang,"杯" , "共",total,"元")



