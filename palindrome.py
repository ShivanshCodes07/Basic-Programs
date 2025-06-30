import numpy
a = [ [1,2,3],[4,5,6],[7,8,9]]
b = [ [4,5,6],[7,8,9],[2,3,4]]
M = numpy.matrix(a)
N = numpy.matrix(b)
print(M)
print(N)
print(M*N)
