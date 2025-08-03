a="AbC dEf Gh"
#实例调用
#1.str.lower 返回字符串的副本，全部字符小写
b=a.lower()
print(b)

#2.str.upper 返回字符串的副本，全部字符大写
b=a.upper()
print(b)

#3.str.title 返回字符串的副本，全部单词首字母大写，其余小写
b=a.title()
print(b)

#4.str.capitalize 返回字符串的副本，全部字符首字母大写，其余小写
b=a.capitalize()
print(b)

#5.str.strip 返回字符串的副本，去掉首尾字符
b=a.strip()
print(b)

#6.str.lstrip(chars) 返回字符串的副本，去掉首字符
b=a.lstrip()
print(b)

#7.str.rstrip(chars) 返回字符串的副本，去掉尾字符
b=a.rstrip()
print(b)

#8.str.split(sep=None) 返回一个列表，由str根据sep被分割的部分组成列表
b=a.split(",")
print(b)

#9.str.count(sub)返回子串sub在str中出现的次数
b=a.count("a")
print(b)

#10.str.replace(old,new) 返回字符串的副本，所有old子串被替换为new
b=a.replace("AbC","abcd")
print(b)

#11.str.join(iter) 在iter变量除了最后元素外每个元素后增加一个str
b=a.join("123456")
print(b)

#12.str.center(width,[,fillchar])字符串str根据宽度width居中，fillchar可选
b=a.center(20,"=")
print(b)
