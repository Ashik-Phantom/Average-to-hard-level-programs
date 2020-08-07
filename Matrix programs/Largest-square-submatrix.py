#This program finds the target elemnet in the given matrix 
#and checks the possible Largest square sub-matrix that can be formed with the target element in the center of the submatrix matrix and prints it 

row,column=map(int,input().split())
matrix=[list(map(int,input().split())) for i in range(row)]
target=int(input())
row_right,row_left,column_up,column_down=0,0,0,0
maximum=0
position_row,position_column=0,0
for i in range(row):
	for j in range(column):
		#first we have to find the position of the target element and then find the adjacent cell
		if matrix[i][j]==target:
			row_right=i
			column_up=j
			row_left=row-i-1
			column_down=column-j-1
			#find the minimum from the adjacent cells we got, so as to determine the dimension of the required submatrix 
			minimum=min(row_right,row_left,column_up,column_down) 
			#now check the maximum sub matrix and find the position of the middle element ie the target element
			if minimum>=maximum:
				maximum=minimum 
				position_row,position_column=i,j 
#now calculate the range from position i of middle element minus the maximum dimention to the position j of middle element plus the maximum dimension
#and print the value at that position 
for i in range(position_row-maximum,position_row+maximum+1):
	for j in range(position_column-maximum,position_column+maximum+1): 
		print(matrix[i][j],end=" ") 
	print()
 
#code by @Ashik-Phantom

#test case 1 
#7 9 
#43 85 91 83 26 30 70 11 95
#34 72 22 19 99 79 50 90 88 
#80 63 51 57 64 36 38 12 25
#37 67 13 53 32 81 59 48 92
#62 20 74 17 96 44 52 33 98
#86 16 29 58 42 66 24 61 46
#68 97 40 87 28 41 65 27 55
#52 

#Output
#64 36 38 12 25
#32 81 59 48 92
#96 44 52 33 98
#42 66 24 61 46
#28 41 65 27 55
