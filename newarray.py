import ctypes

class Array:
    # Init
    def __init__(self, size):
        assert size > 0, "size should be above than 0"

        PyObjects = ctypes.py_object * size
        self.slots = PyObjects()
        self.size = size
        self.clear(None)

    # Len
    def __len__(self):
        return self.size

    # Get item
    def __getitem__(self, index):
        assert index >= 0 and index < self.size, "index must be within the valid range."

        return self.slots[index]

    # Set item
    def __setitem__(self, index, value):
        assert index >= 0 and index < self.size, "index must be within the valid range."

        self.slots[index] = value

    # Clear
    def clear(self, value):
        for i in range(self.size):
            self.slots[i] = value

    # Iterator
    def __iter__(self):
        return ArrayIterator(self.slots)

class ArrayIterator:
    # Init
    def __init__(self, slots):
        self.slots = slots
        self.index = 0
    # Iter
    def __iter__(self):
        return self
    # Next
    def next(self):
        if self.index < len(self.slots):
            item = self.slots[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
        
# example
# Fill a 1D array with random values, then print them, one per line
def printRandomValue():
    import random

    # create the array
    valueList = Array(100)

    # set the value
    for i in range(len(valueList)):
        valueList[i] = random.random()

    # print the value
    for value in valueList:
        print value

# Count the number of occurrences of each letter in a text file
def letterNumCount():

    """letters.txt
    Python is a scripting language built using the C language, a high-level language
    that requires a program's source code be compiled into executable code before it can
    be used.
    """
    
    numArray = Array(127)
    numArray.clear(0)
    
    fobj = open("letters.txt")
    for line in fobj:
        for letter in line:
            code = ord(letter) 
            numArray[code] += 1
    fobj.close()

    # Print the results
    for i in range(26):
        print "%c - %4d %c - %4d" % \
            (chr(65+i), numArray[65+i], chr(97+i), numArray[97+i])   
            
if __name__ == "__main__":
    printRandomValue()
    print ""
    letterNumCount()  