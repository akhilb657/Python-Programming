lst = [1,2,"Akhil",-8,31.5]
print(lst)

print(lst[3])

print(lst[3:5])

print(lst*2)

print(len(lst))

lst.append(45)
lst.remove('Akhil')
del(lst[1])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(3,99)
print(lst)

lst.sort(reverse=True)
print(lst)