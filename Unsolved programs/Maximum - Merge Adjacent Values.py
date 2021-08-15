"""
Maximum - Merge Adjacent Values
The program must accept N integers. An odd value can be merged with an adjacent odd value. 
Similarly an even value can be merged with an adjacent even value. 
This process is repeated till there are no adjacent odd or even values. 
The program must print the maximum possible value M among the final remaining integer values.
Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 10^5
Input Format:
The first line contains N.The second line contains N integers separated by a space.
Output Format:
The first line contains M.
Example Input/Output 1:
Input:
5
12 11 5 60 9
Output:
88
Explanation:
11 and 5 are merged to form 16. Now the values are 12 16 60 9.
Now 16 can be merged with either 12 or 60. Let us assume it is 12.
The values are 28 60 9.Now 28 and 60 are merged. 
The final values are 88 9. The largest is 88.

Example Input/Output 2:
Input:
7
12 5 61 9 20 10 4
Output:
104
Explanation:
61 and 9 merged so that the values are 12 5 70 20 10 4.
Now 70 and 20 are merged to form 12 5 90 10 4.
Now 90 and 10 are merged to form 12 5 100 4.
Finally 100 and 4 are merged to form 12 5 104. 
The largest is 104.
"""
