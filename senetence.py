def upper(s):
    upper = 0
    for i in s:
        if i.isupper():
            upper +=1
    return upper

def lower(s):
    lower = 0
    for i in s:
        if i.islower():
            lower +=1
    return lower

def char(s):
    char = 0
    for i in s :
        char += 1
    return char

def word(s):
    word = 1
    for i in s:
        if i == " ":
            word += 1
    return word

sentence = input("enter your sentence :")
print(" no . of upper case letter :" , upper(sentence))
print("no. of lower case letter : " , lower(sentence))
print(" no. of character :" , char(sentence))
print("no. of words :" , word(sentence))
