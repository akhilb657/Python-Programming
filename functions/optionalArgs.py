def myFun(x, *args, **kwargs):
    print(x)
    #print(args)
    kwargs["company"] = "Magna"
    for each_arg in args:
        print(each_arg)
    #print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
    modified_args = args + (14,15,16)
    myFun2(modified_args,**kwargs)

def myFun2(*args, **kwargs):
    print(args)
    print(kwargs)

myFun(9, 11,12,13,name="Akhil",salary=2500)