# Matrix Row - column pattern
#Print row and then column and so on as per the example patterns

"""
Example input/output 1:
Input:
5 5 
21 22 23 24 25 
26 27 28 29 30
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25  

Output:
21 22 23 24 25
26 11 16 21
27 28 29 30
12 17 22
13 14 15
18 23
19 20
24
25

Example input/output 2:
Input:
2 9
11 12 13 14 15 16 17 18 19
21 22 23 24 252 62 7 28 29
  
output:
11 12 13 14 15 16 17 18 19
21
22 23 24 252 62 7 28 29

Example input/output 3:
Input:
10 5 
11 22 33 44 55 
21 22 23 24 25 
31 32 34 33 35 
51 52 53 54 55 
41 43 46 47 48 
61 62 63 64 65 
71 72 73 74 75 
81 82 84 83 85
91 92 93 94 94
11 12 13 14 15
  
Output:
11 22 33 44 55
21 31 51 41 61 71 81 91 11
22 23 24 25
32 52 43 62 72 82 92 12
34 33 35
53 46 63 73 84 93 13
54 55
47 64 74 83 94 14
48
65 75 85 94 15
"""

# Solution
n,m=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(n)] 
while l: 
    print(*l[0]) 
    l=l[1:] 
    l=[list(i) for i in zip(*l)]
