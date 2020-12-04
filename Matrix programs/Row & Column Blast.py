# Row & Column Blast
"""
The program must accept an integer matrix of size RxC and the positions of N cells as the input.
For each cell among the given N cells, the program must modify the matrix based on the following conditions.
- The program must decrement the value of the integer present in the given cell by (R+C).
- The program decrement the values of the integers present below the given cell by R-1, R-2, R-3 and so on (towards bottom).
- The program decrement the values of the integers present above the given cell by R-1, R-2, R-3 and so on (towards top).
- The program decrement the values of the integers present right to the given cell by C-1, C-2, C-3 and so on (towards right).
- The program decrement the values of the integers present left to the given cell by C-1, C-2, C-3 and so on (towards left).
Finally, the program must print the modified matrix as the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 1000
1 <= N <= 100
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The (R+2)nd line contains N.The next N lines, each contains two integers representing the position of a cell.
Output Format:
The first R lines, each contains C integers representing the modified matrix.
Example Input/Output 1:
Input:
6 6
77 99 22 92 41 65
96 94 83 46 45 71
86 67 58 20 28 23
34 42 87 47 13 26
52 21 75 90 14 66
37 18 43 11 79 82
3
2 2
4 6
1 3
Output:
73 89 10 87 37 59
91 82 73 42 42 65
86 62 54 20 28 18
33 36 81 43 8 14
52 18 73 90 14 61
37 16 42 11 79 78
Explanation:
After modifying the matrix for the cell (2, 2), the matrix becomes
77 94 22 92 41 65
91 82 78 42 42 69
86 62 58 20 28 23
34 38 87 47 13 26
52 18 75 90 14 66
37 16 43 11 79 82
After modifying the matrix for the cell (4, 6), the matrix becomes
77 94 22 92 41 62
91 82 78 42 42 65
86 62 58 20 28 18
33 36 84 43 8 14
52 18 75 90 14 61
37 16 43 11 79 78
After modifying the matrix for the cell (1, 3), the matrix becomes
73 89 10 87 37 59
91 82 73 42 42 65
86 62 54 20 28 18
33 36 81 43 8 14
52 18 73 90 14 61
37 16 42 11 79 78

Example Input/Output 2:
Input:
5 4
28 24 23 30
11 27 22 19
18 26 20 16
14 29 12 13
21 15 10 25
6
1 3
3 4
5 1
4 2
2 1
5 3
Output:
21 19 13 24
0 21 14 14
10 20 11 7
4 20 3 7
8 5 -2 18
"""

#Solution
