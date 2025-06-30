def mini(L):
    mini = L[0]
    for i in range(1,len(L)):
        if L[i]<mini:
            mini = L[i]
    return mini

def sort(L):
    if len(L)==1 or len(L)==0:
        return L
    else:
        m = mini(L)
        L.remove(m)
        return [m]+sort(L)
    
print(sort([3,2,1,4,5,6,7,8,9,0]))