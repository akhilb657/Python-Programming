l = ["Python","Django","Docker","DRF"]

match l:
    case ["Python","Django"]:
        print("Python and Django")
    case ["Django","Docker"]:
        print("Django and Docker")
    case ["Docker","DRF"]:
        print("Docker and DRF")
    case ["Python","Django","Docker","DRF"]:
        print("All courses")
    case _:
        print("None")