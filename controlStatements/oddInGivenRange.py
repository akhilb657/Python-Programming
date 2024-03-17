min = int(input("Enter minimum number: "))
max = int(input("Enter maximum number: "))

i = min

if i % 2 == 0:
    i += 1
while (i <= max):
    print(i)
    i += 2