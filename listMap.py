class MyMap:
    # init
    def __init__(self):
        self._entryList = list()

    # length
    def __len__(self):
        return len(self._entryList)

    # Contain
    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    # Add
    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    # Remove
    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "key is not in the map."
        self._entryList.pop(ndx)

    # valueOf
    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "key is not in the map."
        return self._entryList[ndx].value

    # find position
    def _findPosition(self, key):

        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None

    # iter
    def __iter__(self):
        return _MapIterator(self._entryList)

# Map storage
class _MapEntry:
    # init
    def __init__(self, key, value):
        self.key = key
        self.value = value

# Map Iterator
class _MapIterator:
    # init
    def __init__(self, entryList):
        self._entryList = entryList
        self._ndx = 0
    def __iter__(self):
        return self
    def next(self):
        if self._ndx < len(self._entryList):
            entry = self._entryList[self._ndx].key
            self._ndx += 1
            return entry
        else:
            raise StopIteration

# Test Map Function
def testMyMap():

    # init
    mapEntryList = MyMap()
    
    # Add some key,value pair
    mapEntryList.add('tim', 100)
    mapEntryList.add('dog', 10)
    mapEntryList.add('cat', 1)

    # Print the length
    print len(mapEntryList)

    # Print all the item
    for i in mapEntryList:
        print i,
    print ''

    # In check
    print 'dog' in mapEntryList
    print 'cat1' in mapEntryList

    # Remove
    mapEntryList.remove('dog')

    # Print all the item
    for i in mapEntryList:
        print i,
    print ''

    # Print the value
    print mapEntryList.valueOf('cat')    

if __name__ == "__main__":
    testMyMap()