#Vehicle Registration Number
""" 
The program must accept a string S representing the registration number of a vehicle and an integer K as the input. 
The registration number of a vehicle is generated based on the following conditions.
- The format of the vehicle registration number is either #-#### or ##-####.
- The first part (# or ##) of the vehicle registration number represents the following alphabet series.A, B, C, D, E, .... X, Y, Z, AA, AB, AC, AD, .... AX, AY, AZ, BA, BB, BC, BD, .... ZX, ZY and ZZ.
- The second part (####) of the vehicle registration number represents the following integer series.0001, 0002, 0003, 0004, 0005, .... 9996, 9997, 9998 and 9999.
- The vehicle registration number is generated by combining the above two series.A-0001, A-0002, A-0003, .... A-9998, A-9999, AA-0001, AA-0002, AA-0003, .... ZZ-9997, ZZ-9998 and ZZ-9999.
The program must print the Kth registration number from the given registration number as the output.
Note: The Kth registration number from the given registration number is always valid.
Boundary Condition(s):6 <= Length of S <= 71 <= K <= 9999
Input Format:The first line contains the registration number S.The second line contains K.
Output Format:The first line contains the Kth registration number from the given registration number.

Example Input/Output 1:
Input:
TM-998040
Output:
TN-0021
Explanation:
The given registration number is TM-9980.
The 40th registration number from TM-9980 is TN-0021.
So TN-0021 is printed as the output.

Example Input/Output 2:
Input:
Z-89801779
Output:
AA-0760
"""
#####################################
# logic 1 
#####################################

r,c=map(int,input().split())
m=[[int(j) for j in input().split()]for i in range(r)]
k=[]
t=0
for i in range(r-1,-1,-1):
    if t%2==0:
        for j in range(c):
            k.append(m[i][j])
    else:
        for j in range(c-1,-1,-1):
            k.append(m[i][j])
    t+=1
s=100000
for i in range(c):
    t=1
    y=k[i]
    z=i
    while(z<len(k)):
        z+=y
        if z>=len(k):
            break
        y=k[z]
        t+=1
    if t<s:
        s=t
print(s)
        
#######################
# logic 2 
#######################

r,c = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]
ans = []
for i in range(c):
    x,y = r-1,i
    cnt = 0
    while x in range(r) and y in range(c):
        t = a[x][y]
        cnt += 1
        while t:
            if r%2 != x%2:
                y += 1
                if y == c:
                    y-=1
                    x-=1
            else:
                y -= 1
                if y == -1:
                    y+=1
                    x-=1
            t -= 1
    ans.append(cnt)
print(min(ans))
