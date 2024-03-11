s = {1,2,10,33,"asd",10,2,1}
print(s)


s.update([99,77])
print(type(s))
print(s)

#print(s * 3)

s.remove(2)
print(s)

f = frozenset(s)
#f.remove(10)

