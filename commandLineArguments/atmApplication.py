import sys

l = sys.argv

currentBalance = 10000

if(int(l[1]) == 1):
    print("Current available balance is : ", currentBalance)

elif(int(l[1]) == 2):
    n = int(input("How much you want to withdraw"))
    currentBalance = currentBalance - n
    print("You have withdrawn ",n ,"and current available balance is : ", currentBalance)

elif(int(l[1]) == 3):
    n = int(input("How much you want to deposit by cash"))
    currentBalance = currentBalance + n
    print("You have deposited ",n ,"and current available balance is : ", currentBalance)

elif(int(l[1]) == 4):
    n = int(input("How much you want to deposit by check"))
    currentBalance = currentBalance + n
    print("You have deposited ",n ,"and current available balance is : ", currentBalance)