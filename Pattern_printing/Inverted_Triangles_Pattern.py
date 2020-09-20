# Inverted Triangles Pattern
"""
The program must accept an integer N as the input. The program must generate a matrix of size RxC with zeroes, 
where R represents the number of rows N+1 in the matrix and C represents the number of columns (N*2)+1 in the matrix. 
The program must replace the zeroes in the matrix based on the following conditions.- All the zeroes in the first row are replaced with asterisks.
- All the zeroes in the middle column are replaced with asterisks.
- All the zeroes in the diagonal from top-left to the bottom-middle are replaced with asterisks.
- All the zeroes in the diagonal from top-right to the bottom-middle are replaced with asterisks.
Finally, the program must print the modified matrix as the output.
Boundary Condition(s):3 <= N <= 100
Input Format:
The first line contains N.
Output Format:
The first R lines containing the modified matrix.

Example Input/Output 1:
Input:
4
Output:
*********
0*00*00*0
00*0*0*00
000***000
0000*0000

Example Input/Output 2:
Input:
5
Output:
***********
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
00000*00000
"""
###########################################################################
# Solution

#Logic 1 - nested loops  
# Code - Arsive

n = int(input())
r = n + 1
c = n * 2 + 1
d = 0
for i in range(r):
    for j in range(c):
        if i == 0 or j == c//2 or j == d or j == c - d - 1:
            print('*',end="")
        else:
            print(0,end="")
    print()
    d += 1
    
###########################################################################

# Logic 2 - Concatenation
# Code - Ashik-Phantom

  
n = int(input())
c = n*2+1 
z1, z2 = 1, n-2 
print('*' * c)
for i in range(n - 1): 
    print('0' * z1, '*', '0' * z2, '*','0' * z2, '*', '0' * z1, sep="") 
    z1 += 1 
    z2 -= 1
print('0' * z1, '*', '0' * z1, sep="")
