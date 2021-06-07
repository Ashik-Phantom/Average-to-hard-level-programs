"""
Enclose Character Matrix
The program must accept a character matrix of size R*C and an integer K as the input. The values of R and C are always divisible by K. The program must enclose the given character matrix within sub matrices of size K*K.
- The sub matrices in the border must be filled with 1s and 0s alternatively in clockwise direction. The first sub matrix in the top left will be filled with 1s.


Boundary Condition(s):
2 <= R, C <= 50
2 <= K <= Minimum value between R and C

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The (R+2)nd line contains K.

Output Format:
The first (2*K)+R lines, each contains (2*K)+C characters separated by a space.

Example Input/Output 1:
Input:
9 6
h R W G v P
z n N L A Q
Y u q z j r
z O k w y V
D z D g x i
u e S R s t
I e p A M e
m c u a h I
q V X Z p W
3

Output:
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0
0 0 0 h R W G v P 1 1 1
0 0 0 z n N L A Q 1 1 1
0 0 0 Y u q z j r 1 1 1
1 1 1 z O k w y V 0 0 0
1 1 1 D z D g x i 0 0 0
1 1 1 u e S R s t 0 0 0
0 0 0 I e p A M e 1 1 1
0 0 0 m c u a h I 1 1 1
0 0 0 q V X Z p W 1 1 1
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0

Explanation:
Here R = 9, C = 6 and K = 3.
The given 9*6 character matrix is enclosed within square matrices of size 3*3.
The square matrices in the border are filled with 1s and 0s alternatively in clockwise direction.

Example Input/Output 2:
Input:
6 6
h R W G v P
z n N L A Q
Y u q z j r
z O k w y V
D z D g x i
u e S R s t
2

Output:
1 1 0 0 1 1 0 0 1 1
1 1 0 0 1 1 0 0 1 1
0 0 h R W G v P 0 0
0 0 z n N L A Q 0 0
1 1 Y u q z j r 1 1
1 1 z O k w y V 1 1
0 0 D z D g x i 0 0
0 0 u e S R s t 0 0
1 1 0 0 1 1 0 0 1 1
1 1 0 0 1 1 0 0 1 1

Example Input/Output 3:
Input:
4 6
a Y y F d s
s o c A c n
O V n v i L
p G s v C T
2

Output:
1 1 0 0 1 1 0 0 1 1
1 1 0 0 1 1 0 0 1 1
0 0 a Y y F d s 0 0
0 0 s o c A c n 0 0
1 1 O V n v i L 1 1
1 1 p G s v C T 1 1
0 0 1 1 0 0 1 1 0 0
0 0 1 1 0 0 1 1 0 0

Example Input/Output 4:
Input:
4 8
a Y y F d s m p
s o c A c n d f
O V n v i L o e
p G s v C T r j
2

Output:
1 1 0 0 1 1 0 0 1 1 0 0
1 1 0 0 1 1 0 0 1 1 0 0
0 0 a Y y F d s m p 1 1
0 0 s o c A c n d f 1 1
1 1 O V n v i L o e 0 0
1 1 p G s v C T r j 0 0
0 0 1 1 0 0 1 1 0 0 1 1
0 0 1 1 0 0 1 1 0 0 1 1
"""



#Solution 1 

r,c=map(int,input().split())
m=[input().split() for x in range(r)]
k=int(input())
for x in range(r+(2*k)):
    for y in range(c+(2*k)):
        if (x//k+y//k)%2:
            ch=0
        else: ch=1
        if x<k or y<k or x>=(r+k) or y>=(c+k):
            print(ch,end=" ")
        else:
            print(m[x-k][y-k],end=" ")
    print()
    
    
    
#Solution 2

p,q=map(int,input().split());soni=[list(map(str,input().split())) for _ in 'p'*p];l=int(input());fuh=[];first=[];last=[];a=0
for x in range((q//l)+2):
    if x%2==0:first+=[1]*l;last+=[0]*l 
    else:first+=[0]*l;last+=[1]*l
for x in range((p//l)+2):
    for _ in range(l):fuh+=[first[:]] if x%2==0 else [last[:]]
for x in range(l,l+p):
    b=0
    for y in range(l,l+q):fuh[x][y]=soni[a][b];b+=1 
    a+=1 
for x in fuh:print(*x)
#print("fuhrer")


#Solution 3

r,c=map(int,input().split())
l=[input().split() for i in range(r)]
k=int(input())
x,y=(2*k)+r,(2*k)+c
m=1
s=[[] for i in range(x)]
for i in range((r//k)+2):
    p=[]
    for j in range(2+(c//k)):
        o=(1+i+j)%2
        for t in range(k):
            for q in range(k):
                s[(i*k)+t].append(o)
for i in range(r): 
    for j in range(c):
        s[i+k][j+k]=l[i][j]
for i in s:
    print(*i)
    
    
# Solution 4 

r,c=map(int,input().split())
m=[input().strip().split() for x in range(r)]
k=int(input())
mat=[]
totRows = (r+2*k)//k
for x in range(totRows):
    if x%2==0:
        row=(("1"*k+"0"*k)*100)[:c+2*k] 
    else:
        row=(("0"*k+"1"*k)*100)[:c+2*k] 
    for y in range(k):
        mat.append(list(row))
for x in range(k,k+r):
    for y in range(k,k+c):
        mat[x][y]=m[x-k][y-k]
for g in mat:
    print(*g)
    
    
