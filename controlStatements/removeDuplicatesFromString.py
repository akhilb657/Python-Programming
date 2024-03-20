s = 'abbcaaaaqqqwwwee'
l = []
for i in s:
    if i not in l:
        l.append(i)
print(l)
print("".join(l))