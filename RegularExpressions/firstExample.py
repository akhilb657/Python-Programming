import re

s = "Take 1 One 10-5-2024 23 idea. Only One idea 45 at a Time 30-9-2024"

res = re.search(r'o\w\w',s)
print(res)

res = re.findall(r'o\w\w',s)
print(res)

res = re.match(r'T\w\w',s)
print(res.group())

res = re.sub(r'One','Two',s)
print(res)

res = re.split(r'\d+',s)
print(res)

res = re.findall(r'O\w{1,2}',s)
print(res)

res = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',s)
print(res)

res = re.search(r'^T\w*',s)
print(res.group())