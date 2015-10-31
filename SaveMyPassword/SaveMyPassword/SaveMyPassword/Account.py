from SaveMyPassword import *

def CreateAccount():
    account = {}
    account['name'] = raw_input('Enter the account name:')
    account['acct'] = raw_input('Enter the account:')
    account['pwd'] = Password.CreatePassword()    
    return acount