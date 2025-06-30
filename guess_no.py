import random
target = random.randint(1,100)
while True:
    user_choice = int(input("enter your guess number :"))
    if(user_choice == target):
        print("success : your guess is correct")
        break
    elif(user_choice < target):
        print("your guess is less than target , choose higher number")
    else:
        print("your guess is greater than target , choose lower number")
       
print("______GAME OVER______")