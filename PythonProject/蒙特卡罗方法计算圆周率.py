import  random
darts = 1000*1000
hits = 0.0
for i in range(1,darts+1):
    x, y = random.random(), random.random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0 :
        hits += 1.0
    pi =4 * (hits/darts)
    print("圆周率的值是：{0}".format(pi))

