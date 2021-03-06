# Consonants & Square Brackets
"""
The program must accept a string S containing only alphabets as the input. The program must find the number of consonants C in the string S. 
Then the program must print the string in (C+1)/2 lines based on the following conditions.
- In the first line, the program must enclose the 1st and Cth consonants within square brackets [ ]. Then the program must print the modified string S.
- In the second line, the program must enclose the 2nd and (C-1)th consonants within the square brackets [ ]. Then the program must print the modified string S.
- Similarly, the program must print the remaining lines as the output.Note: At least one consonant is always present in the string S.
Boundary Condition(s):
2 <= Length of S <= 100
Input Format:The first line contains S.
Output Format:The first (C+1)/2 lines, each contains a string.
Example 
Input/Output 1:
Input:
skillrack
Output:
[s]killrac[k]
[s][k]illra[c][k]
[s][k]i[l]l[r]a[c][k]
[s][k]i[l][l][r]a[c][k]
Explanation:
Here S = "skillrack".The number of consonants in the string S is 7. So (7+1)/2 lines are printed as the output.In the first line, 
the 1st and 7th consonants are enclosed within the square brackets.Now the string becomes [s]killrac[k].In the second line, 
the 2nd and 6th consonants are enclosed within the square brackets.Now the string becomes [s][k]illra[c][k].In the third line, 
the 3rd and 5th consonants are enclosed within the square brackets.Now the string becomes [s][k]i[l]l[r]a[c][k].In the fourth line,
the 4th consonant is enclosed within the square brackets.Now the string becomes [s][k]i[l][l][r]a[c][k].
Example Input/Output 2:
Input:
Zombies
Output:
[Z]ombie[s]
[Z]o[m][b]ie[s]
"""

s=list(input().strip())
l=[]
for i in range(len(s)):
    if s[i].lower() not in "aeiou":
        l.append(i)
for i in range((len(l)+1)//2):
    s[l[i]],s[l[-i-1]]="["+s[l[i]]+"]","["+s[l[-i-1]]+"]"
    print(*s,sep="")
