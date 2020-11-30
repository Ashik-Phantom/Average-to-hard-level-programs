# Nth Term - Powers of 2
"""
The program must accept an integer N as the input. The program must print the Nth term in the following sequence.
0 1 0 1 2 3 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0 1 2 . . . and so on.
The above sequence is formed using 0 to (21)-1, 0 to (22)-1, 0 to (23)-1, 0 to (24)-1, . . . and so on.
Note: Optimize your logic to avoid Time Limit Exceeded error.
Boundary Condition(s):1 <= N <= 10^18
Input Format:The first line contains N.
Output Format:The first line contains the Nth term in the sequence.

Example Input/Output 1:
Input:
5
Output:
2
Explanation:
The 5th term in the above sequence is 2.
So 2 is printed as the output.

Example Input/Output 2:
Input:
28
Output:
13
""" 
####################################
            Solution 1 
####################################

n = int(input()) 
a = 2 
while(n > a):
    n -= a 
    a *= 2  
print(n-1)

####################################
            Solution 2
####################################
n = int(input())
i = 0
while n -(2**i)>=0:
    n -=(2**i)
    i+=1
print(n)
