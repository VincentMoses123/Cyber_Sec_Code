# Code by Vincent Moses II
import random
import string

def generate_password(length: int=10):
    #Picks 10 random letters, numbers, or punctuation
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length)) # repeats picking things intill lenght reaches 10
    return password

password = generate_password()
print("Generated Password: " + password)