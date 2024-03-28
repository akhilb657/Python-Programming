import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

try:
    f = open("myfile","w")
    a,b = [int(x) for  x in input("Enter 2 numbers: ").split()]
    logging.info("Division in Progress")
    c = a/b

    f.write("Writing %d into file" %c)
    #f.close()

except ZeroDivisionError:
    print("Division not possible\nEnter non zero integer")
    logging.error("Division by zero")

else:
    print("Division is possible")

finally:
    f.close()
    print("file closed")

print("Code after exception")