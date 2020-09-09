# Replace - Four Directions
"""
The program must accept an integer matrix of size RxC and an integer X as the input.
The program must replace the integers with asterisks (*) in the north-east, south-east, south-west and north-west directions of X(including X) in the matrix. 
Then the program must print the modified matrix as the output.Note: The integer X has occurred only once in the RxC integer matrix.
Boundary Condition(s):
2 <= R, C <= 50
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
Output Format:
The first R lines contain the modified matrix.

Example Input/Output 1:
Input:
5 4
14 13 46 24
33 35 30 18
12 22 23 27
31 21 26 44
47 10 36 49
22
Output:
14 13 46 * 
* 35 * 18 
12 * 23 27
* 21 * 44
47 10 36 *
Explanation:
The integers in the north-east, south-east, south-west and north-west directions of 22 are highlighted in the 5x4 matrix.
14 13 46 24
33 35 30 18
12 22 23 27
31 21 26 44
47 10 36 49
So those integers are replaced with asterisks (*) in the matrix.Hence the output is
14 13 46 *
* 35 * 18
12 * 23 27
* 21 * 44
47 10 36 *
Example Input/Output 2:
Input:
4 4
31 73 29 87
77 44 66 46
90 9 10 43
3 1 39 34
10
Output:
* 73 29 87
77 * 66 *
90 9 * 43
3 * 39 *
"""

#solution
from collections import defaultdict as dt
r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
x=int(input()) 
d1 = dt(list)
d2 = dt(list) 
for i in range(r):
	for j in range(c):
		d1[i-j].append(m[i][j])
		d2[i+j].append(m[i][j])
k1=[i for i in d1.keys()]
k2=[i for i in d2.keys()]
for i in k1:
	if x in d1[i]:
		a=i
	if x in d2[i]:
		b=i		
print("\nkey1=",a)
print("key2=",b)
print()
for i in range(r):
	for j in range(c):
		if i-j==a or i+j==b:
			print("*",end=" ")
		else:
			print(m[i][j],end=" ")
	print()

