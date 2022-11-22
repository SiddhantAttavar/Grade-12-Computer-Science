'''
Write a program that asks a new user about UserId and password and then appends it to file "Security.bin" provided the given userid does not exist in the file. If it does, then display error message "User id already exists" and prompts the user to re-enter the userid. Also, make sure that the pasword is atleast 8 characters long with atleast a digit and a special character out of "$@%" in it.
'''

import pickle

def checkPasswordSecurity(password):
    if len(password) < 8:
        return False
    s = '0124356789'
    for c in s:
        if c in password:
            break
    else:
        return False
    s = '$@%'
    for c in s:
        if c in password:
            return True
    return False

def newUser(userId, password):
    d = {}
    try: 
        file = open('Security.bin', 'rb')
        d = pickle.load(file)
        file.close()
    except:
        file = open('Security.bin', 'wb')
        file.close()
        try:
            file = open('Security.bin', 'rb')
            d = pickle.load(file)
            file.close()
        except:
            pass

    if userId in d:
        print('User id exists')
        return
    if not checkPasswordSecurity(password):
        print('Weak password')
        return

    d[userId] = password
    file = open('Security.bin', 'wb')
    pickle.dump(d, file)
    file.close()
    
userId = input('Enter user id: ')
password = input('Enter password: ')
newUser(userId, password)
