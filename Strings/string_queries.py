#String -Queries
"""
Example Input/Output:
Input:
skillrack 
5
s+1 
2+s 
s+4 
s+1 
3+s

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
