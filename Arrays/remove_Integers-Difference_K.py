"""
Example test case 1:
Input:
1 3 4 9 10 11 12 17 20
4
Output:
5

Explanation:
After removing the integers 1, 3, 4, 17 and 20 from the list, the list becomes 9 10 11 12.
Here, the difference between the maximum and the minimum is 3 (12-9) which is less than 4.So the minimum count to remove is 5.

Example Input/Output 2:
Input:
7 8 6 5 4 3
5
Output:
0

Example Input/Output 3:
Input:
30 10 20 40 15 70 90 16 100
5
Output:
6
"""
# Solution 

a = list(map(int,input().split()))
k = int(input())
a.sort()
b = []
c = 0
for i in range(len(a)):
    for j in range(len(a)-1, i, -1):
        if(a[j] - a[i] <= k):
            b.append(i + (len(a) - j - 1))
print(min(b))
