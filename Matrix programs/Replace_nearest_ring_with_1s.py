# Replace nearest ring with 1s

"""
The program must accept a matrix of size RxC containing 0s, 1s and exactly one X as the input. 
The program must find the full ring near to X with at least one 0. 
Then the program must modify the matrix by replacing all 0s in the full ring with 1s. Finally, the program must print the modified matrix as the output. 
If there is no such full ring near to X, the program must print the given matrix as it is.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.The next R lines, each contains C elements separated by a space.
Output Format:
The first R lines, each contains C elements separated by a space.

Example Input/Output 1:
Input:
5 60 
1 1 1 0 1
1 1 0 1 1 0
0 1 1 X 0 1
0 0 1 0 0 1
0 0 0 1 1 0

Output:
0 1 1 1 0 1
1 1 1 1 1 0
0 1 1 X 1 1
0 0 1 1 1 1
0 0 0 1 1 0

Explanation:The full ring near to X with at least one 0 is highlighted below.
0 1 1 1 0 1
1 1 0 1 1 0
0 1 1 X 0 1
0 0 1 0 0 1
0 0 0 1 1 0
After replacing 0s in the full ring with 1s, the matrix becomes
0 1 1 1 0 1
1 1 1 1 1 0
0 1 1 X 1 1
0 0 1 1 1 1
0 0 0 1 1 0

Example Input/Output 2:
Input:
8 7
1 0 0 1 0 0 0
0 1 1 0 1 1 0
1 1 1 1 1 1 1
1 1 X 1 0 1 0
1 1 1 1 1 1 0
0 1 1 0 1 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0
Output:
1 0 0 1 0 0 0
1 1 1 1 1 1 0
1 1 1 1 1 1 1
1 1 X 1 1 1 0
1 1 1 1 1 1 0
1 1 1 1 1 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0

Explanation:
The full ring near to X with at least one 0 is highlighted below.
1 0 0 1 0 0 0
0 1 1 0 1 1 0
1 1 1 1 1 1 1
1 1 X 1 0 1 0
1 1 1 1 1 1 0
0 1 1 0 1 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0
After replacing 0s in the full ring with 1s, the matrix becomes
1 0 0 1 0 0 0
1 1 1 1 1 1 0
1 1 1 1 1 1 1
1 1 X 1 1 1 0
1 1 1 1 1 1 0
1 1 1 1 1 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0

Example Input/Output 3:
Input:3 4
1 0 1 0
X 0 1 0
0 0 0 0
Output:
1 0 1 0
X 0 1 0
0 0 0 0
"""
# Solution 

def finish(): 
    for i in l: 
        print(*i) 
        exit()
        
r,c = map(int,input().split())
l = []
for i in range(r): 
    k = list(map(str,input().split())) 
    if 'X' in k: 
        posi = i 
        posj = k.index('X') 
    l.append(k)
f = 0 
postempi = posi
postempj = posj 
sizei = posi+2 
sizej = posj+2
res=[]
while(f == 0): 
    if posi <= 0 or posj <= 0 or sizei > r or sizej > c:
        finish() 
    for i in range(posi-1, sizei): 
        for j in range(posj-1, sizej): 
            res.append(l[i][j]) 
    if '0' not in res: 
        res = [] 
        posi -= 1 
        posj -= 1 
        sizei += 1 
        sizej += 1 
    else: 
        for i in range(posi-1, sizei): 
            for j in range(posj-1, sizej): 
                if i == postempi and j == postempj: 
                    l[i][j] = 'X' 
                else: 
                    l[i][j] = '1' 
        finish()
