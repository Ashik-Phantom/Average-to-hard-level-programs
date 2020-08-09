/*The size of the chessboard is given as (r,c) and rook is placed at (x,y) and a pawn is placed at (a,b). The program is to find the number possible movement of the rook. 
The movement of the rook is stopped when it reaches the end of the board or it encounters a pawn (pawn's position)

input:
r c 
x y 
a b 
 
output 
count of movements 

Testcase 1:
input:
8 8 
6 5 
2 5 
Output:

Explaination:

. . . . . . . .
. . . . P . . .
. . . . * . . .
. . . . * . . .
. . . . * . . .
* * * * R * * *
. . . . * . . .
. . . . * . . .
*/
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int R,C,rookRow,rookCol,pawnRow,pawnCol;
    scanf("%d %d\n%d %d\n%d %d",&R,&C,&rookRow,&rookCol,&pawnRow,&pawnCol);
    int totalMoves=R+C-2;
    if(rookRow==pawnRow){
        if(pawnCol<rookCol){
            totalMoves-=(pawnCol+1);
        }
        else
        {
            totalMoves-=(C-pawnCol);
        }
    }
    else if(rookCol==pawnCol){
        if(pawnRow<rookRow){
            totalMoves-=(pawnRow+1);
        }
        else
        {
            totalMoves-=(R-pawnRow);
        }
    }
    printf("%d",totalMoves);
}
