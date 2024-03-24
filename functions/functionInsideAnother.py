def display(name):
    def message():
        return "Hy"
    res = message() + " " + name
    return res

print(display("Akhil"))
#print(message())