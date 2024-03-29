"""
Remove Parallel Edges - Directed Graph
There are N nodes in a directed graph. The program must accept the adjacency matrix of the directed graph as the input. If there are two edges between the two nodes, then the edges are called as parallel edges. The program must remove the parallel edges(i.e., remove the edge with maximum weight) in the graph. Then the program must print the revised adjacency matrix of the graph as the output.

Note:
- The value 0 in the matrix indicates that there is no edge between the two nodes.
- The weigths of the parallel edges are always not equal.

Boundary Condition(s):
2 <= N <= 50
0 <= Matrix element value <= 1000

Input Format:
The first line contains N.
The next N lines, each contains N integer values separated by a space.

Output Format:
The first N lines contain the revised adjacency matrix of the graph.

Example Input/Output 1:
Input:
5
0 2 0 0 0
4 0 3 0 0
0 0 0 0 9
0 5 0 0 6
0 0 0 3 0

Output:
0 2 0 0 0
0 0 3 0 0
0 0 0 0 9
0 5 0 0 0
0 0 0 3 0

Explanation:
There are 5 nodes in the directed graph.
The parallel edges present between the nodes 1 and 2.
1 -> 2 = 2
2 -> 1 = 4
Similarly, the parallel edges present between the nodes 4 and 5.
4 -> 5 = 6
5 -> 4 = 3
After removing the edges with the maximum weight, the adjacency matrix becomes
0 2 0 0 0
0 0 3 0 0
0 0 0 0 9
0 5 0 0 0
0 0 0 3 0

Example Input/Output 2:
Input:
6
0 9 6 0 3 0
0 0 3 0 8 7
4 8 0 9 0 3
0 6 2 0 1 0
6 1 0 4 0 5
8 4 5 0 0 0

Output:
0 9 0 0 3 0
0 0 3 0 0 0
4 0 0 0 0 3
0 6 2 0 1 0
0 1 0 0 0 5
8 4 0 0 0 0 
"""

n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if l[i][j]!=0 and l[j][i]!=0:
            if l[i][j]>l[j][i]:
                l[i][j]=0
            else:
                l[j][i]=0
for i in l:
    print(*i)
    
