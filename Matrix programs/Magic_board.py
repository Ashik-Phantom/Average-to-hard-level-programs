m, n = map(int, input().split())
no_of_reds = int(input())
reds, blues = [], []
for i in range(no_of_reds):
    A = input().strip()
    x, y = A.split()
    f = [int(x),int(y)]
    reds.append(f)
no_of_blues = int(input())
for i in range(no_of_blues):
    A = input().strip()
    x, y = A.split()
    f = [int(x),int(y)]
    blues.append(f)
moves = int(input())
board = [['0' for i in range(n)] for j in range(m)]
for x in reds:
    a, b = x[0]-1, x[1]-1
    for i in range(m):
        for j in range(n):
            if i == a and j == b:
                board[i][j] = '1R'
                break
for x in blues:
    a, b = x[0]-1, x[1]-1
    for i in range(m):
        for j in range(n):
            if i == a and j == b:
                board[i][j] = '1B'
                break
print('Starting position:')
for i in board:
    print(*i)
print()
print("changing position:")
for x in range(moves):
    print("Move", x+1, sep=" ")
    if x % 2 == 0:
        for i in range(m):
            for j in range(n):
                if 'R' in board[i][j]:
                    if i > 0:
                        if 'R' in board[i-1][j]:
                            board[i - 1][j] = str(int(board[i-1][j][0]) + int(board[i][j][0])) + 'R'
                            board[i][j] = '0'
                        elif board[i-1][j] == '0':
                            board[i-1][j] = board[i][j][0]+'R'
                            board[i][j] = '0'
                        elif 'B' in board[i-1][j]:
                            board[i - 1][j] = str(int(board[i - 1][j][0]) + int(board[i][j][0])) + 'R'
                            board[i][j] = '0'
    else:
        for ii in range(m-1,-1,-1):
            for jj in range(n-1,-1,-1):
                if 'B' in board[ii][jj]:
                    if jj < n-1:
                        if 'B' in board[ii][jj+1]:
                            board[ii][jj+1] = str(int(board[ii][jj+1][0]) + int(board[ii][jj][0])) + 'B'
                            board[ii][jj] = '0'
                        elif board[ii][jj+1] == '0':
                            board[ii][jj+1] = board[ii][jj][0]+'B'
                            board[ii][jj] = '0'
                        elif 'R' in board[ii][jj+1]:
                            board[ii][jj+1] = str(int(board[ii][jj+1][0]) + int(board[ii][jj][0])) + 'R'
                            board[ii][jj] = '0'
    for iii in board:
        print(*iii)
    print()
print()
print("Final Answer:")
for i in board:
    print(*i)

"""
Test case 1:
8 8 
7
1 1
2 1
3 1 
4 1
8 1
4 4 
6 2 
6
5 1   
6 1
7 1 
5 2 
5 3 
4 5
5

Output:
4R 0 0 1R 0 0 0 0
0 0 0 0 0 0 0 0
0 3R 0 0 0 0 0 0
0 0 0 0 0 0 1B 0
2R 0 0 0 1B 0 0 0
0 0 1B 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Test case 2:
4 5 
6
4 1
3 2 
3 1
1 1 
2 1
3 5 
10 
2 2 
4 4
2 4
1 5 
2 5 
1 4
4 3 
4 5 
1 3
2 3
3 

Output:
3R 2R 0 1B 5R
1R 0 0 1B 0
0 0 0 0 0
0 0 0 1B 2B
"""
