'''
cat student.txt

10015
John
Smith
2
3.01
10334
Jane
Roberts
4
3.81
'''
FILENAME = 'students.txt'

# Student File reader
class StudentFileReader:

    # Init
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None

    # Open
    def open(self):
        self._inputFile = open(self._inputSrc)

    # Close
    def close(self):
        self._inputFile.close()
        self._inputFile = None

    # Fetch record
    def fetchRecord(self):
        line = self._inputFile.readline()
        if line == "":
            return None
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student

    # Fetch all
    def fetchAll(self):
        theRecords = list()
        theRecord = self.fetchRecord()
        while theRecord is not None:
            theRecords.append(theRecord)
            theRecord = self.fetchRecord()

        return theRecords

# Student Record storage class
class StudentRecord:
    # Init
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0

# Prints the student report
def printReport(theList):
    # The class names associated with the class codes
    classNames = (None, "Freshman", "Sophomore", "Junior", "Senior")

    # print the header
    print "LIST OF STUDENTS".center(50)
    print ""
    print "%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA')
    print "%5s %25s %10s %4s" % ('-'*5, '-'*25, '-'*10, '-'*4)
    # Print the body
    for record in theList:
        print "%5d %-25s %10s %4.2f" % (record.idNum,\
                         record.lastName +', ' + record.firstName, \
                         classNames[record.classCode], record.gpa)

    # Add a footer
    print "-" * 50
    print "Number of students:", len(theList)

# Main
def main():
    reader = StudentFileReader(FILENAME)
    reader.open()
    studentList = reader.fetchAll()
    reader.close()

    # Sort the list by id number
    studentList.sort(key = lambda rec: rec.idNum)

    # Print the student report
    printReport(studentList)

if __name__ == '__main__':
    main()
    
'''
                 LIST OF STUDENTS                 

ID    NAME                      CLASS      GPA 
----- ------------------------- ---------- ----
10015 Smith, John                Sophomore 3.01
10334 Roberts, Jane                 Senior 3.81
--------------------------------------------------
Number of students: 2
'''