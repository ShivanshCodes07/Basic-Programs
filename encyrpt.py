import string


def encrypt(s, shift):

    lower_case = list(string.ascii_lowercase)

    upper_case = list(string.ascii_uppercase)


    encrypt_msg = ''

    for char in s:

        if char in lower_case:

            encrypt_msg += lower_case[(lower_case.index(char) + shift) % 26]

        elif char in upper_case:

            encrypt_msg += upper_case[(upper_case.index(char) + shift) % 26]

        else:

            encrypt_msg += char 

   

    return encrypt_msg

print(encrypt("s vyfo iye" , 10))