# Substring Count - K Times
"""
The program must accept a string S and two integers L, K as the input. The program must print YES if at least one substring of length L has occurred K or more times consecutively in the string S. Else the program must print NO as the output.Boundary Condition(s):2 <= Length of S <= 10001 <= L <= Length of S2 <= K <= 20Input Format:The first line contains S.The second line contains L and K.Output Format:The first line contains YES or NO.
Example Input/Output 1:
Input:
abcccc
1 4
Output:
YES
Explanation:
Here S = abcccc, L = 1 and K = 4.The substring values of length 1 are a, b, c, c, c, c.The substring c has repeated 4 times consecutively. So YES is printed as the output.

Example Input/Output 2:
Input:
ababaaac
2 2
Output:
YES

Example Input/Output 3:
Input:
xyxyxzxy
2 3
Output:
NO
"""

s=input().strip()
l,k=map(int,input().split())
for i in range(len(s)-l+1):
    if s[i:i+l]*k in s:
        print("YES")
        exit(0)
print("NO")
