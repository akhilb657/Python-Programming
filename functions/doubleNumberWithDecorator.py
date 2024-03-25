def decorFun(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decorFun
def num():
    return 99
#res = decorFun(num)
#print(res())
print(num())