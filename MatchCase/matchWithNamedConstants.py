class ATM:
    withdraw = 1
    deposit = 2
    balance_check = 3

option = 4

match option:
    case ATM.withdraw:
        print("Withdraw")
    case ATM.deposit:
        print("Deposit")
    case ATM.balance_check:
        print("Balance check")
    case _:
        print("Invalid input")