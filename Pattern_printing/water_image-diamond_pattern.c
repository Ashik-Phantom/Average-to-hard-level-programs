//Water Image - Diamond Pattern

/*
The program must accept an integer N as the input. The program must print 2*N lines of output based on the following conditions.
- In the first line, the program must print N-1 asterisks without any space. 
  Then the program must print the integer 1.- In the second line, the program must print N-2 asterisks without any space. 
  Then the program must print the integers 2 and 3 separated by a space in reverse order.
- In the third line, the program must print N-3 asterisks without any space. 
  Then the program must print the integers 4, 5 and 6 separated by a space in reverse order.
- Similarly, the program must print the lines till the Nth line.- After printing the Nth line, 
  the program must print the exact water image of the first N lines as the output.
  
  Boundary Condition(s):2 <= N <= 100
  Input Format:
  The first line contains N.
  Output Format:
  The first 2*N lines containing the asterisks and integer value(s) based on the given conditions.
  
  Example Input/Output 1:
  Input:
  3
  Output:
  **1
  *3 2
  6 5 4
  6 5 4
  *3 2
  **1
  Explanation:
  Here N = 3, so the pattern contains 6 lines of output.The first 3 lines are given below.
  **1
  *3 2
  6 5 4
  After printing the first 3 lines, 
  the water image of the above 3 lines is printed.Hence the output is
  **1
  *3 2
  6 5 4
  6 5 4
  *3 2
  **1
  Example Input/Output 2:
  Input:4
  Output:
  ***1
  **3 2
  *6 5 4
  10 9 8 7
  10 9 8 7
  *6 5 4
  **3 2
  ***1 
  
  */ 
  
//Solution 
  

#include<stdio.h>
#include <stdlib.h>

int main()
{
    int N,i,j,k=0;
    scanf("%d",&N);
    for(i=0;i<N;i++)
    {
        for(j=0;j<N-1-i;j++)
        {
            printf("*");
        }
        for(j=N-1-i;j<N;j++)
        {
            k++;
        }
        int t = k;
        for(j=N-1-i;j<N;j++)
        {
            printf("%d ",t--);
        }
        printf("\n");
    }
    for(i=0;i<N;i++)
    {
        for(j=N-1;j>N-1-i;j--)
        {
            printf("*");
        }
        for(j=N-1-i;j>=0;j--)
        {
            printf("%d ",k--);
        }
        printf("\n");
    }
}
