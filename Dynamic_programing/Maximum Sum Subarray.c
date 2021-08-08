 /*
 DP - Maximum Sum Subarray
 
An array of N integers (both positive and negative) is given as the input to the program. The program must print the maximum sum of the subarray in the given array as the output.

Boundary Condition(s):
1 <= N <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by space.

Output Format:
The first line contains the maximum subarray sum.

Example Input/Output 1:
Input:
7
2 1 -6 4 -2 8 -2

Output:
10

Explanation:
The subarray 4 -2 8 has the maximum sum 10.

Example Input/Output 2:
Input:
10
73 64 18 -18 44 -4 -17 -28 -59 54

Output:
181
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int max(int a,int b)
{
    return a > b ? a: b;
}

int dp(int arr[], int n)
{
    int local_max = 0;
    int global_max = -INFINITY;
    for(int i=0;i<n;i++)
    {
        local_max = max(arr[i], arr[i]+local_max);
        if(local_max > global_max)
        {
            global_max = local_max;
        }
    }
    return global_max;
}
int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;scanf("%d",&arr[i++]));
    printf("%d", dp(arr,n));
}
