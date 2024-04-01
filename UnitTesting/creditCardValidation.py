from datetime import *

def validateCard(expDate):
    if (expDate > datetime.now().date()):
        return "Valid"
    else:
        #return "Expired"
        raise RuntimeError("card has expired")

#print(validateCard(date(2014,3,31)))