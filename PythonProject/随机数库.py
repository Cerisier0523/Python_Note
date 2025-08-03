import random
random.seed(10)#初始化给定的随机数种子，默认为当前系统时间
random.random()#生成一个0.0到1.0之间的随机小数
random.uniform(1,2)#生成一个1到2之间的随机小数
random.randint(10,100)#生成一个10到100的整数
random.randrange(10,100,10)#生成一个10到100之间以10为步长的随机整数
s=random.getrandbits(2);print(s)#生成一个1比特(转化为二进制)长的随机整数
s=random.choice([1,2,3,4,5,6,7,8,9]) ;print(s) #从序列中随机选择一个元素
s=random.sample(range(1,10),2);print(s)#从序列中随机选择2个不重复的元素，用列表形式返回
s=[1,2,3,4,5,6,7,8,9];random.shuffle(s);print(s) #将序列中元素随机排序，返回打乱后的序列