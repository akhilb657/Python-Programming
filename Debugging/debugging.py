import myModule

def fun1(n):
    print("fun1",n)
    myModule.fun2(n)

n = int(input("Enter a number: "))
fun1(n)