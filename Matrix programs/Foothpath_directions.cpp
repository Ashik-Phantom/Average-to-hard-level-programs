// Footpath - Four Directions
/*
The program must accept four integers N, W, S and E representing the number of steps in the directions North, West, South and East respectively. 
A person is standing in a position, and he moves N steps towards the north, then he moves W steps towards the west, 
then he moves S steps towards the south and E steps towards the east. The program must print the output based on the following conditions.
- Initially, the person moves N steps towards the north, so the program prints "N" N times towards the north.
- Then the person moves W steps towards the west, so the program prints "W" W times towards the west.
- Then the person moves S steps towards the south, so the program prints "S" S times towards the south.
- Then the person moves E steps towards the east, so the program prints "E" E times towards the east.
The person stops moving when he crosses his path or there are no moves in the east. 
The program must print the hyphens instead of empty places to make the person's footpath more clear.
Boundary Condition(s):1 <= N, W, S, E <= 100Input Format:The first line contains N, W, S and E separated by a space.Output Format:The lines containing the characters as per the given conditions.

Example Input/Output 1:
Input:
5 7 6 5
Output:
WWWWWWWN
S------N
S------N
S------N
S------N
S-------
SEEEEE--

Explanation:
Here N = 5, W = 7, S = 6 and E = 5.
Initially, the person moves 5 steps towards the north (N).
Then the person moves 7 steps towards the west (W).
Then the person moves 6 steps towards the south (S).
Then the person moves 5 steps towards the east (E).
Then the empty places are filled with hyphens.
Hence the output

Example Input/Output 2:
Input:
4 3 3 3
Output:
WWWN
S--N
S--N
SEEE

Example Input/Output 3:
Input:
6 6 6 10
Output:
WWWWWWN----
S-----N----
S-----N----
S-----N----
S-----N----
S-----N----
SEEEEEEEEEE
Example Input/Output 4:
Input:10 5 4 8
Output:
WWWWWN
S----N
S----N
S----N
SEEEEE
-----N
-----N
-----N
-----N
-----N
*/


#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv){
    int n ,w,s,e;
    cin>>n >> w>>s>>e ;
    if (s<n)
        e = min(w,e);
    char arr[max(n,s+1)] [max(e,w)+1] ;
    int r = max(n,s+1);
    int c = max(e,w)+1;
    for(int i = 0 ; i < r ;  ++i){
        for(int j = 0 ;j< c; j ++){
            arr[i][j] = '-';
        }
    }
    for(int i = 0 ;i < n;i++){
        arr[i][w] = 'N';
    }
    for(int i = 0 ;i < w ; i++)
        arr[0] [i] = 'W';
    for(int i = 1 ;i <= s ; i++)
        arr[i][0] = 'S';
    for(int i =1 ; i <= e ; i++)
        arr[s][i] = 'E';
    for(int i = 0 ;i < r; i ++){
        for(int j = 0 ;j < c ; j++)
            cout<< arr[i][j] ; 
        cout<< endl ; 
    }

}
