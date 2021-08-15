"""
Stars Black Holes Count 
The program must accept an R*C matrix consisting of 1s and 0s. 
A star is a cell which has 1 in it and surrounded by 0s. 
A black hole is a cell which has 0 in it and surrounded by all 1s. 
The program must print the count of stars and the count of black holes.
Boundary Condition(s):
2 <= R, C <= 100
Input Format:
The first line contains R and C separated by a space.The next R lines, 
each contains C integer values separated by a space.
Output Format:
The first line contains a string value "stars=" followed by the count of stars.
The second line contains a string value "blackholes=" followed by the count of black holes.
Example Input/Output 1:
Input:
5 6
1 0 0 0 1 0
0 0 1 0 1 1
0 0 0 0 1 1
1 0 1 1 1 0
0 0 0 1 1 1
Output:
stars=3
blackholes=2
Explanation:
The stars are denoted by S and the blackholes by B.
S 0 0 0 1 B
0 0 S 0 1 1
0 0 0 0 1 1
S 0 1 1 1 B
0 0 0 1 1 1
Example Input/Output 2:
Input:
5 6
1 0 0 0 1 0
0 0 1 0 1 1
0 0 0 0 1 1
1 1 1 1 1 0
0 1 0 1 1 1
Output:
stars=2
blackholes=4
"""

r,c=map(int,input().split()) 
