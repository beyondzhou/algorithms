from newarray import Array

class Array2D:
    # init
    def __init__(self, nrows, ncols):
        self._theRows = Array(nrows)

        for i in range(len(self._theRows)):
            self._theRows[i] = Array(ncols)

    # the number of rows
    def numRows(self):
        return len(self._theRows)

    # the number of cols
    def numCols(self):
        return len(self._theRows[0])

    # clear the array
    def clear(self, value):
        for i in range(self.numRows()):
            self._theRows[i].clear(value)

    # get the item
    def __getitem__(self, nTuple):
        assert len(nTuple) == 2, "The size of tuple should be 2."
        row = nTuple[0]
        col = nTuple[1]

        assert row >= 0 and row < self.numRows() and \
             col >= 0 and col < self.numCols(), "out of subscript"

        the1dArray = self._theRows[row]
        return the1dArray[col]

    # set the itme
    def __setitem__(self, nTuple, value):
        assert len(nTuple) == 2, "The size of tuple should be 2."
        row = nTuple[0]
        col = nTuple[1]

        assert row >= 0 and row < self.numRows() and \
             col >= 0 and col < self.numCols(), "out of subscript"

        the1dArray = self._theRows[row]
        the1dArray[col] = value
        
# Compute the average grade of exam
def avgGradeCompute():

    '''
    cat grade.txt

    7 
    3
    90 96 92
    85 91 89
    82 73 84
    69 82 86
    95 88 91
    78 64 84
    92 85 89

    '''

    # open the file
    gradeFile = open("grade.txt")

    # read the second line
    numStudents = int(gradeFile.readline())
    
    # read the first line
    numExams = int(gradeFile.readline())

    # init the array2d
    gradesArray = Array2D(numStudents, numExams)

    # read the grade
    i = 0
    for line in gradeFile:
        grades = line.split()
        for j in range(len(grades)):
            gradesArray[i,j] = grades[j]
        i += 1

    # close the file
    gradeFile.close()

    # compute the average grade
    for student in range(numStudents):
        total = 0.0
        for col in range(numExams):
            total += float(gradesArray[student,col])
        examAvg = total / numExams
        print "%2d:  %6.2f" % (student+1, examAvg)
        
if __name__ == '__main__':
    avgGradeCompute()