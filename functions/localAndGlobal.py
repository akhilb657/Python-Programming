x = 10

def display():
    #print(x)
    #y = 2
    x = 99
    #print(y)
    print(x)
    print(globals()['x'])


print(x)
#print(y)
#display()

f = display
f()
f()