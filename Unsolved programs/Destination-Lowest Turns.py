"""
Destination - Lowest Turns (Id-13632)
There are R lanes and in each lane there are C junctions in which left or right turns may be allowed. 
A boy starts in his bicycle from a given junction whose lane and junction values are given. 
The boy must travel to a destination junction whose lane and junction values are given. 
The program must print the minimum number of turns the boy takes to travel from source to the destination. 
Due to maintenance work in some junctions, the left or right turns are not allowed. 
The junctions where maintenance work is happening are denoted by the value 0.
Boundary Condition(s):2 <= R, C <= 100
Input Format:
The first line contains R and C separated by a space.The next R lines each containing C values 1 or 0 separated by a space.
The (R+2)th line contains the source lane and junction values separated by a space.
The (R+3)th line contains the destination lane and junction values separated by a space.
Output Format:
The first line contains an integer representing the minimum number of turns the boy takes to travel from source to the destination.

Example Input/Output 1:
Input:
4 5
1 1 1 0 1
1 0 1 1 1
1 1 1 1 0
1 1 1 1 1
1 1
1 5
Output:
3
Explanation:The path where the boy must travel to travel from source to destination taking minimum number of turns is indicated as below.
P P P 0 P
1 0 P P P
1 1 1 1 0
1 1 1 1 1
Example Input/Output 2:
Input:
4 5
1 1 1 1 1
1 0 1 1 1
1 1 1 1 0
1 1 1 1 1
1 1
1 5
Output:
0
Explanation:
Here there is no need to take a turn.
P P P P P
1 0 1 1 1
1 1 1 1 0
1 1 1 1 1
Example Input/Output 3:
Input:
6 8
1 1 0 1 1 1 0 1
0 1 1 1 0 1 1 0
1 0 0 0 0 0 1 1
1 1 1 1 1 0 1 1
1 1 1 1 0 1 0 1
1 1 1 1 1 1 1 1
1 1
6 1
Output:
10
Example Input/Output 4:
Input:
6 8
1 1 0 1 1 1 0 1
0 1 1 1 0 1 1 0
1 0 0 1 0 0 1 1
1 1 1 1 1 0 1 1
1 1 1 1 0 1 0 1
1 1 1 1 1 1 1 1
1 1
6 1
Output:
4
"""

