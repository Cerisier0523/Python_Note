try:
    num1,num2 = eval(input("请输入两个数字:"))
    if num1>=num2:
         if num1 % num2==0:
            print("{0}是{1}的{2:.0f}倍".format(num1,num2,num1/num2))
         else :
             print("无关系")
    elif num2>num1:
        if num2 % num1 == 0:
            print("{0}是{1}的{2:.0f}倍".format(num2,num1,num2/num1))
        else :
            print("无关系")
except SyntaxError :
    print("请输入整数")
except TypeError :
    print("请输入整数")