/*
check is subset in a array forms the sum k, if yes print possible else not possible 
 ip: 3 34 4 12 5 2
      9 
 op: POSSIBLE
*/    

import java.util.*;

import javax.lang.model.util.ElementScanner6;
public class Main
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int arr[] = new int[N];
        for(int i=0;i<N;i++)
        {
            arr[i] = sc.nextInt();
        }
        int K = sc.nextInt();
        boolean dp[][] = new boolean[N][K+1];
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<=K;j++)
            {
                if(j==0)
                {
                    dp[i][j] = true;
                }
                else if(i==0)
                {
                    if(arr[i]==j) dp[i][j]=true;
                    else dp[i][j]=false;
                }
                else
                {
                    if(arr[i]<=j)
                    {
                        dp[i][j] = dp[i-1][j] || dp[i-1][j-arr[i]];
                    }
                    else{
                        dp[i][j] = dp[i-1][j];
                    }
                }
            }
        }

        for(int i=0;i<N;i++)
        {
            for(int j=0;j<=K;j++)
            {
                System.out.print(dp[i][j]+" ");
            }
            System.out.print("\n");
        }
    }
}

