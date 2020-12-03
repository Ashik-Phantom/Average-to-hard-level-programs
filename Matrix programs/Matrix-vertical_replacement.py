# Matrix - Vertical Replacement
"""
The program must accept a character matrix of size RxC and a string S as the input. 
The program must find the position P of the first occurrence of the first character of S in the given matrix. 
Then the program must replace L characters (where L is equal to the length of S) from the position P with the characters in S vertically (top to bottom) in the matrix. 
If it reaches the last column when traversing vertically, then the program must start replacing the characters from the first column for the remaining characters. 
Finally, the program must print the modified matrix as the output.Note: The first character of S is always present in the given matrix.
Boundary Condition(s):
2 <= R, C <= 501 <= Length of S <= R*C
Input Format:
The first line contains R and C separated by a space.The next R lines, each contains C characters separated by a space.
The (R+2)nd line contains S.Output Format:The first R lines, each contains C characters representing the modified matrix.
Example Input/Output 1:
Input:
6 5
S K q J l
P L M b F
F s F J D
i b P b r
s q A n Z
D a A O j
shopping
Output:
S K p J l
P L i b F
F s n J D
i h g b r
s o A n Z
D p A O j
Explanation:
Here S = shopping.The position of the first occurrence of the first character of S is (3, 2).
After replacing the characters from the position (3, 2) with the characters of S, the matrix becomes

Example Input/Output 2:
Input:
3 3
t S l
S e e
F N i
SkillRack
Output:
a S l
c k l
k i R

Example Input/Output 3:
Input:
4 5
a S r p k
Y I D k F
h O m x w
j i Q h p 
window
Output:
n S r p k
d I D k F
o O m x w 
w i Q h i
"""


# Solution 
r, c = map(int,input().split())
l = [list(map(str,input().split())) for i in range(r)]
s = input().strip()
f=0
for i in range(r):
    for j in range(c):
        if l[i][j]==s[0]:
            x,y,f=i,j,1
            break
    if f==1:
        break 
for i in s:
    l[x][y]=i
    x+=1 
    if x==r:
        x=0 
        y+=1
    if y==c:
        y=0 
for i in l:
    print(*i)
         
      
