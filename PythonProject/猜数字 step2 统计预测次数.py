number = 9
count = 0
while count < 5:
    guess = eval(input("请输入数字:"))
    count += 1
    if guess == number:
        print("猜对了")
        break
    elif guess < number:
        print("猜小了")
    elif guess > number:
        print("猜大了")