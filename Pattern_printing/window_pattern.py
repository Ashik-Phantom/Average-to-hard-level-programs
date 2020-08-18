#Window Pattern

"""
The program must accept two integers N and X as the input. 
The program must print an S*S matrix of matrices (where S is the square root of X) based on the following conditions.
  - The size of each matrix in the S*S matrix is N*N.- Each matrix contains only asterisks.
  - The matrices are separated by the pipe symbols (|) vertically(including edges).
  - The matrices are separated by the hyphens (-) horizontally(including edges).
  - Each intersection of the matrices(including corners) is represented by the plus symbol (+).
Note: The value of X is always a perfect square.

Boundary Condition(s):
1 <= N <= 50
1 <= X <= 100

Input Format:
The first line contains N and X separated by a space.
Output Format:The first (N*S)+(S+1) lines containing the S*S matrix of matrices based on the given conditions.

Example Input/Output 1:

Input: 5 1
Output:
+-----+
|*****|
|*****|
|*****|
|*****|
|*****|
+-----+

Explanation:
Here N = 5 and X = 1.
The square root of 1 is 1.
So the size of the matrix is 1x1 and it contains a matrix of size 5*5 with asterisks.
Hence the output is
+-----+
|*****|
|*****|
|*****|
|*****|
|*****|
+-----+

Example Input/Output 2:
Input: 2 4
Output:
+--+--+
|**|**|
|**|**|
+--+--+
|**|**|
|**|**|
+--+--+

Example Input/Output 3:

Input: 1 16
Output:
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+

"""

#solution

#normal method

import math
n,X=map(int,input().split())
x=int(math.sqrt(X))
print('+',end='')
for i in range(x): 
    print('-'*n,'+',sep='',end='')
print()
for i in range(x):
    for j in range(n): 
        print('|',end="") 
        for ii in range(x): 
            print('*'*n,'|',sep='',end='') 
        print() 
    print('+',end='') 
    for iii in range(x): 
        print('-'*n,'+',sep='',end='') 
    print()
    
#-----------------------------------------------------------------------------------------------------------    

#using resursive functions

import math

def split(x,n):
    print('+',end='')
    for i in range(x): 
        print('-'*n,'+',sep='',end='')
    print()
def submat(x,n):
        print('|',end="") 
        for i in range(x): 
            print('*'*n,'|',sep='',end='') 
        print()
        
n,X=map(int,input().split())
x=int(math.sqrt(X))
split(x,n)
for i in range(x):
    for j in range(n): 
        submat(s,n)
    split(x,n)
