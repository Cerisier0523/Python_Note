import math

r=eval(input('请输入半径：'))
s=math.pi*r*r
c=2*math.pi*r
print('面积是:\n',s)
print('周长是:\n',c)
print("面积:{},周长:{}".format(s,c))
print(f"面积:{s},周长:{c}")
print(f"面积:{s:.2f},周长:{c:.2f}")
print("面积:{:.2f},周长:{:.2f}".format(s,c))

