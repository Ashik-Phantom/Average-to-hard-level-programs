 # Integer & Asterisks Decryption
 """
 The program must accept a string S (encrypted string) containing digits and asterisks as the input. The encryption algorithm is given below.
 - The alphabets from a to j are replaced with the digits from 0 to 9 respectively.
 - The alphabets from k to z are replaced with the values from 10* to 25* respectively.
 The program must decrypt the string S and print it as the output.Note: The string S is always a valid encrypted string.
 Boundary Condition(s):1 <= Length of S <= 100
 Input Format:The first line contains S.
 Output Format:The first line contains the decrypted string S.
 Example Input/Output 1:
 Input:
 18*10*811*11*17*0210*
 Output:
 skillrack
 Explanation:
 Here S = 18*10*811*11*17*0210*.
 18* is replaced with the alphabet s. Now the string becomes s10*811*11*17*0210*.
 10* is replaced with the alphabet k. Now the string becomes sk811*11*17*0210*.
 8 is replaced with the alphabet i. Now the string becomes ski11*11*17*0210*.
 11* is replaced with the alphabet l. Now the string becomes skil11*17*0210*.
 11* is replaced with the alphabet l. Now the string becomes skill17*0210*.
 17* is replaced with the alphabet r. Now the string becomes skillr0210*.
 0 is replaced with the alphabet a. Now the string becomes skillra210*.
 2 is replaced with the alphabet c. Now the string becomes skillrac10*.
 10* is replaced with the alphabet k. Now the string becomes skillrack.
 So skillrack is printed as the output.
 
 Example Input/Output 2:
 Input:
 15*17*14*617*012*12*813*6
 Output:
 programming
 """ 
 
 # Solution
 
 x = input().strip()
alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(10,26):
    s = str(i)+"*"
    x = x.replace(s,alp[i])
for i in range(0,10):
    x = x.replace(str(i),alp[i])
print(x)
