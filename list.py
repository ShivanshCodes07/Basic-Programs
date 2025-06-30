def star(a):
    no = a
    while no!=0 :
        for i in range(no):
            print("*",end=" ")
        no=no-1
        print()

print(star(5))