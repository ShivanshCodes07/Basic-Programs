def binary_search(L, k):
    s = sorted(L)
    
    begin = 0
    end = len(s)-1
    while(begin<=end):
        mid = (begin+end)//2
        if k == s[mid]:
            return 1
        elif k<s[mid]:
            end = mid-1
        elif k > s[mid]:
            begin = mid+1
        elif(end - begin == 1):
            if k == s[begin] or k == s[end]:
                return 1
    return 0
            
print(binary_search([13,10,45,34,67,90,78,9,0,35,] ,-1))