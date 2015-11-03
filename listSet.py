class MySet:
    # Init
    def __init__(self):
        self._theElements = list()

    # Len
    def __len__(self):
        return len(self._theElements)

    # Equal
    def __equal__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # is subset
    def isSubsetOf(self, setB):

        for item in self:
            if item not in setB:
                return False
        return True

    # add
    def add(self, item):
        if item not in self:
            self._theElements.append(item)

    # remove
    def remove(self, item):
        assert item in self, "item must be in the set."
        self._theElements.remove(item)

    # union
    def union(self, setB):

        newSet = MySet()
        newSet._theElements.extend(self)

        for item in setB:
            if item not in self:
                newSet._theElements.append(item)

        return newSet

    # intersection
    def interset(self, setB):

        newSet = MySet()

        for item in setB:
            if item in self:
                newSet._theElements.append(item)

        return newSet

    # difference
    def difference(self, setB):

        newSet = MySet()

        for item in self:
            if item not in setB:
                newSet._theElements.append(item)

        return newSet

    # iter
    def __iter__(self):
        return _MySetIterator(self._theElements)

# Iterator
class _MySetIterator:
    # Init
    def __init__(self, theElements):
        self._theElements = theElements
        self._index = 0
    def __iter__(self):
        return self
    def next(self):
        if self._index < len(self._theElements):
            item = self._theElements[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
def test_listSet():
    
    print 'Init a set named smith'
    smith = MySet()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    print '\noutput smith set'
    for element in smith:
        print element
    
    print '\nInit a set named roberts'
    roberts = MySet()
    roberts.add('POL-101')
    roberts.add('ANTH-230')
    roberts.add('CSCI-112')
    roberts.add('ECON-101')
 
    print '\noutput roberts set'
    for element in roberts:
        print element   

    print '\ndo the intersection'
    interSet = smith.interset(roberts)
    for element in interSet:
        print element    
        
    print '\ndo the difference'
    diffSet = smith.difference(roberts)
    for element in diffSet:
        print element    
        
    print '\ndo the union'
    uniSet = smith.union(roberts)
    for element in uniSet:
        print element    
        
    print '\nremove a element in the union'
    uniSet.remove('CSCI-112')
    for element in uniSet:
        print element    
        
if __name__ == "__main__":
    test_listSet()