def comp(p,r,t):
    if t == 1:
        return p*(1+(r/100))
    else:
        return comp(p,r,t-1)*(1+(r/100))
    
print(comp(2000,10,3))
    