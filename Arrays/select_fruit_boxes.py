# Select Fruit Boxes
# Dificulty: HARD
"""
A fruit shop owner announces a game to win fruits. The shop owner placed N boxes in a straight line, each box containing a certain number of fruits. 
The rules of the game are given below.
- A customer can pick any number of boxes but if the customer picks a box, then he/she should not pick the boxes which are adjacent to it (left and right).
- The customer not allowed to rearrange the boxes.The program must accept N integers representing the number of fruits in the N boxes as the input. 
The program must print the maximum number of fruits M that the customer can get as the output.

Boundary Condition(s):2 <= N <= 10001 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:The first line contains M.

Example Input/Output 1:
Input:4
5 3 11 20
Output:
25
Explanation:
The three possible ways to select the boxes are given below.
5, 11
5, 20
3, 20
The maximum number of fruits that the customer can get is 25 (5 + 20).
So 25 is printed as the output.
Example Input/Output 2:
Input:7
10 20 15 1 9 12 2
Output:
37
""" 
#################################
# Solution 1 Dynamic programing 
#################################
n=int(input())
l=list(map(int,input().split()))
dp=[0]*n
dp[0]=l[0]
dp[1]=l[1]
for i in range(2,n):
    dp[i]=l[i]+max(dp[:i-1])
print(max(dp))

#################################
# Solution 2
#################################
n=int(input())
l=list(map(int,input().strip().split()))
curr = l[0]
prev = 0
for i in l[1:]:
    curr = max(i+prev,curr)
    prev = curr
print(curr)

#################################
# Solution 3
#################################
n=int(input())
l=list(map(int,input().split()))
for i in range(2,n):
    l[i]=max(l[i]+max(l[:i-1]),l[i-1])
print(l[n-1])

