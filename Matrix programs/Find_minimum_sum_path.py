"""
Alphabet Matrix - Minimum Sum Path
The program must accept a matrix of size R*C containing only alphabets as the input. Each alphabet has a weight, which is equal to the position of the alphabet in the English alphabet set. The positions of two cells (X1, Y1) and (X2, Y2) in the matrix are also passed as the input. The program must print the minimum sum of the weights of the alphabets in the path between the given two cells(both inclusive). The path must be formed based on the following conditions.
- Only horizontal and vertical movements are allowed.
- If two cells are present in the same row or column, then the two cells must be connected directly. Else the two cells must be connected by the path which has exactly one change in the direction.

Boundary Condition(s):
2 <= R, C <= 50
1 <= X1, X2 <= R
1 <= Y1, Y2 <= C

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The (R+2)th line contains X1 and Y1 separated by a space.
The (R+3)th line contains X2 and Y2 separated by a space.

Output Format:
The first line contains an integer representing the minimum sum of the weights of the alphabets.

Example Input/Output 1:
Input:
4 5
W I g k E
M l Z a p
d c A j h
D a h F E
2 5
2 2

Output:
55

Explanation:
Here the given two cells are present in the same row.
So they are connected directly as given below.
p -> a -> Z -> l
The sum of weights of all the alphabets in the above path is 55 (16+1+26+12).
Hence 55 is printed as the output.

Example Input/Output 2:
Input:
3 3
j p t
V u O
P h S
1 1
3 3

Output:
75

Explanation:
There are two possible paths between the given two cells.
Path 1: j -> p -> t -> O -> S = (10+16+20+15+19) = 80
Path 2: j -> V -> P -> h -> S = (10+22+16+8+19) = 75
Here the minimum sum is 75, which is printed as the output.
"""

#Solution 
