A = {"python",123,("python,123")}#使用{}建立集合
B = set("pypy123")#使用set()建立集合，把()中内容转换成集合
C = {"python",123,"python",123}
D = {}#没有内容的{}生成的是字典类型

print(A)
print(B)
print(C)
print(D,type(D))