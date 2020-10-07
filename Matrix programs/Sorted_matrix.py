# Sorted Submatrix
"""
The program must accept an integer matrix of size RxC and an integer M as the input. 
The program must print YES if the given matrix contains at least one submatrix of size MxM where all the integers in each row and column are sorted in ascending order. 
Else the program must print NO as the output.Note: The value of M is always less than or equal to the minimum between R and C.
Boundary Condition(s):
2 <= R, C <= 502 <= M <= 10
Input Format:The first line contains R and C separated by a space.The next R lines, each contains C integers separated by a space.The (R+2)nd line contains M.
Output Format:The first line contains YES or NO.
Example Input/Output 1:
Input:
4 5
1 9 1 2 4
8 9 2 3 6
3 7 5 7 8
5 1 2 3 4
3
Output:
YES
Explanation:In the given 4x5 matrix, the 3x3 sub-matrix with sorted rows and columns is highlighted below.
1 9 1 2 4
8 9 2 3 6
3 7 5 7 8
5 1 2 3 4
So YES is printed as the output.

Example Input/Output 2:
Input:
3 4
1 2 3 4
5 6 7 8
9 0 1 23
Output:
NO
"""
