# Matrix Traversal - Path
"""
The program must accept an integer matrix of size RxC, the position (X, Y) of a cell and a string P representing a path containing the characters >, v, < and ^ as the input. 
The path P always starts from the given cell (X, Y). The program must print the integers which are present in the given path P. 
The four characters in the path P representing the four directions.
- The character > indicates that the next cell is on the right.
- The character v indicates that the next cell is on the bottom.
- The character < indicates that the next cell is on the left.
- The character ^ indicates that the next cell is on the top.
If the path P is not valid (i.e., if it crosses the edges of the matrix), the program must print the string value "Invalid Path" as the output.

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The (R+2)nd line contains X and Y separated by a space.
The (R+3)rd line contains P.

Output Format:
The first line contains the integer value(s) present in the given path P or "Invalid Path".
Example Input/Output 1:
Input:
5 5
1 2 3 4 5
6 7 8 9 0
1 2 3 4 5
6 7 8 9 0
1 2 3 4 5
1 2
>>>v

Output:
2 3 4 5 0

Explanation:
The starting position of the path is (1, 2).
The path P is >>>v.
The integers present in the given path P are stared below.
1 2 3 4 5
6 7 8 9 0
1 *2 *3 *4 *5
6 7 8 9 *0
1 2 3 4 5
Hence the output is 2 3 4 5 0

Example Input/Output 2:
Input:
3 4
1 2 3 4
5 6 7 8
1 2 3 0
1 1
>>vv<v>
Output:
Invalid Path

"""
# Solution

r, c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(r)]
x, y = map(int, input().split())
x, y = x-1, y-1
s = input().strip()
k = [l[x][y]]
for i in s:
    if i == '^':
       x -= 1 
    elif i == '<':
        y -= 1
    elif i == '>':
        y += 1
    elif i == 'v':
        x += 1
    if x >= 0 and y >= 0 and x < r and y < c:
        k.append(l[x][y])
    else:
        print("Invalid Path")
        exit()
print(*k)
