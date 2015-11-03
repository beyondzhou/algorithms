class SparseMatrix:

    # init
    def __init__(self, row, col):
        self._nrows = row
        self._ncols = col
        self._theElements = list()

    # get the row
    def numRows(self):
        return self._nrows

    # get the col
    def numCols(self):
        return self._ncols

    # set the item
    def __setitem__(self, nTuple, scalar):
        ndx = self._findPosition(nTuple[0], nTuple[1])
        if ndx is not None:
            if scalar != 0.0:
                self._theElements[ndx].value = scalar
            else:
                self._theElements.pop(ndx)
        else:
            if scalar != 0.0:
                element = _MatrixElement(nTuple[0], nTuple[1], scalar) 
                self._theElements.append(element)   

    # get the item
    def __getitem__(self, nTuple):
        ndx = self._findPosition(nTuple[0], nTuple[1])
        assert ndx is not None, "item is not exists or its value is 0."
        return self._theElements[ndx].value

    # scale
    def scaleBy(self, scalar):
        for item in self._theElements:
            item.value *= scalar

    # add
    def __add__(self, rhsMatrix):

        assert self.numRows() == rhsMatrix.numRows() and \
               self.numCols() == rhsMatrix.numCols(), "matrix is not compitable!"

        # Create a new matrix
        newSparseMatrix = SparseMatrix(self.numRows(), self.numCols())

        for element in self._theElements:
            dupElement = _MatrixElement(element.row, element.col, element.value)
            newSparseMatrix._theElements.append(dupElement)

        for element in rhsMatrix._theElements:
            value = newSparseMatrix[element.row, element.col]
            value += element.value
            newSparseMatrix[element.row, element.col] = value

        return newSparseMatrix
    
    # sub
    def __sub__(self, rhsMatrix):

        assert self.numRows() == rhsMatrix.numRows() and \
               self.numCols() == rhsMatrix.numCols(), "matrix is not compitable!"

        # Create a new matrix
        newSparseMatrix = SparseMatrix(self.numRows(), self.numCols())

        for element in self._theElements:
            dupElement = _MatrixElement(element.row, element.col, element.value)
            newSparseMatrix._theElements.append(dupElement)

        for element in rhsMatrix._theElements:
            value = newSparseMatrix[element.row, element.col]
            value -= element.value
            newSparseMatrix[element.row, element.col] = value

        return newSparseMatrix
    

    def __mul__(self, rhsMatrix):

        assert self.numCols() == rhsMatrix.numRows(), "Matrix is not matching!"

        # Create a new matrix
        newSparseMatrix = SparseMatrix(self.numRows(), rhsMatrix.numCols())

        # Do the loop
        for row in range(self.numRows()):
            for col in range(rhsMatrix.numCols()):
                sum_ = 0
                for mid in range(self.numCols()):
                    ndxA = self._findPosition(row, mid)
                    ndxB = rhsMatrix._findPosition(mid, col)
                    if ndxA is not None and ndxB is not None:
                        sum_ += self[row, mid] * rhsMatrix[mid, col]
                element = _MatrixElement(row, col, sum_)
                newSparseMatrix._theElements.append(element)

        return newSparseMatrix

    # find position
    def _findPosition(self, row, col):
        n = len(self._theElements)
        for i in range(n):
            if self._theElements[i].row == row and \
               self._theElements[i].col == col:
                return i
        return None

# Storage class
class _MatrixElement:
    # init
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        
def test_matrix():
   
    # Import
    import random

    # set default value for matrix
    aMatrix = SparseMatrix(2,3)
    bMatrix = SparseMatrix(2,3)
    fMatrix = SparseMatrix(3,2)

    aMatrix[0,0] = random.randint(1,10)
    aMatrix[1,1] = random.randint(1,10)
    
    bMatrix[0,0] = random.randint(1,10)
    bMatrix[1,1] = random.randint(1,10)
    
    fMatrix[0,0] = random.randint(1,10)
    fMatrix[1,1] = random.randint(1,10)
                     
    print 'The primary value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            ndx = aMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % aMatrix[i,j], 
        print '\r'   

    print '\nThe primary value of bmatrix'
    for i in range(bMatrix.numRows()):
        for j in range(bMatrix.numCols()):
            ndx = bMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % bMatrix[i,j], 
        print '\r'  
        
    print '\nThe primary value of fmatrix'
    for i in range(fMatrix.numRows()):
        for j in range(fMatrix.numCols()):
            ndx = fMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % fMatrix[i,j], 
        print '\r'    

    # add amatrix and bmatrix to cmatrix
    cMatrix = aMatrix + bMatrix
    
    print '\nThe value of cMatrix (aMatrix + bMatrix)'
    for i in range(cMatrix.numRows()):
        for j in range(cMatrix.numCols()):
            ndx = cMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % cMatrix[i,j], 
        print '\r'   

    # sub amatrix and bmatrix to dmatrix
    dMatrix = aMatrix - bMatrix
    
    print '\nThe value of dMatrix (aMatrix - bMatrix)'
    for i in range(dMatrix.numRows()):
        for j in range(dMatrix.numCols()):
            ndx = dMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % dMatrix[i,j], 
        print '\r'   
   
    # Mul amatrix and fMatrix to ematrix
    eMatrix = aMatrix * fMatrix
    
    print '\nThe value of eMatrix (aMatrix * fMatrix)'
    for i in range(eMatrix.numRows()):
        for j in range(eMatrix.numCols()):
            ndx = eMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % eMatrix[i,j], 
        print '\r'  
                          
    # Scale the amatrix by 3
    aMatrix.scaleBy(3)
    
    print '\nThe scale value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            ndx = aMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % aMatrix[i,j], 
        print '\r'   
                
if __name__ == "__main__":
    test_matrix()