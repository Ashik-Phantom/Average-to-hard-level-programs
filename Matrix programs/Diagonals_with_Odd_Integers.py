# Diagonals with Odd Integers
"""
The program must accept an integer matrix of size RxC as the input. The program must print the number of diagonals having only odd integers that are parallel to the 
top-left to bottom-right diagonal and the top-right to bottom-left diagonal in the matrix.

Boundary Condition(s):
2 <= R, C <= 100
Input Format:
The first line contains R and C separated by a space.The next R lines, each contains C integers separated by a space.
Output Format:
The first line contains an integer representing the number of diagonals having only odd integers in the matrix.

Example Input/Output 1:
Input:
5 5
60 37 26 98 73
29 50 32 52 43
52 19 29 81 33
13 94 17 63 80
90 25 77 11 54
Output:
6
Explanation:
The diagonals that are parallel to the top-left to bottom-right diagonal and having only odd integers are stared below.
Legend:
+ --> Diagnal line
* --> odd lines
+60 37 26 98 *73
*29 +50 32 52 43
52 *19 +29 81 33
*13 94 *17 +63 80
90 *25 77 *11 +54
Total number of diagnals that are parallel to the top-left to bottom-right and having only odd integers are 3 

The diagonals that are parallel to the top-right to bottom-left diagonal and having only odd integers are highlighted below.
60 *37 26 98 +73
*29 50 32 +52 *43
52 19 +29 *81 *33
13 +94 *17 *63 80
+90 *25 *77 11 54
Total number of diagnals that are parallel to the top-right to bottom-left diagonal and having only odd integers are 3
Here the total number of diagonals in both the order with only odd integers is 6. 
So 6 is printed as the output.

Example Input/Output 2:
Input:
4 3
354 234 259
104 384 352
331 289 127
127 261 288
Output:
4
"""

# Solution 

# top left to bottom right diagonal
def top_left_to_bottom_right_diagonal(r, c, l): 
    g = [[l[i - j][j] for j in range(max(i - r + 1, 0), min(i + 1, c))] for i in range(r + c - 1)] 
    return g 

# top right to bottom left diagonal
def top_right_to_bottom_left_diagonal(r, c, l): 
    p = {x : [] for x in range(r-1, -c, -1)} 
    for i in range(r): 
        for j in range(c): 
            p[i - j].append(l[i][j]) 
    g = [i for i in p.values()] 
    return g

# count of odd diagnals
def count_of_odd_diagnals(count,l):
    for i in l: 
        f = 0 
        for j in i: 
            if j % 2 == 0: 
                f = 1 
        if f == 0: 
            count += 1
    return count    
 
# Main
r, c = map(int, input().split()) 
l = [list(map(int, input().split())) for i in range(r)] 
count = 0
count = count_of_odd_diagnals(count, top_left_to_bottom_right_diagonal(r, c, l))
count = count_of_odd_diagnals(count, top_right_to_bottom_left_diagonal(r, c, l))
print(count)
