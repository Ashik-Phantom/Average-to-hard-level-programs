#Rotate Matrix by X Degrees
"""
The program must accept an integer matrix of size NxN and an integer X as the input. 
The program must rotate the matrix by X degrees in the clockwise direction. 
Finally, the program must print the modified matrix as the output.
If it is not possible to rotate the matrix by X degrees, the program must print INVALID as the output. 
The matrix rotation is possible if the value of X is a multiple of 90 (i.e., 0, 90, 180, 270, 360, 450, 540, and so on).

Boundary Condition(s):2 <= N <= 1000 <= X <= 10^5

Input Format:
The first line contains N.The next N lines, each contains N integers separated by a space.
The (N+2)nd line contains X.
Output Format:
The first N lines, each contains N integers representing the rotated matrix.

Example Input/Output 1:
Input:
4
44 17 27 29
39 29 18 19
13 40 13 31
36 47 29 22
270

Output:
29 19 31 22
27 18 13 29
17 29 40 47
44 39 13 36

Explanation:
After rotating the matrix by 270 degrees, the matrix becomes.
29 19 31 22
27 18 13 29
17 29 40 47
44 39 13 36

Example Input/Output 2:
Input:
35 11 98 52 8
44 48 77 85 80
67 77 25 44 10
97 17 38 55 95
32 70 78 85 69
45

Output:
INVALID
"""

#Solution 

n=int(input()) 
l=[list(map(int,input().split())) for i in range(n)] 
x=int(input())%360 
k=[0,90,180,270]
if x not in k: 
    print('INVALID')
else: 
    if x==90: l=[i[::-1] for i in zip(*l)] 
    elif x==180: l=[i[::-1] for i in l][::-1] 
    elif x==270: l=[i for i in zip(*l)][::-1] 
    for i in l: print(*i)
