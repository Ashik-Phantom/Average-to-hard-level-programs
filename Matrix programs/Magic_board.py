# Magical Board Game

"""
In a magical board, there are R red coins and B black coins. There are two magnets on the board that pull the coins towards them. One magnet is present at the top of the board 
that will pull only red coins column wise. The other magnet is present in the right side of the board that will pull only black coins row wise. 
Only one magnet can pull coins at a time. At any point of time, the coin cannot move outside the board. if there is no coin in the next cell when moving towards up or right, 
then the coins can move without any change. But if there are X coins in the next cell, the coins will change the color based on the following conditions.
- If X is greater than the number of coins to be added (i.e if X is greated than the number of coins in the current cell), then all coins will be the same color as in the 
next cell.
-  If X is less than the number of coins to be added, then all coins will be the same color as in the current cell.
- If X is equal to the number of coins to be added, then compare the color in the current cell and the next cell, if both are same then the coins can move without 
any change in color. Else all the coins will become red color. So both red and black coins can not be present in the same cell. Every second, all the coins move towards 
up or right simultaneously by exactly 1 cell. The program must accept the size of the board MxN and the positions of the R red coins, B black coins as the input. 
The program must print the number of coins in each cell and its color (R or B) after T seconds as the output.
Note: The magnet on the top of the board always starts to pull first.

Boundary Condition(s):
2 <= M, N <= 20 
1 <= R+B <=M*N
1 <= T <= 50

Input Format:
The first line contains M and N separated by a space.
The second line contains R.
The next R lines from the 3rd line, each containing two integers representing the positions of a red coin.
The (R+3)rd line contains B.
The next B lines from the (R+4)th line, each containing two integers representing the positions of a B black coins.
The (R+B+4)th line contains T.

Output Format:
The first M lines containing the number of coins in each cell and its color (R or B) after T seconds.

Test case 1:
Input:
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
Input:
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

# Solution ( 50% correct)
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
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if 'B' in board[i][j]:
                    if j < n-1:
                        if 'B' in board[i][j+1]:
                            board[i][j+1] = str(int(board[i][j+1][0]) + int(board[i][j][0])) + 'B'
                            board[i][j] = '0'
                        elif board[i][j+1] == '0':
                            board[i][j+1] = board[i][j][0]+'B'
                            board[i][j] = '0'
                        elif 'R' in board[i][j+1]:
                            board[i][j+1] = str(int(board[i][j+1][0]) + int(board[i][j][0])) + 'R'
                            board[i][j] = '0'
    for i in board:
        print(*i)
    print()
print()
print("Final Answer:")
for i in board:
    print(*i)
