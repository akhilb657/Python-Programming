def decorFun(fun):
    def inner(n):
        res = fun(n)
        return res + " How are you?"
    return inner

@decorFun
def hello(name):
    return "Hello " + name

print(hello("Akhil"))

