/*
check is subset in a array forms the sum k, if yes print possible else not possible 
 ip: 3 34 4 12 5 2
      9 
 op: POSSIBLE
*/        


#include <stdio.h>
#include <stdlib.h>

int solve(int arr[],int k,int n)
{
    int mat[n+1][k+1],i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<=k;j++)
        {
            if(j==0) mat[i][j]=1;
            
            else if(i==0)
            {
                if(j==arr[i]) mat[i][j]=1;
                else mat[i][j]=0;
            }
            
            else
            {
                if(arr[i]<=j)
                {
                    if(mat[i-1][j]==1)
                    mat[i][j]=1;
                    else
                    mat[i][j]=mat[i-1][j-arr[i]];
                }
                else
                {
                    mat[i][j]=mat[i-1][j];
                }
            }
        }
    }
    printf("-----------------------\n");
    printf("| 0 1 2 3 4 5 6 7 8 9 |\n");
    printf("-----------------------\n");
    for(i=0;i<n;i++,printf("|\n"))
    {   printf("| ");
        for(j=0;j<=k;j++)
        {
            printf("%d ",mat[i][j]);
        }
    }
    printf("-----------------------\n");
  return mat[n][r];
}

int main()
{
    int arr[]={3,34,4,12,5,2};
    int n=6;
    int k=9;
    if(solve(arr,k,n)==1) printf("\nPOSSIBLE");
    else printf("\nNOT POSSIBLE");
}

