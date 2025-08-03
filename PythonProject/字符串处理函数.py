import string
from collections import namedtuple

#求字符串长度
print("{0}".format(len("一二三四五六")),end="\n")

#将数字转化为字符串
print(str(123),end="\n")
#将容器(列表字典)转化为字符串
print("str([1,2,3])",end="\n")

#此处单双引号交替使用，不然会报错
print('str({"name":"alice"})',end="\n")
#其他解决方式
#转义内部双引号
print("str({\"name\":\"alice\"})",end="\n")

#整数x的十六位进制或八进制小写形式字符串
print("hex(425)",end="\n")
print("oct(425)",end="\n")

#unicode编码转化字符(输出特定符号如箭头)
print(chr(425),end="\n")
#单字符转化为unicode编码
print(ord(25),end="\n")

