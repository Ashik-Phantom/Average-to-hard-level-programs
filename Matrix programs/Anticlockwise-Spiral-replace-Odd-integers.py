"""
Problem statement:
		Get an input 'S' and get an matrix of size 'S X S' and get a 
string 'A' write a program that checks elemnets in the matrix 
'SPIRAL-ANTICLOCKWISE' and if it encounters an odd integer it should be 
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
r 8 r
6 o 4
o c k

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

------------------------------------------------------------"""

s=int(input())
arr=[list(map(int,input().split())) for i in range(s)] 
a=input().strip() 
lenn=len(a)
k,l,n,m,o=0,0,s,s,0
# k - starting row index 
# m - ending row index 
# l - starting column index 
# n - ending column index 
# i - iterator  
# o - itretion of the string

# initialize the count 
c= 0

# total number of elements in matrix 
total = m * n 

while (k<m and l<n): 
	if (c==total): 
		break
		
	#first column from the remaining columns  
	for i in range(k, m):
	    if(arr[i][l]%2==1):
	        arr[i][l]=a[o]
	        o+=1
	    if o==lenn:
	        o=0
	    c+=1  
	l+=1

	if (c==total) : 
		break

	#last row from the remaining rows  
	for i in range (l, n):
	    if arr[m-1][i]%2==1:
	        arr[m - 1][i]=a[o]
	        o+=1
	    if o==lenn:
		    o=0
	    c+=1	  
	m-=1
	  
	if (c==total) : 
		break

	#last column from the remaining columns  
	if (k < m) : 
		for i in range(m - 1, k - 1, -1):
		    if arr[i][n-1]%2==1:
		        arr[i][n - 1]=a[o]
		        o+=1
		    if o==lenn:
			    o=0
		    c+=1
		n-=1

	if (c==total) : 
		break

	#first row from the remaining rows  
	if (l<n) : 
	    for i in range(n - 1, l - 1, -1):
	        if arr[k][i]%2==1:
	            arr[k][i]=a[o]
	            o+=1
	        if o==lenn:
	            o=0
	        c+=1			  
	    k += 1
#print the replaced matrix
for i in arr: 
	print(*i)
