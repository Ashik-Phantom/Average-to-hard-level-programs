# Footpath - Four Directions
"""
The program must accept four integers N, W, S and E representing the number of steps in the directions North, West, South and East respectively. 
A person is standing in a position, and he moves N steps towards the north, then he moves W steps towards the west, 
then he moves S steps towards the south and E steps towards the east. The program must print the output based on the following conditions.
- Initially, the person moves N steps towards the north, so the program prints "N" N times towards the north.
- Then the person moves W steps towards the west, so the program prints "W" W times towards the west.
- Then the person moves S steps towards the south, so the program prints "S" S times towards the south.
- Then the person moves E steps towards the east, so the program prints "E" E times towards the east.
The person stops moving when he crosses his path or there are no moves in the east. 
The program must print the hyphens instead of empty places to make the person's footpath more clear.
Boundary Condition(s):1 <= N, W, S, E <= 100Input Format:The first line contains N, W, S and E separated by a space.Output Format:The lines containing the characters as per the given conditions.

Example Input/Output 1:
Input:
5 7 6 5
Output:
WWWWWWWN
S------N
S------N
S------N
S------N
S-------
SEEEEE--

Explanation:
Here N = 5, W = 7, S = 6 and E = 5.
Initially, the person moves 5 steps towards the north (N).
Then the person moves 7 steps towards the west (W).
Then the person moves 6 steps towards the south (S).
Then the person moves 5 steps towards the east (E).
Then the empty places are filled with hyphens.
Hence the output

Example Input/Output 2:
Input:
4 3 3 3
Output:
WWWN
S--N
S--N
SEEE

Example Input/Output 3:
Input:
6 6 6 10
Output:
WWWWWWN----
S-----N----
S-----N----
S-----N----
S-----N----
S-----N----
SEEEEEEEEEE
Example Input/Output 4:
Input:10 5 4 8
Output:
WWWWWN
S----N
S----N
S----N
SEEEEE
-----N
-----N
-----N
-----N
-----N
"""

############################################## 
# logic 1 
# 100% correct
n,w,s,e=map(int,input().split()) 
if s>=n:
    x=max(w,e)
else:
    x=w
y=max(n,s) 
mat=[]
for i in range(y+1):
    temp=[]
    for j in range(x+1):
        temp.append("-")
    mat.append(temp)    
for i in range(0,w):
    mat[0][i]="W"
for i in range(0,n):
    mat[i][w]="N"
for i in range(1,s+1):
    mat[i][0]="S" 
for i in range(1,e+1):
    try:
        mat[s][i]="E"
    except:
        break     
for i in mat:
    if len(set(i))!=1:
        print(*i,sep="")
	
##############################################
# logic 2
# 100% correct

n,w,s,e=map(int,input().split()) 
r=max(n,s)
c=max(w,e)
if n>=e+1: 
	c=c-(e-w)
	e=w 
l=[['-' for j in range(c+1)] for i in range(r+1)]
for i in range(n): 
	l[i][w]='N'
for i in range(w): 
	l[0][i]='W'
for i in range(1,s+1): 
	l[i][0]='S' 
for i in range(1,e+1): 
	l[s][i]='E' 
for i in l: 
	if i.count('-')==c+1: 
		continue 
	else: 
		print(*i,sep="")

##############################################
# logic 3 
# 70% correct

n,w,s,e=map(int,input().split()) 
r=max(n,s)
c=max(w,e)
f=0
l=[['-' for j in range(c+1)] for i in range(r+1)]
for i in range(n): 
	l[i][w]='N'
for i in range(w): 
	l[0][i]='W'
for i in range(1,s+1): 
	l[i][0]='S' 
for i in range(1,e+1): 
	l[s][i]='E'
	if n>s:
		f=1
		if i==w:
			break  
for i in l: 
	g=''.join(ii for ii in i)
	if g.count('-')==c+1: 
		continue 
	else: 
		if f==1:
			print(g.rstrip('-'))
		else:
			print(g)

##############################################
# logic 4
# 50% correct
		
n,w,s,e=map(int,input().split()) 
row,col=max(s,n-1),max(w,e)
if s+1<n+1:
    col=w
l=[['-']*(1+col) for i in range(row+1)]
for i in range(n):
    l[i][w]='N' 
for i in range(w):
    l[0][i]='W' 
for i in range(1,s+1):
    l[i][0]='S' 
for i in range(1,e+1):
    if i<col+1:
        l[s][i]='E' 
[print(*i,sep="") for i in l]  


