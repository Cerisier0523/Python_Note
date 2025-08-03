#S.add(x) 如果x不在s中，将x添加到s中
#S.discard(x) 移除S中元素x，如果x不在集合S中，不报错
#S.remove(x) 移除S中元素x，如果x不在集合S中，产生KeyError异常
#S.clear(x) 移除S中所有元素
#S.pop(x) 随机返回S的一个元素，更新S，若S为空产生KeyError异常
#S.copy(x) 返回集合S的一个副本

B = set("pypy123")
print(B)
B.add("a")
print(B)
B.remove("p")
print(B)
B.discard("y")
print(B)
print(B.copy())
print(B.pop())
B.clear()
print(B)
