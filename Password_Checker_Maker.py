import random
import string
import re
import Password_Strengh


print("Welcome to the password test")
print("In this test, the code checks the password you put in")
print("Then if it does not recive a password it liks, it gives you a new one that is better!")

import validate_password 
password=input(str("Enter your password: "))
is_valid=validate_password(password)

if is_valid:
    print("Valid and strong password")
else:
    print("Not a valid password!")