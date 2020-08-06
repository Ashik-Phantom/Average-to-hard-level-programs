"""
CLOCKWISE - SPIRAL REPLACE ODD INTEGERS
Problem statement:
		Get an input 'N' and get an matrix of size 'n X n' and get a 
string 'A' write a program that checks elemnets in the matrix 
'SPIRAL-CLOCKWISE' and if it encounters an odd integer it should be 
replace with the elements of the string 'A' if the number of odd 
integers is greater than the length of the string then the program must 
start replacing the integer circularly

---------------------------------------------------------------
Test case 1:
Input:
3
7 8 9
6 3 4
1 5 7
rock

output:
r 8 o
6 o 4 
r k c
--------------------------------------------------------------
Testcase 2:
Input: 
6 
12 23 34 4 6 89 
31 55 45 15 87 91 
63 74 32 44 98 86
23 43 56 87 99 54
11 34 56 88 98 45
34 44 46 88 67 54 
ENVIRONMENT

output: 
12 E 34 4 6 N
E N T E N V
M 74 32 44 98 86
N I 56 R V 54
O 34 56 88 98 I
34 44 46 88 R 54
------------------------------------------------------------
""" 

#Solution: 

s=int(input())
arr=[list(map(int,input().split())) for i in range(s)] 
a=input().strip() 
lena=len(a) 
n,m,k,l,o=s,s,0,0,0 
# k - starting row index 
# m - ending row index 
# l - starting column index 
# n - ending column index 
# i - iterator  
# o - itretion of the string
while(k<m and l<n): 
	#first element of every column
	for i in range(l,n): 
		if arr[k][i]%2==1: 
			arr[k][i]=a[o] 
			o+=1 
		if o==lena: 
			o=0 
	k+=1 
	#last element of every column
	for i in range(k,m): 
		if arr[i][n-1]%2==1:
			 arr[i][n-1]=a[o] 
			 o+=1 
		if o==lena: 
			o=0 
	n-=1 
	#last element of every column if Last and First row are not same
	if k<m: 
		for i in range(n-1,l-1,-1):
			if arr[m-1][i]%2==1: 
				arr[m-1][i]=a[o] 
				o+=1 
			if o==lena: 
				o=0 
		m-=1 
	#first element of every row if Last and First column are not same
	if l<n: 
		for i in range(m-1,k-1,-1): 
			if arr[i][l]%2==1: 
				arr[i][l]=a[o] 
				o+=1 
			if o==lena: 
				o=0 
		l+=1
for i in arr: 
	print(*i)
#code by Ashik-Phantom
