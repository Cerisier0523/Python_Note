import math
# height,weight = eval(input("请输入身高和体重："))
# bmi = weight/(height**2)
# height, weight = map(float, input("请输入身高和体重：").split())
height = float(input("请输入身高：(厘米)"))/100
weight = float(input("请输入体重：(公斤)"))
bmi = weight/math.pow(height,2)
print("bmi是:{:.2f}".format(bmi))
if bmi < 18.5:
    print("偏瘦")
elif bmi >= 18.5 and bmi <= 25:
    print("正常")
elif bmi >= 25 and bmi <= 30:
    print("偏胖")
else:
    print("肥胖")
