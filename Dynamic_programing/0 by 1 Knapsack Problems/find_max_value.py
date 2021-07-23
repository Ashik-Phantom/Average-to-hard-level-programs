"""
Given a knapsack with capacity C and two arrays w[] and val[] representing the weights and values of N distinct items, 
the task is to find the maximum value you can put into the knapsack.
Items cannot be broken and an item with weight X takes X capacity of the knapsack.
"""

n, w = map(int,input().split()) 
wt = list(map(int,input().split())) 
val = list(map(int,input().split())) 
r,c = n+1,w+1
dp = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        if i==0 or j==0:
            dp[i][j] = 0 
        elif j>=wt[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i-1]] + val[i-1])
        else:
            dp[i][j] = dp[i-1][j] 
for i in dp:
    for j in i:
        print(j,end=" ")
    print()


"""
4 8 
2 5 4 3
3 6 7 2
ans 10
6 9
3 1 5 8 4 2
10 8 19 15 20 16
ans 46
"""
