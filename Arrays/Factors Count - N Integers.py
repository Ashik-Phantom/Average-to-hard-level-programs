#Factors Count - N Integers
"""
The program must accept N integers as the input. The program must find all the factors of the N integers. The program must print the distinct factors along with the number of occurrences. The number of occurrences of each factor must be enclosed within the parentheses. The factors must be printed in descending order based on the number of occurrences. If two or more factors have occurred the same number of times, then the program must sort those factors in ascending order.Note: Optimize your logic to avoid the Time Limit Exceeded error.Boundary Condition(s):2 <= N <= 1001 <= Each integer value <= 10^8Input Format:The first line contains N.The second line contains N integers separated by a space.Output Format:The first line contains the factors along with the number of occurrences.Example Input/Output 1:Input:56 9 12 8 17Output:1(5) 2(3) 3(3) 4(2) 6(2) 8(1) 9(1) 12(1) 17(1)Explanation:The factors of 6 is 1, 2, 3 and 6.The factors of 9 is 1, 3 and 9.The factors of 12 is 1, 2, 3, 4, 6, 12.The factors of 8 is 1, 2, 4 and 8.The factors of 17 is 1, 17.The factor 1 occurs 5 times.The factor 2 occurs 3 times.The factor 3 occurs 3 times.The factor 4 occurs 2 times.The factor 6 occurs 2 times.The factor 8 occurs once.The factor 9 occurs once.The factor 12 occurs once.The factor 17 occurs once.After sorting the factors based on the given conditions, the factors are1(5) 2(3) 3(3) 4(2) 6(2) 8(1) 9(1) 12(1) 17(1)Example Input/Output 2:Input:979 27 37 19 63 13 23 61 5Output:1(9) 3(2) 9(2) 5(1) 7(1) 13(1) 19(1) 21(1) 23(1) 27(1) 37(1) 61(1) 63(1) 79(1)
""" 

# Solution 1

n = int(input())
l = list(map(int,input().split()))
d = {} 
for num in l:
    for fact in range(1,int(num**0.5)+1):
        if num%fact == 0:
            if fact in d:
                d[fact] += 1
            else:
                d[fact] = 1 
            if fact == num//fact:
                continue
            if num//fact in d:
                d[num//fact] += 1 
            else:
                d[num//fact] = 1
for fact,count in sorted(d.items(),key = lambda x:[-x[1],x[0]]):
    print(fact,"(",count,")",sep="",end=" ")

  
# Solution 2
n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
            t=i//j
            if j!=t:
                if t in d:
                   d[t]+=1
                else:
                    d[t]=1
d=sorted(sorted(d.items(),key=lambda x:x[0]),key=lambda x:x[1],reverse=1)
for i in d:
    print(i[0],'(',i[1],')',sep='',end=' ')
