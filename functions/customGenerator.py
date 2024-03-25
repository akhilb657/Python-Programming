def customGen(x,y):
    while x<y:
        yield x
        x += 1
res = customGen(1,10)
for i in res:
    print(i)