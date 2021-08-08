/* DP - Longest Common Substring Length

Two string values S1 and S2 are passed as the input to the program. The program must print the length of the longest common substring.

Boundary Condition(s):
1 <= Length of S1, S2 <= 10^4

Input Format:
The first line contains the value of S1.
The second line contains the value of S2.

Output Format:
The first line contains the integer value denoting the length of the longest common substring.

Example Input/Output 1:
Input:
abcde
cdefg

Output:
3

Explanation:
cde is the longest common substring whose length is 3.
*/
  
#include<stdio.h>
#include<stdlib.h>

int max(int a, int b)
{
    return a > b ? a : b;
}

int dp(char* s1,char* s2,int r,int c)
{
    int i,j;
    int mat[r+1][c+1];
    int result = 0;
    for(i=0;i<=r;i++)
    {
        for(j=0;j<=c;j++)
        {
            if(i==0 || j ==0)
                mat[i][j] = 0;
            else if(s1[i-1]==s2[j-1])
            {
                mat[i][j] = mat[i-1][j-1] + 1;
                result = max(result, mat[i][j]);
            }
            else
                mat[i][j] = 0;
        }
    }
    return result;
}
int main()
{
    int l1,l2,i,j;
    char s1[10000],s2[10000];
    scanf("%s\n",s1);
    scanf("%s",s2);
    for(l1=0;s1[l1];l1++);
    for(l2=0;s2[l2];l2++);
    printf("%d", dp(s1,s2,l1,l2));
}


/*
# longest substring 

#include<stdio.h>
#include<stdlib.h>

int max(int a, int b)
{
    return a > b ? a : b;
}

int dp(char* s1,char* s2,int r,int c)
{
    int i,j;
    int mat[r+1][c+1];
    for(i=0;i<=r;i++)
    {
        for(j=0;j<=c;j++)
        {
            if(i==0 || j ==0)
            {
                mat[i][j] = 0;
            }
            else if(s1[i-1]==s2[j-1])
            {
                mat[i][j] = mat[i-1][j-1] + 1;
            }
            else if(mat[i-1][j] >= mat[i][j-1])
            {
                mat[i][j]=mat[i-1][j];
            }
            else
            {
                mat[i][j]=mat[i][j-1];
            }
        }
    }
    return mat[r][c]+1;
}
int main()
{
    int l1,l2,i,j;
    char s1[10000],s2[10000];
    scanf("%s\n",s1);
    scanf("%s",s2);
    for(l1=0;s1[l1];l1++);
    for(l2=0;s2[l2];l2++);
    printf("%d", dp(s1,s2,l1,l2));
}
*/
