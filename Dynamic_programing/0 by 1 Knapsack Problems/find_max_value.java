/*
Given a knapsack with capacity C and two arrays w[] and val[] representing the weights and values of N distinct items, 
the task is to find the maximum value you can put into the knapsack.
Items cannot be broken and an item with weight X takes X capacity of the knapsack.
*/

import java.util.*;

import javax.lang.model.util.ElementScanner6;
public class knapsack
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = sc.nextInt();
        int wt[] = new int[N];
        int val[] = new int[N];
        int dp[][] = new int[N+1][C+1];
        for(int i=0;i<N;i++)
        {
            wt[i] = sc.nextInt();
        }
        for(int i=0;i<N;i++)
        {
            val[i] = sc.nextInt();
        }
        for(int i=0;i<=N;i++)
        {
            for(int j=0;j<=C;j++)
            {
                if(i==0 || j==0) dp[i][j] = 0;
                else if(wt[i-1]<=j)
                {
                    dp[i][j] = Math.max((dp[i-1][j-wt[i-1]]+val[i-1]),dp[i-1][j]);
                }
                else{
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        for(int i=0;i<=N;i++)
        {
            for(int j=0;j<=C;j++)
            {
                System.out.print(dp[i][j]+" ");
            }
            System.out.print("\n");
        }
    }
}
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
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
