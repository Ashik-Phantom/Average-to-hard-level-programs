#Rain Drop Lights Pattern
"""The program must accept an integer matrix of size R*C representing the state of rain drop lights and an integer T as the input. 
Each column in the matrix represents a rain drop and it contains the integers from 0 to R-1 representing the brightness of lights. 
The lights in each column change their state after a delay of X seconds (i.e., the brightness of the lights in a column shifted down by a position after a delay of X seconds). 
The delay(in seconds) for each column is passed as the input. The program must print the state of the rain drop lights after T seconds as the output.

Boundary Condition(s):
2 <= R, C <= 50
1 <= T <= 100
1 <= Delay time for each column <= 50
Input Format:The first line contains R, C and T separated by a space.The next R lines, each contains C integer values separated by a space.
The (R+2)th line contains C integer values representing the delay time for C columns.Output Format:The first R lines, 
each contains C integers values representing the state of the rain drop lights after T seconds. 

Example Input/Output 1:
Input:
5 7 4
0 3 2 0 3 2 0
1 4 3 1 4 3 1
2 0 4 2 0 4 2
3 1 0 3 1 0 3
4 2 1 4 2 1 4
2 1 1 3 1 1 2
Output:
3 4 3 4 4 3 3
4 0 4 0 0 4 4
0 1 0 1 1 0 0
1 2 1 2 2 1 1
2 3 2 3 3 2 2

Explanation:
Here T = 4.1st and 7th columns: Delay = 2 seconds. So the lights in the columns 1 and 7 change their state every 2 seconds.
2nd, 3rd, 5th and 6th columns: Delay = 1 second. So the lights in the columns 2, 3, 5 and 6 change their state every second.
4th column: Delay = 3 seconds. So the lights in the column 4 change their state every 3 seconds.
After 4 seconds, the state of the rain drop lights becomes
3 4 3 4 4 3 3
4 0 4 0 0 4 4
0 1 0 1 1 0 0
1 2 1 2 2 1 1
2 3 2 3 3 2 2

Example Input/Output 2:
Input:
7 6 15
4 1 5 3 2 0
5 2 6 4 3 1
6 3 0 5 4 2
0 4 1 6 5 3
1 5 2 0 6 4
2 6 3 1 0 5
3 0 4 2 1 6
4 1 6 2 3 5
Output:
1 0 3 3 4 4
2 1 4 4 5 5
3 2 5 5 6 6
4 3 6 6 0 0
5 4 0 0 1 1
6 5 1 1 2 2
"""




def fun(col, s, t): 
    for i in range(1, t+1): 
        if i%s==0: 
            temp = l[r-1][col] 
            for j in range(r): 
                temp,l[j][col] = l[j][col],temp
            
            
r,c,t=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(r)]
d=list(map(int,input().split())) 
for i in range(c): 
    fun(i,d[i],t)
for i in l:
    print(*i)
