Minimum distinct number change count
"""
N integers are passed as the input to the program. A cost of 1 unit is involved to increase or decrease a given value by 1. 
The program must print the minimum cost involved to make the values distinct.
Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10000
Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
Output Format:
The first line contains the minimum cost involved to make the values distinct.
Example Input/Output 1:
Input:
11
54 35 35 72 58 56 55 80 55 49 57
Output:3
Explanation:
1 unit is involved in changing 35 to either 36 or 34.
2 units involved in changing one of the 55 to 53 (as changing 55 to 59 involves 4 units).
Now the values are distinct as below.
54 35 36 72 58 56 55 80 53 49 57
Hence total cost is 3.

Example Input/Output 2:
Input:
11
35 35 49 54 55 55 56 57 58 72 80
Output:3

Example Input/Output 3:
Input:
14
10 11 12 2 3 5 7 7 8 9 13 14 15 5
Output:
2
Explanation:
One of the 5s is changed to 4 with a cost 1.
One of the 7s is changed to 6 with a cost 1.
Hence total minimum cost needed is 2.
"""
