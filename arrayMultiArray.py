from newarray import Array

class MultiArray:
    # init
    def __init__(self, *dims):

        assert len(dims) > 1, "Multi array should at least 2 dimension!"
        self._dims = dims
        
        size = 1
        for i in self._dims:
            assert i > 0, "Dimension should be above than 0!"
            size *= i

        self._elements = Array(size)

        self._factors = Array(len(self._dims))
        self._computeFactor()

    # get the dims
    def numDims(self):
        return len(self._dims)

    # get the length 
    def length(self, dim):
        return self._dims[dim-1]

    # get the item
    def __getitem__(self, nTuple):
        assert len(nTuple) == self.numDims(), "Invalid subscript!"
        ndx = self._computeIndex(nTuple)
        return self._elements[ndx]

    # set the item
    def __setitem__(self, nTuple, value):
        assert len(nTuple) == self.numDims(), "Invalid subscript!"
        ndx = self._computeIndex(nTuple)
        self._elements[ndx] = value

    # clear
    def clear(self, value):
        self._elements.clear(value)

    # compute the index
    def _computeIndex(self, nTuple):
        offset = 0
        for i in range(len(nTuple)):
            if nTuple[i] < 0 or nTuple[i] >= self._dims[i]:
                return None
            else:
                offset += nTuple[i] * self._factors[i]
        return offset

    # compute the factor
    def _computeFactor(self):
        for i in range(len(self._factors)):
            total = 1
            for j in range(i+1, len(self._factors)):
                total *= self._dims[j]
            self._factors[i] = total
       
# test function     
def test_mdarray():

    # Open the text file for reading
    gradeFile = open(r'c:\temp\grade.txt', 'r')
    
    # Extract the first two values which indicate the size of the array
    numStudents = int(gradeFile.readline())
    numExams = int(gradeFile.readline())
    
    # Create the 2D array to store the grades
    examGrades = MultiArray(numStudents, numExams)
    
    # Extract the grades from the remaining lines
    records = gradeFile.readlines()
    
    i = 0
    for student in records:
        grades = student.split()
        for j in range(numExams):
            examGrades[i,j] = int(grades[j])
        i += 1
    # close the text file
    gradeFile.close()
    
    # compute each student's aveerage exam grade
    for i in range(numStudents):
        # Tally the exam grades for the ith student
        total = 0
        for j in range(numExams):
            total += examGrades[i,j]
    
        # Compute average for the ith student
        examAvg = total / float(numExams)
        print "%2d: %6.2f" % (i+1, examAvg)
        
if __name__ == "__main__":
    test_mdarray()