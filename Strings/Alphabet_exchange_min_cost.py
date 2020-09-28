# Minimum Cost - Alphabet Exchange
""" 
The program must accept 26 integers representing the frequency of 26 lower case alphabets as the input. The cost to exchange an alphabet with another alphabet is equal to the absolute difference between their ASCII values. The program must print the minimum cost to convert all alphabets to the same.Boundary Condition(s):0 <= Each integer value <= 50Input Format:The first line contains 26 integers separated by a space.Output Format:The first line contains an integer representing the minimum cost to convert all alphabets to the same.Example Input/Output 1:Input:0 2 0 3 0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0Output:14Explanation:The minimum cost 14 is obtained by exchanging all alphabets with d or e or f.So 14 is printed as the output.Example Input/Output 2:Input:1 1 1 2 0 3 0 5 6 0 7 0 8 0 1 0 2 0 3 1 1 1 2 3 4 0Output:288
"""

# Solution
s = input().split() 
a = 97 
l = {} 
for i in s: 
    if int(i) > 0: 
        l[chr(a)] = int(i) 
    a+=1 
if len(l) == 0:
    print(0)
    exit()
result = []
for i in l.keys(): 
    val = ord(i) 
    h = 0 
    for j in l.keys(): 
        if i != j: 
            for k in range(l[j]): 
                g = abs(val-ord(j)) 
                h += g 
    result.append(h)
print(min(result))
