def matrix_multiplication(X, Y):

    # row and columns of matrix X

    r1, c1 = len(X), len(X[0])

   

    # row and columns of matrix Y

    r2, c2 = len(Y), len(Y[0])

   

    # initializing result matrix

    # the dimension of resultant matrix: r1 x c2

    result = []

    for i in range(r1):

        result.append([0]*c2)

   

    # matrix multiplication

    # iterate through rows of X

    for i in range(r1):

       # iterate through columns of Y

       for j in range(c2):

           # iterate through rows of Y

           for k in range(r2):

               result[i][j] += X[i][k] * Y[k][j]

   

    return result

l = [[1,2] , [4,5] , [7,8]]
m = [[9,7,6] , [2,3,4]]
print(matrix_multiplication(l,m))