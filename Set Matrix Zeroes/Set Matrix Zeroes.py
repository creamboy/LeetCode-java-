class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        if col==0 or row==0:
            return
        colhaszero=False
        rowhaszero=False
        for i in range(row):
            if matrix[i][0]==0:
                rowhaszero=True
                break
        for i in range(col):
            if matrix[0][i]==0:
                colhaszero=True
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if colhaszero:
            for i in range(col):
                matrix[0][i]=0
        if rowhaszero:
            for i in range(row):
                matrix[i][0]=0
                
