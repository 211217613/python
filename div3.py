import numpy as np
from math import sqrt
import time
import sys

print('\n',sys.version,'\n')

np.random.seed([1234])
# simple loops
n = 400
A = np.random.rand(n,n)
B = np.random.rand(n,n)
C = np.zeros_like(A)

t0 = time.time()
for i in range(n):
    for k in range(n):
        for j in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Matrix Multiply n= {0} with loops {1} sec".format(n,time.time() - t0) )

t0 = time.time()
norm = 0
for i in range(n):
    for j in range(n):
        norm += C[i][j] * C[i][j]
norm = sqrt(norm)
print("matrix norm n={0} with loops {1} sec".format(n, time.time() -t0))

s = list()
# for x in range(0,1001):
#     if x % 3 == 0 or x % 5 == 0:
#         s.append(x)

[s.append(x) for x in range(0,41000) if x %3 ==0 or x%5==0]
print(sum(s))
