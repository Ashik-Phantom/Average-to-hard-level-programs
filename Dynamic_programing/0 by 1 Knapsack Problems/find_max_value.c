#include <stdio.h>
int max(a,b)
{
    if(a>=b) return a;
    else return b;
}
int main() {
    int n,w,i,j;
    scanf("%d %d",&n,&w);
    int num[n],wt[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&num[i]);
    }
    for(i=0;i<n;i++)
    {
        scanf("%d",&wt[i]);
    }
    int r=n+1,c=w+1;
    int dp[r][c];
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            if(i==0 || j==0)
            {
                dp[i][j]=0;
            }
            else if(j>=num[i-1])
            {
                dp[i][j] = max(
                    dp[i-1][j-num[i-1]] + wt[i-1],
                    dp[i-1][j]
                    );
            }
            else
            {
                dp[i][j] = dp[i-1][j]; 
            }
        }
    }
    
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d ",dp[i][j]);
        }
        printf("\n");
    }
}

/*
4 8 
2 5 4 3
3 6 7 2
ans 10
6 9
3 1 5 8 4 2
10 8 19 15 20 16
ans 46
*/
