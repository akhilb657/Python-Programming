l = [1,2,3,4,5,6,7,8]

res = list(filter(lambda n : n%2 == 0,l))
print(res)
for i in res:
    print(i)