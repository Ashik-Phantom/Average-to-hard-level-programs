
/*
Enclose Character Matrix
The program must accept a character matrix of size R*C and an integer K as the input. The values of R and C are always divisible by K. The program must enclose the given character matrix within sub matrices of size K*K.
- The sub matrices in the border must be filled with 1s and 0s alternatively in clockwise direction. The first sub matrix in the top left will be filled with 1s.
Boundary Condition(s):
2 <= R, C <= 50
2 <= K <= Minimum value between R and C
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The (R+2)nd line contains K.
Output Format:
The first (2*K)+R lines, each contains (2*K)+C characters separated by a space.
Example Input/Output 1:
Input:
9 6
h R W G v P
z n N L A Q
Y u q z j r
z O k w y V
D z D g x i
u e S R s t
I e p A M e
m c u a h I
q V X Z p W
3
Output:
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0
0 0 0 h R W G v P 1 1 1
0 0 0 z n N L A Q 1 1 1
0 0 0 Y u q z j r 1 1 1
1 1 1 z O k w y V 0 0 0
1 1 1 D z D g x i 0 0 0
1 1 1 u e S R s t 0 0 0
0 0 0 I e p A M e 1 1 1
0 0 0 m c u a h I 1 1 1
0 0 0 q V X Z p W 1 1 1
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 0 0 0 1 1 1 0 0 0
Explanation:
Here R = 9, C = 6 and K = 3.
The given 9*6 character matrix is enclosed within square matrices of size 3*3.
The square matrices in the border are filled with 1s and 0s alternatively in clockwise direction.
Example Input/Output 2:
Input:
6 6
h R W G v P
z n N L A Q
Y u q z j r
z O k w y V
D z D g x i
u e S R s t
2
Output:
1 1 0 0 1 1 0 0 1 1
1 1 0 0 1 1 0 0 1 1
0 0 h R W G v P 0 0
0 0 z n N L A Q 0 0
1 1 Y u q z j r 1 1
1 1 z O k w y V 1 1
0 0 D z D g x i 0 0
0 0 u e S R s t 0 0
1 1 0 0 1 1 0 0 1 1
1 1 0 0 1 1 0 0 1 1
Example Input/Output 3:
Input:
4 6
a Y y F d s
s o c A c n
O V n v i L
p G s v C T
2
Output:
1 1 0 0 1 1 0 0 1 1
1 1 0 0 1 1 0 0 1 1
0 0 a Y y F d s 0 0
0 0 s o c A c n 0 0
1 1 O V n v i L 1 1
1 1 p G s v C T 1 1
0 0 1 1 0 0 1 1 0 0
0 0 1 1 0 0 1 1 0 0
Example Input/Output 4:
Input:
4 8
a Y y F d s m p
s o c A c n d f
O V n v i L o e
p G s v C T r j
2
Output:
1 1 0 0 1 1 0 0 1 1 0 0
1 1 0 0 1 1 0 0 1 1 0 0
0 0 a Y y F d s m p 1 1
0 0 s o c A c n d f 1 1
1 1 O V n v i L o e 0 0
1 1 p G s v C T r j 0 0
0 0 1 1 0 0 1 1 0 0 1 1
0 0 1 1 0 0 1 1 0 0 1 1
*/


#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int r, c; 
    cin>>r>>c; 
    char arr[r][c];
    for(int i = 0 ;i < r;i++){
        for(int j = 0 ;j < c;j ++)
            cin>>arr[i][j];
    }
    int k ; cin>>k;
    int L = k, U = c+k-1;
    for(int i = 0 ;i < 2*k+r;i++){
        for(int j = 0 ;j < 2*k +c ;j++){
            char ch = '1'-(((i/k)&1)^((j/k)&1));
            if(i<L || i>=r+k || j<L || j>U)
                cout<<ch<<" ";
            else
                cout<<arr[i-k][j-k]<<" ";
        }
        cout<<endl;
    }

}

