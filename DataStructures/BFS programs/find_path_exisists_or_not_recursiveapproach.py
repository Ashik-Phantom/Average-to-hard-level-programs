

# Python3 program to find
# path between two cell in matrix
 
# Method for finding and printing
# whether the path exists or not
def isPath(matrix, n):
 
    # Defining visited array to keep
    # track of already visited indexes
    visited = [[False for x in range (n)]
                      for y in range (n)]
    
    # Flag to indicate whether the
    # path exists or not
    flag = False
 
    for i in range (n):
        for j in range (n):
           
            # If matrix[i][j] is source
            # and it is not visited
            if (matrix[i][j] == 1 and not
                visited[i][j]):
 
                # Starting from i, j and
                # then finding the path
                if (checkPath(matrix, i,
                              j, visited)):
                   
                    # If path exists
                    flag = True
                    break
    if (flag):
        print("YES")
    else:
        print("NO")
 
# Method for checking boundaries
def isSafe(i, j, matrix):
   
    if (i >= 0 and i < len(matrix) and
        j >= 0 and j < len(matrix[0])):
        return True
    return False
 
# Returns true if there is a
# path from a source(a
# cell with value 1) to a
# destination(a cell with
# value 2)
def checkPath(matrix, i, j,
              visited):
 
    # Checking the boundaries, walls and
    # whether the cell is unvisited
    if (isSafe(i, j, matrix) and
        matrix[i][j] != 0 and not
        visited[i][j]):
       
        # Make the cell visited
        visited[i][j] = True
 
        # If the cell is the required
        # destination then return true
        if (matrix[i][j] == 2):
           return True
 
        # traverse up
        up = checkPath(matrix, i - 1,
                       j, visited)
 
        # If path is found in up
        # direction return true
        if (up):
           return True
 
        # Traverse left
        left = checkPath(matrix, i,
                         j - 1, visited)
 
        # If path is found in left
        # direction return true
        if (left):
           return True
 
        # Traverse down
        down = checkPath(matrix, i + 1,
                         j, visited)
 
        # If path is found in down
        # direction return true
        if (down):
           return True
 
        # Traverse right
        right = checkPath(matrix, i,
                          j + 1, visited)
 
        # If path is found in right
        # direction return true
        if (right):
           return True
     
    # No path has been found
    return False
 
# Driver code
if __name__ == "__main__":
   
    matrix = [[0, 3, 0, 1],
              [3, 0, 3, 3],
              [2, 3, 3, 3],
              [0, 3, 3, 3]]
 
    # calling isPath method
    isPath(matrix, 4)
