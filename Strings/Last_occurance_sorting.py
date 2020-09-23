"""
Last Occurrence Sorting
The program must accept two string values S1 and S2 as the input. 
The program must print the characters in S2 in ascending order based on the positions of their last occurrence in S1.Note: 
All the characters in S2 are always present in S1.
Boundary Condition(s):
1 <= Length of S1,S2 <= 100

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains a string representing the characters of S2 as per the given condition.
Example Input/Output 1:
Input:
earthquakes
shake
Output:
hakes
Explanation:
Here S1 is earthquakes and S2 is shake.
The position of the last occurrence of s in earthquakes is 11.
The position of the last occurrence of h in earthquakes is 5.
The position of the last occurrence of a in earthquakes is 8.
The position of the last occurrence of k in earthquakes is 9.
The position of the last occurrence of e in earthquakes is 10.
So the characters in shake are printed in ascending order based on the positions of their last occurrence in S1.Hence the output is hakes 
Example Input/Output 2:
Input:
Software
Hardwares
SHortS
Output:
SSotHr
"""

# Solution 

def o(ch,a): 
    for i in range(len(a)): 
        if ch==a[i]: 
            pos=i 
    return pos 
a=input().strip() 
b=input().strip() 
l=[] 
for i in b: 
    l.append(o(i,a)) 
l.sort() 
for x in l: 
    print(a[x],end="")
