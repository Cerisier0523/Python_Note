a = int(eval(input("第一个数:")))
b = int(eval(input("第二个数:")))

smaller = min(a,b)
for i in range(smaller,1,-1):
    if a%i==0 and b%i==0:
       print("最大公约数是：{0}".format(i))
       break