# Non-overlapping Square Submatrices
"""
The program must accept an integer matrix of size RxC as the input. The program must print all possible non-overlapping square submatrices in the given matrix as the output. The non-overlapping square submatrices must be printed in increasing order of size.Boundary Condition(s):2 <= R, C <= 30Input Format:The first line contains R and C separated by a space.The next R lines, each contains C integers separated by a space.Output Format:The lines containing the non-overlapping square submatrices.Example Input/Output 1:Input:4 548 89 68 28 3093 89 98 37 6829 67 70 21 1232 19 72 89 53Output:48 8993 8968 2898 3729 6732 1970 2172 8948 89 6893 89 9829 67 7048 89 68 2893 89 98 3729 67 70 2132 19 72 89Explanation:In the given 4x5 matrix, the non-overlapping square submatrices are given below.48 8993 8968 2898 3729 6732 1970 2172 8948 89 6893 89 9829 67 7048 89 68 2893 89 98 3729 67 70 2132 19 72 89Example Input/Output 2:Input:5 661 65 85 18 56 1917 81 21 40 23 3516 79 12 62 59 5133 49 25 24 93 4771 50 63 86 29 66Output:61 6517 8185 1821 4056 1923 3516 7933 4912 6225 2459 5193 4761 65 8517 81 2116 79 1218 56 1940 23 3562 59 5161 65 85 1817 81 21 4016 79 12 6233 49 25 2461 65 85 18 5617 81 21 40 2316 79 12 62 5933 49 25 24 9371 50 63 86 29
"""

# Solution
r,c=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(r)]
index=min(r,c) 
for s in range(2,index+1): 
        row=r//s 
        for i in range(0,row*s,s): 
            col=c//s 
            for j in range(0,col*s,s): 
                if len(l[i:i+s])!=s: 
                    break 
                for ctr in range(i,i+s): 
                    for ctc in range(j,j+s): 
                        print(l[ctr][ctc],end=" ") 
                    print()
                    
