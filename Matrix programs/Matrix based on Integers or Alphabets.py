""" Matrix - Integers / Alphabets """
"""
The program must accept a character matrix of size RxC containing only alphabets and digits as the input. The program must find the number of alphabets A and the number of digits D in the given character matrix. Then the program must print the output based on the following conditions.- If the value of A is a perfect square, then the program must print all the alphabets as a square matrix.- If the value of D is a perfect square, then the program must print all the digits as a square matrix.- If both A and D are perfect squares, then the program must print the square matrix based on the maximum value between A and D.- If both A and D are perfect squares and equal, then the program must print all the alphabets as a square matrix.Note: At least one of the values A and D is always a perfect square.Boundary Condition(s):2 <= R, C <= 50Input Format:The first line contains R and C separated by a space.The next R lines, each contains C characters separated by a space.Output Format:The line(s) containing a square matrix based on the given conditions.Example Input/Output 1:Input:3 3a 1 bc d e2 3 4Output:1 23 4Explanation:The number of alphabets A is 5 and the number of digits D is 4.Here 4 is a perfect square and 5 is not a perfect square.So all the 4 digits are printed as a square matrix (4 = 2 * 2).Hence the output is1 23 4Example Input/Output 2:Input:3 4U 5 e PZ X o 8w E 4 rOutput:U e PZ X ow E rExample Input/Output 3:Input:2 31 a 23 4 5Output:a
"""

def printMat(N,lis):
    ind=0
    for row in range(N):
        for col in range(N):
            print(lis[ind],end=" ")
            ind+=1
        print()
R,C=map(int,input().split())
matrix=[list(map(str,input().split())) for row in range(R)]
alphabets,digits=[],[]
for row in matrix:
    for ch in row:
        if ch.isalpha():
            alphabets.append(ch)
        else:
            digits.append(ch)
A,D=int(len(alphabets)**0.5),int(len(digits)**0.5)
if A*A==len(alphabets) and D*D==len(digits):
    if A==D:
        printMat(A,alphabets)
    elif A>D:
        printMat(A,alphabets)
    else:
        printMat(D,digits)
elif A*A==len(alphabets):
    printMat(A,alphabets)
else:
    printMat(D,digits)
