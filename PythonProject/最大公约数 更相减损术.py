a = int(eval(input("第一个数:")))
b = int(eval(input("第二个数:")))

while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print("最大公约数是：{0}".format(a))