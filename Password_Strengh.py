import re

#Checks for certain conditions to check if you have a strong password or not!

def validate_password(password):
    #Checks for length of password
    if len(password) < 8:
        return False
    
    #Check for capital letter
    if not re.search(r'[A-Z]', password):
        return False
    
    #Check for lower case letter
    if not re.search(r'[a-z]', password):
        return False
    
    #check for number
    if not re.search(r'\d', password):
        return False
    
    #Check for symbols
    if not re.search(r'[,.<>/;:"{}=-_!@#$%^&]', password):
        return False
    
    return True



password=input(str("Enter your password: "))
is_valid=validate_password(password)

if is_valid:
    print("Valid and strong password")
else:
    print("Not a valid password!")
    