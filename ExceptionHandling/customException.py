class OverTheLimitException(Exception):
    def __init__(self,msg):
        self.msg = msg


def withdrawl(amount):
    if(amount > 500):
        raise OverTheLimitException("You cannot withdraw 500$ per day")

withdrawl(600)