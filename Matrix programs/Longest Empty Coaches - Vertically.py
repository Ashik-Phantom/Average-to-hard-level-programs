# Longest Empty Coaches - Vertically
"""
A train consists of R*C coaches. The train is standing on a railway platform which is designed in a vertical zig-zag fashion. The program must accept an integer matrix of size R*C containing only 1's and 0's representing coaches of the train. The top-left cell of the matrix represents the one of the ends of the train. The integer 1 indicates that the coach is full and 0 indicates that the coach is empty. The program must print the length of the longest empty coaches in the train.Boundary Condition(s):2 <= R, C <= 100Input Format:The first line contains R and C separated by a space.The next R lines, each contains C integers separated by a space.Output Format:The first line contains the length of the longest empty coaches in the train .Example Input/Output 1:Input:10 71 1 1 1 1 0 00 0 0 1 1 1 11 1 1 0 1 1 01 1 0 1 1 0 10 0 0 0 0 0 01 0 1 1 0 1 00 0 1 0 1 1 11 0 0 0 0 0 01 1 0 1 0 0 01 1 0 1 0 0 1Output:6Explanation:The longest empty coaches in the train are highlighted below.1 1 1 1 1 0 00 0 0 1 1 1 11 1 1 0 1 1 01 1 0 1 1 0 10 0 0 0 0 0 01 0 1 1 0 1 00 0 1 0 1 1 11 0 0 0 0 0 01 1 0 1 0 0 01 1 0 1 0 0 1Here the length is 6 which is printed as the output.Example Input/Output 2:Input:5 60 0 0 1 0 11 0 0 1 0 11 0 0 0 0 10 0 0 1 0 10 0 1 1 1 0Output:11
"""

R , C = list( map( int , input().split() ) )
Train = []
for i in range(R):
    Train.append( input().split() )
Train_Linear = []
Down = True
for Col in range(C):
    for Row in range(R):
        if(Down):
            Train_Linear.append( Train[Row][Col] )
        else:
            Train_Linear.append( Train[R-1-Row][Col] )
    Down = not Down
print( max( [ len(val) for val in ''.join(Train_Linear).split('1') ] ) )
