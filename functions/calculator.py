def cal(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div

ans = cal(5,4)
print(ans)

for i in ans:
    print(i)