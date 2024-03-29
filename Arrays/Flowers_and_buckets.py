"""
Flowers and Buckets
In a garden, there are N trees in a row. 
Each tree has a certain number of flowers. An empty bucket is placed under each tree to collect the falling flowers. 
If the wind blows on the right side, a flower from each tree will fall into the bucket on its left side. Similarly, 
if the wind blows on the left side, a flower from each tree will fall into the bucket on its right side.
The program must accept N integers representing the number of flowers in the N trees and a string S as the input. 
The string S contains only L's and R's, where L indicates that the wind blows on the left side and R indicates that the wind blows on the right side.
The program must print the number of flowers collected in each bucket in the end as the output.

Note: If a flower falls on the left side of the first tree or a flower falls on the right side of the last tree, 
it means that the flower is falling outside of the garden and hence it is not collected in any of the buckets.
Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 1000
1 <= Length of S <= 1000
Input Format:
The first line contains N.The second line contains N integer values separated by a space.The third line contains S.
Output Format:The first line contains N integer values separated by a space.
Example Input/Output 1:
Input:
4
10 3 6 5
LRRL
Output:
2 4 3 2
Explanation:The given string S = LRRL.
Initially, all 4 buckets are empty.
0 0 0 0
1st character L: After the wind blows on the left side, the number of flowers in the buckets become
0 1 1 1
2nd character R: After the wind blows on the right side, the number of flowers in the buckets become
1 2 2 1
3rd character R: After the wind blows on the right side, the number of flowers in the buckets become
2 3 3 1
4th character L: After the wind blows on the left side, the number of flowers in the buckets become
2 4 3 2

Example Input/Output 2:
Input:
8
4 11 11 4 12 14 5 4
RRLLRLLLR
Output:
4 6 7 9 6 8 7 2
"""




#Your code below
n=int(input()) 
l=list(map(int,input().split())) 
s=input().strip() 
bkt=[0 for i in range(n)] 
for i in s:
    if i=='L':
        for j in range(n): 
            if l[j]>0:
                if j!=n-1:
                    bkt[j+1]+=1 
                l[j]-=1 
    elif i=='R':
        for j in range(n):
            if l[j]>0:
                if j!=0:
                    bkt[j-1]+=1 
                l[j]-=1 
print(*bkt)
