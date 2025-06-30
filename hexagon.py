n = int(input("enter the number"))
#
for i in range(n):

  for j in range(n-1 -i):
    print(" ",end="")
  
  for k in range (n + i * 2):
    print("@",end="")
  print()
for i in range(n-1):

  for j in range(i+1):
    print(" ",end="")
  
  for k in range((n) +(n-2-i)*2):
    print("@",end="")
  print()