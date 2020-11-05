# Longest Prefix Suffix
"""
The program must accept a string S as the input. The program must print the length of the longest proper prefix which is also a proper suffix in S. 
If there is no common proper prefix and proper suffix, the program must print -1 as the output.
Note: The proper prefix and proper suffix may overlap in the string S.
Boundary Condition(s):1 <= Length of S <= 10^5
Input Format:The first line contains S.
Output Format:The first line contains the length of the longest proper prefix which is also a proper suffix in S or -1.
Example Input/Output 1:
Input:
abcdxyzabcd
Output:4
Explanation:
The longest proper prefix which is also a proper suffix in the string abcdxyzabcd is abcd.
So the length of the proper prefix or proper suffix is 4.So 4 is printed as the output.
Example Input/Output 2:
Input:
PQRSPQRSP
Output:
5
Example Input/Output 3:
Input:
xyzabcxyzc
Output:
-1
"""

# Solution

s=input().strip()
n=len(s)
for i in range(n-1,0,-1):
    if s[:i]==s[-i:]:
        print(len(s[:i]))
        exit()
print(-1)
