"""
Max Coupon Amount 
A matrix of size R*C contains the coupon amount. A person if he picks a coupon amount in a column, 
he cannot pick the adjacent coupon amount in the previous or the next column. 
The program must print the maximum amount that can be picked by the person by choosing a maximum of one coupon amount in each column.
Boundary Condition(s):3 <= R, C <= 1001 <= Coupon amount <= 10^5
Input Format:The first line contains R and C separated by a space.The next R lines, each contains C integers separated by a space.
Output Format:The first line contain an integer representing the maximum amount that can be picked by the person by choosing a maximum 
of one coupon amount in each column.
Example Input/Output 1:
Input:
4 5
10 5 2 8 20
20 1 6 4 80
30 3 8 4 10
15 2 5 3 30
Output:
111
Explanation:The max coupon can be collected by choosing 
20 2 6 3 80.
Example Input/Output 2:
Input:
3 3
10 500 400
50 200 2000
90 1000 400
Output:
1410
Explanation:The max coupon can be collected by choosing 10 1000 400.Max Execution Time Limit: 50 millisecs
"""
