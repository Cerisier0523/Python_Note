number = 9
guess = eval(input("请输入数字:"))
if guess == number:
    print("恭喜猜对了")
elif guess > number:
    print("猜大了")
elif guess < number:
    print("猜小了")