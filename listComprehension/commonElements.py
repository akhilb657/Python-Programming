a = [1,2,3,4,5]
b = [1,4,5,6,9]

z = []
"""
for i in a:
    if i in b:
        z.append(i)
"""
z = [i for i in a if i in b]

print(z)
