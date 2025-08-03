a = int(eval(input("第一个数:")))
b = int(eval(input("第二个数:")))

while b!=0:
    a,b=b,a%b
print("最大公约数是：{0}".format(a))