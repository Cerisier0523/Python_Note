x="hello"
y="world"
#连接字符串
print("{0}".format(x+y))
#复制n次字符串
print("{0}".format(x*2),end="\n")
#判断前者是否为后者的子串
print("{0}".format(x in y),end="\n")
#索引符号
print("{0}".format(x[1:2]),end="\n")#左闭右开，不包含后者

