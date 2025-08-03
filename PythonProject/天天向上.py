import math

# a=math.pow(1+0.01,365)
# b=math.pow(1-0.01,365)
# print("进步一点点{0} 退步一点点{1}".format(a,b))

a=1;b=1;
for i in range(365):
    a*=1.01
    b*=0.99
print("进步一点点{0} 退步一点点{1}".format(a,b))