n = int(input("enter the number of minutes : "))
colored_grid = 1
for i in range(n):
    colored_grid = colored_grid + (i*4)
print("after ", n , "minutes there are " , colored_grid-1 , "colored celss on the boundry 1 in the center ")

