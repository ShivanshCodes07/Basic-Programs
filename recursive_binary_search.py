def binary_search(L, K, begin, end):
    S = sorted(L)
    mid = (end + begin) // 2
    
    if begin == end:
        if S[begin] == K:
            return 1
        else:
            return 0
    
    if end - begin == 1:
        if S[begin] == K or S[end] == K:
            return 1
        else:
            return 0
    
    if S[mid] == K:
        return 1
    elif S[mid] < K:
        return binary_search(L, K, mid + 1, end)
    else:
        return binary_search(L, K, begin, mid - 1)

print(binary_search([34,45,56,76,89,100,234,25, 9, 0, 12] , 500 , 0, 10))
    