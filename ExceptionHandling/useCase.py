class InvalidPasswordException(Exception):
    def __init__(self,msg):
        self.msg = msg
def password(pwd):
    if len(pwd) < 8:
        raise InvalidPasswordException("Password must have atleast 8 characters")

try:
    s = input("Create your password: ")
    password(s)
    print("Password created successfully")

except InvalidPasswordException:
    print("Password must have atleast 8 characters")