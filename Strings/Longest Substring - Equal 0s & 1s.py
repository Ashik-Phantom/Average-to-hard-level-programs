# Longest Substring - Equal 0s & 1s
"""
The program must accept a string S containing only 0s and 1s as the input. The program must print the longest substring of S based on the following conditions.
- The number of 0s must be equal to the number of 1s in the substring.
- All 1s must be present in the first half or the second half of the substring.
If two or more such longest substrings are present in S, the program must print the first occurring substring as the output. 
If there is no such substring, the program must print -1 as the output.
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the substring of S as per the given conditions or -1.

Example Input/Output 1:
Input:
011011000
Output:
1100
Explanation:
The given string is 011011000.The longest substring with equal 1s and 0s where all the 1s present in the first half is 1100.
So 1100 is printed as the output.

Example Input/Output 2:
Input:
000111001100111000
Output:
000111

Example Input/Output 3:
Input:
1111111
Output:
-1
""" 

#########################################################################
##############                Solution 1             ####################
#########################################################################

S=input().strip()
for length in range(len(S),0,-1):
    for index in range(0,len(S)-length+1):
        subStr=S[index:index+length]
        if subStr.count('0')==subStr.count('1'):
            middle=length//2
            if len(set(subStr[:middle]))==1 or len(set(subStr[middle:]))==1:
                print(subStr)
                exit()
print(-1)

#########################################################################
##############                Solution 2             ####################
#########################################################################

n=input().strip()
for i in range(len(n),1,-1):
    for j in range(len(n)-i+1):
        a=n[j:j+i];
        x=len(a)//2
        if a.count('1')==a.count('0') and len(set(a[:a.count('0')]))==1:
            print(a);
            exit()
print(-1)

#########################################################################
##############                Solution 3             ####################
#########################################################################

s=input().strip()
l=len(s)
a=[]
for i in range(l):
    for j in range(l,i,-1):
        t=s[i:j]
        c=(j-i)//2
        r='1'*c+'0'*c
        if t==r or t==r[::-1]:
            a.append(t)
if a:
    print(max(a,key=len))
else:
    print(-1)
    
#########################################################################
##############                Solution 4             ####################
#########################################################################

s=input().strip()
n=(len(s)+1)//2
l=[]
for i in range(n,0,-1):
    t=('1'*i)+('0'*i)
    if t in s:
        l.append(t)
    if t[::-1] in s:
        l.append(t[::-1])
    if l:
        print(sorted(l,key=lambda x:s.index(x))[0]),exit()
print(-1)
