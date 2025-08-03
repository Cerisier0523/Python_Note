def fact (n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

n=10
print(fact(n))

s=1
for i in range(1,n+1):
    s=s*i
print(s)