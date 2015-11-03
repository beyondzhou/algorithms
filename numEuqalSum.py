# Find the two numbers whose sum is the other number
def findTwoNum(theSeq, theSum):

    quickSort(theSeq)
    print theSeq
    recFindTwoNum(theSeq, theSum)
   
# quickSort
def quickSort(theSeq):

    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)

def recQuickSort(theSeq, first, last):

    if first > last:
        return
    else:
        pos = partitionSeq(theSeq, first,  last)
        recQuickSort(theSeq, first, pos-1)
        recQuickSort(theSeq, pos+1, last)

def partitionSeq(theSeq, first, last):

    pivot = theSeq[last]
    i = first - 1
    for j in range(first, last):
    
        if theSeq[j] < pivot:
            i = i + 1
            theSeq[i], theSeq[j] = theSeq[j], theSeq[i]

    theSeq[i+1], theSeq[last] = theSeq[last], theSeq[i+1]

    return i+1

# rec find two number
def recFindTwoNum(theSeq, theSum):

    first = 0
    last = len(theSeq)-1
    while first < last:
        theTotal = theSeq[first] + theSeq[last]
        if theTotal == theSum:
            print '%s and %s is equal to %s' % (theSeq[first], theSeq[last], theSum)
            first += 1
            last -= 1
        elif theTotal < theSum:
            first += 1
        elif theTotal > theSum:
            last -= 1

if __name__ == "__main__":
    theSeq = [1, 5, 9, 3, -1, 4, 6, -2, 3, 4, -8]
    findTwoNum(theSeq, 8)