# Sort Submatrices
"""
The program must accept an integer matrix of size RxC as the input. The program must sort the 2x2 submatrices in the matrix based on the integer present in the top-left position.
If two or more submatrices have the same integer value in the top-left position, then the program must sort those submatrices in the order of their occurrence.Note:
The values of R and C are always even.
Boundary Condition(s):4 <= R, C <= 50
Input Format:The first line contains R and C separated by a space.The next R lines, each contains C integers separated by a space.
Output Format:The first R lines, each contains C integers separated by a space.
Example Input/Output 1:
Input:
4 4
64 39 75 90
55 35 50 98
95 37 30 49
80 56 13 65
Output:
30 49 64 39
13 65 55 35
75 90 95 37
50 98 80 56
Explanation:The four 2x2 submatrices in the given 4x4 matrix are given below.
64 39
55 35

75 90
50 98

95 37
80 56

30 49
13 65
After sorting the submatrices based on the integer present in the top-left position, the matrix becomes
30 49 64 39
13 65 55 35
75 90 95 37
50 98 80 56

Example Input/Output 2:
Input:
4 6
28 39 83 94 32 18
96 51 17 47 61 66
83 86 12 20 28 89
64 89 13 33 95 94
Output:
12 20 28 39 28 89
13 33 96 51 95 94
32 18 83 94 83 86
61 66 17 47 64 89
"""

# Solution

n,m=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(n)] 
l1=[] 
for i in range(0,n,2): 
    for j in range(0,m,2): 
        l1+=[[l[i][j],l[i][j+1],l[i+1][j],l[i+1][j+1]]] 
l1=sorted(l1,key=lambda x:x[0]) 
for i in range(0,n,2): 
    for j in range(0,m,2): 
        l[i][j]=l1[0][0] 
        l[i][j+1]=l1[0][1] 
        l[i+1][j]=l1[0][2] 
        l[i+1][j+1]=l1[0][3] 
        l1=l1[1:]
for i in l: 
    print(*i)
    
