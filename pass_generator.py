import random
import string
password_length = int(input("enter the length of password : "))
password = ""
for i in range(password_length):
    password += random.choice(string.ascii_letters + string.digits + string.punctuation)
print("your generated password is :" , password)