def fun1(n):
    if n<=1:
        return n
    a,b=0,1
    for i in range(2,n+1):
        a,b=b,a+b
    return b

def fun2(n):
    if n<=1:
        return n
    return fun2(n-1)+fun2(n-2)

print(fun1(7),fun2(7))