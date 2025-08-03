#del d[k] 删除字典d中键k对应的项
#k in d 判断k是否在字典d中，有返回True
#d.keys() 返回字典d中所有键的信息
#d.values() 返回字典d中所有值的信息
#d.items() 返回字典d中所有键值对的信息
#d.get(k.<default>) 键k存在，则返回相应值，不存在则返回<default>
#d.pop(k.<default>) 键k存在，则取出相应值，不存在则返回<default>
#d.popitem() 随机从字典d中取出一个键值对，以元组的形式返回
#d.clear() 删除所有键值对
#len(d) 返回字典d中元素的个数

d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
print("中国" in d)
print("北京" in d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get("中国","伊斯兰堡"))
print(d.get("巴基斯坦","伊斯兰堡"))
print(d.get("中国","上海"))

print(d)
del d["美国"]
print(d)
d.pop("法国","键不存在")
print(d)
d.pop("俄罗斯","键不存在")
print(d)
d.clear()
print(d)