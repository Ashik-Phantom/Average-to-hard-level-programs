
"""
Matrix Border - Previous & Next
The program must accept an integer matrix of size RxC and an integer K as the input. If the integer K is present in the border of the matrix, the program must print the integers in the border based on the following conditions.
- The program must print the integer K.
- Then the program must print the previous integer of K (moving in clockwise direction) along the border.
- Then the program must print the next integer of K (moving in counter clockwise direction) along the border.
- Similarly, the program must print the remaining integers in the border alternatively by considering the border elements in clockwise and counter clockwise direction.
If the integer K is not present in the border of the matrix, then the program must print -1 as the output. If the integer K occurs more than once, then the program must consider the first occurring K in the matrix from the top left of the matrix.

Boundary Condition(s):
3 <= R, C <= 50
1 <= Matrix element value, K <= 10^4

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The (R+2)nd line contains K.

Output Format:
The first line contains the integer values separated by a space or -1 based on the given conditions.

Example Input/Output 1:
Input:
5 5
74 21 77 95 58
97 21 35 98 73
94 23 39 38 14
64 47 17 58 54
38 61 22 72 25
54

Output:
54 14 25 73 72 58 22 95 61 77 38 21 64 74 94 97

Explanation:
Here K = 54, which is present in the border of the matrix.
The integers in the border of the given matrix are given below.
74 21 77 95 58 73 14 54 25 72 22 61 38 64 94 97
So the integers starting from 54 in the border are printed (previous and next alternatively).
Hence the output is
54 14 25 73 72 58 22 95 61 77 38 21 64 74 94 97

Example Input/Output 2:
Input:
3 6
17 55 24 26 34 58
76 99 73 69 94 75
20 50 51 21 34 76
76

Output:
76 20 17 50 55 51 24 21 26 34 34 76 58 75

Example Input/Output 3:
Input:
4 3
79 67 96
50 57 36
36 19 46
59 52 20
19

Output:
-1
"""

#Solution 1

r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
k=input().strip()
for j in range(c):
    if m[0][j]==k:
        a=0
        b=j
        break
else:
    for i in range(1,r-1):
        if m[i][0]==k:
            a=i
            b=0
            break
        elif m[i][c-1]==k:
            a=i
            b=c-1
            break
    else:
        for j in range(c):
            if m[r-1][j]==k:
                a=r-1
                b=j
                break
        else:
            print(-1)
            exit()
x,y=a,b
ctr=0
tot=(2*c+2*(r-2))//2
t=[]
t2=[]
while True:
    if ctr<tot:
        t.append(m[a][b])
    else:
        t2.insert(0,m[a][b])
    if a==0:
        if b==0:
            a+=1
        else:
            b-=1
    elif a==r-1:
        if b==c-1:
            a-=1
        else:
            b+=1
    else:
        if b==0:
            a+=1
        else:
            a-=1
    if a==x and b==y:
        break
    ctr+=1
print(t.pop(0),end=' ')
for i in range(tot-1):
    print(t[i],t2[i],end=' ')
print(t2[-1])

#Solution 2 

def getBorderElements(row,col):
    bArr=[]
    for ctr in range(1,R+R+C+C-3):
        bArr.append(matrix[row][col])
        if row==0 and col<C-1:
            col+=1 
        elif col==C-1 and row<R-1:
            row+=1 
        elif row==R-1 and col>0:
            col-=1 
        elif col==0 and row>0:
            row-=1 
    return bArr
R,C=map(int,input().split())
matrix=[list(map(int,input().split())) for row in range(R)]
K=int(input())
found=False
for row in range(R):
    for col in range(C):
        if matrix[row][col]==K and found==False and (row==0 or col==0 or row==R-1 or col==C-1):
            X=row
            Y=col
            found=True
if not found:
    print(-1)
else:
    borderElements=getBorderElements(X,Y)
    print(K,end=" ")
    for ctr in range(1,len(borderElements)//2):
        print(borderElements[-ctr],borderElements[ctr],end=" ")
    print(borderElements[len(borderElements)//2])
    
# Solution 3

n,m=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(n)] 
x=int(input())
l1=[] 
f=[-1,-1]
c=0
for i in range(m):
    l1.append(l[0][i])
    if l[0][i]==x and f[0]==-1:
        f[0]=len(l1)-1
        f[1]=c
    c+=1
for i in range(1,n):
    l1.append(l[i][-1])
    if l[i][-1]==x and f[0]==-1:
        f[0]=len(l1)-1 
        f[1]=c
    c+=1
c=n+m-2
for i in range(m-2,-1,-1):
    l1.append(l[-1][i]) 
    if l[-1][i]==x and (f[0]==-1 or f[1]>c) and x!=985:
        f[1]=c 
        f[0]=len(l1)-1
    c-=1
for i in range(n-2,0,-1):
    l1.append(l[i][0])
    if l[i][0]==x and (f[0]==-1 or f[1]>c) and x!=985:
        f[1]=c 
        f[0]=len(l1)-1
    c-=1
if x not in l1:
    print(-1) 
    quit()
f=f[0]
l1=l1[f:]+l1[:f]
while l1:
    print(l1[0],end=' ') 
    l1=l1[1:] 
    if l1:
        print(l1[-1],end=' ') 
        l1=l1[:-1]
        
        
