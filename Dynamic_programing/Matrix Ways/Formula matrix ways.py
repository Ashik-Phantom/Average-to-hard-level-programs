"""
 DP (using formula) - Matrix Ways from Top Left to Bottom Right
The number of rows R and columns C of a matrix are passed as the input. The program must print the number of ways W to traverse from the top left cell of the matrix to the bottom right cell of the matrix. From any given cell, the movement can be either to the right cell or the bottom cell.
Boundary Condition(s):
2 <= R, C <= 100
Input Format:
The first line contains R and C separated by a space.
Output Format:
The first line contains the number of ways W.
Example Input/Output 1:
Input:
2 2
Output:
2
Example Input/Output 2:
Input:
3 4
Output:
10
Example Input/Output 3:
Input:
20 15
Output:
818809200
"""
def fact(n):
    res=1 
    for i in range(2,n+1):
        res*=i
    return res 
def out(a,b):
    a,b=a-1,b-1
    return fact(a+b)//(fact(a)*fact(b)) 
m,n=map(int,input().split())
print(out(m,n))
