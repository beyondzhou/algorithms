from newarray2d import Array2D

# Implement a matrix
class MyMatrix:

    # init
    def __init__(self, nrows, ncols):
        self._theGrid = Array2D(nrows, ncols)
        self._theGrid.clear(0)

    # return the number of rows in the matrix

    def numRows(self):
        return self._theGrid.numRows()

    # return the number of columns in the matrix
    def numCols(self):
        return self._theGrid.numCols()

    # return the value stored in the given matrix element
    def __getitem__(self, ndxTuple):

        return self._theGrid[ndxTuple[0],ndxTuple[1]]

    # set the matrix element 
    def __setitem__(self, ndxTuple, scalar):

        self._theGrid[ndxTuple[0],ndxTuple[1]] = scalar

    # scalar value
    def scaleBy(self, scalar):

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                self._theGrid[row,col] *= scalar

    # transpose
    def transpose(self):
        
        theNewGrid = MyMatrix(self._theGrid.numCols(), self._theGrid.numRows())

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                theNewGrid[col,row] = self._theGrid[row, col]

        return theNewGrid

    # add
    def __add__(self, rhsMatrix):
    
        assert rhsMatrix.numRows() == self._theGrid.numRows() and \
           rhsMatrix.numCols() == self._theGrid.numCols(), \
            "Matrix sizes not compatible"
            
        theNewGrid = MyMatrix(self._theGrid.numRows(), self._theGrid.numCols())

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                theNewGrid[row,col] = self._theGrid[row,col] + rhsMatrix[row,col]

        return theNewGrid

    # sub
    def __sub__(self, rhsMatrix):

        assert rhsMatrix.numRows() == self._theGrid.numRows() and \
           rhsMatrix.numCols() == self._theGrid.numCols(), \
            "Matrix sizes not compatible"
                
        theNewGrid = MyMatrix(self._theGrid.numRows(), self._theGrid.numCols())

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                theNewGrid[row,col] = self._theGrid[row,col] - rhsMatrix[row,col]

        return theNewGrid

    # mul
    def __mul__(self, rhsMatrix):

        assert self._theGrid.numCols() == rhsMatrix.numRows(), \
            "Matrix sizes not compatible"
            
        theNewGrid = MyMatrix(self._theGrid.numRows(), rhsMatrix.numCols())
        
        for row in range(self._theGrid.numRows()):
            for col in range(rhsMatrix.numCols()):
                total = 0
                
                for mid in range(self._theGrid.numCols()):
                    total += self._theGrid[row,mid] * rhsMatrix[mid,col]

                theNewGrid[row,col] = total

        return theNewGrid
    
def test_matrix():
   
    # Import
    import random

    # set default value for matrix
    aMatrix = MyMatrix(2,3)
    bMatrix = MyMatrix(2,3)
    fMatrix = MyMatrix(3,2)

    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            aMatrix[i,j] = random.randint(1,2)
            bMatrix[i,j] = random.randint(1,2)

    for i in range(fMatrix.numRows()):
        for j in range(fMatrix.numCols()):
            fMatrix[i,j] = random.randint(1,2)
                     
    print 'The primary value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            print '%s ' % aMatrix[i,j], 
        print '\r'   

    print '\nThe primary value of bmatrix'
    for i in range(bMatrix.numRows()):
        for j in range(bMatrix.numCols()):
            print '%s ' % bMatrix[i,j], 
        print '\r'  
        
    print '\nThe primary value of fmatrix'
    for i in range(fMatrix.numRows()):
        for j in range(fMatrix.numCols()):
            print '%s ' % fMatrix[i,j], 
        print '\r'    

    # add amatrix and bmatrix to cmatrix
    cMatrix = aMatrix + bMatrix
    
    print '\nThe value of cMatrix (aMatrix + bMatrix)'
    for i in range(cMatrix.numRows()):
        for j in range(cMatrix.numCols()):
            print '%s ' % cMatrix[i,j], 
        print '\r'   

    # sub amatrix and bmatrix to dmatrix
    dMatrix = aMatrix - bMatrix
    
    print '\nThe value of dMatrix (aMatrix - bMatrix)'
    for i in range(dMatrix.numRows()):
        for j in range(dMatrix.numCols()):
            print '%s ' % dMatrix[i,j], 
        print '\r'   
   
    # Mul amatrix and fMatrix to ematrix
    eMatrix = aMatrix * fMatrix
    
    print '\nThe value of eMatrix (aMatrix * fMatrix)'
    for i in range(eMatrix.numRows()):
        for j in range(eMatrix.numCols()):
            print '%s ' % eMatrix[i,j], 
        print '\r'  
                          
    # Scale the amatrix by 3
    aMatrix.scaleBy(3)
    
    print '\nThe scale value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            print '%s ' % aMatrix[i,j], 
        print '\r'   
        
    # Transpose the amatrix 
    dMatrix = aMatrix.transpose()
    
    print '\nThe transpose value of amatrix'
    for i in range(dMatrix.numRows()):
        for j in range(dMatrix.numCols()):
            print '%s ' % dMatrix[i,j], 
        print '\r'   

if __name__ == "__main__":
    test_matrix()