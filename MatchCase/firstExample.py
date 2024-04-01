x = 11

match x:
    case 1 | 4:
        print("1 or 4")
    case 2:
        print(2)
    case 3:
        print(3)
    case 9:
        print(9)
    case _:
        print("default")