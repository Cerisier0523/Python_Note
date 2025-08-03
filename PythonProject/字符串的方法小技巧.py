
#小技巧：replace()方法是替换，若要把字符串中间的某个子串删掉，
# 可以用.replace()把某个子串用''替换
a="唯品会——360公司"
print(a.replace("——360公司"," "))

#.join()方法的特殊性，也可以用于连接列表中的元素
my_list=['apple','banana','mango']
print(':'.join(my_list))
