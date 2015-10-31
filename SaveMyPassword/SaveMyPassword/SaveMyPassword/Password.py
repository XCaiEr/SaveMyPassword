import getpass, msvcrt, sys

pwdChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','X',
            '0','1','2','3','4','5','6','7','8','9',
            '`','~','!','@','#','$','%','^','&','*','(',')','-','=','_','+',
            '[',']','{','}','\\','|',';',':','\'','\"',',','.','?','<','>','/','?']

def GetPasswordHidden(pwd = 'password:'):
    return getpass.getpass(pwd)

def GetPassword(pwd = 'password:'):
    sys.stdout.write(pwd)
    chars = []
    while True:
        char = msvcrt.getch()
        if char in '\r\n':
            print ''
            break
        elif char == '\b':
            if chars:
                del chars[-1]
                sys.stdout.write('\b \b')
        elif char == '\x1b':
            print ''
            return None
        elif char in pwdChars:
            chars.append(char)      
            sys.stdout.write('*')
    return ''.join(chars)

def Compare(pwd1, pwd2):
    if pwd1 == pwd2:
        return True
    else:
        return False

def CreatePassword(password = 'password:', confirm = 'confirms:', 
                   match = 'Password is created.', failed = 'Password is not created.'):
    pwd1 = GetPassword(password)
    if pwd1:
        pwd2 = GetPassword(confirm)
        if pwd2:
            if Compare(pwd1, pwd2):
                print match
                return pwd1
            else:
                print failed
                return CreatePassword()
    return None