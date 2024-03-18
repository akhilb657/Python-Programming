n = int(input("Enter a number: "))

primeFlag = True

i = 2
while (i < n):
    if (n % i == 0):
        primeFlag = False
    i += 1

if (primeFlag and n > 1):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")