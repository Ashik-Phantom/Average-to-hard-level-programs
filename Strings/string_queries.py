#String -Queries
"""
Example Input/Output:
Input:
skillrack 
5
S+1 
2+S 
S+4 
S+1 
3+S

Output:
sksskskillrackkackkk
"""
# Solution
s = input().strip()
n = int(input()) 
for i in range(n):
    S = input().strip() 
    x, y = S.split('+') 
    if y.isdigit():
        s = s + s[-int(y):]
    else:
        s = s[:int(x)] + s
print(s)    
