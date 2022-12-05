EMPTY = ""
class Heap:
    
    """Creates a min heap"""
    def __init__(self, size=10):
        """"""
        self.heapArraySize = size
        self.heapElementsCount = 0
        self.heapArray  = [EMPTY] * size
        self.rootIndex = 1
        

        #leftChildIndex = 2 * index
        #rightChildIndex = (2 * index) + 1
        #parentIndex = index //  2
    
    def addItem(self, value):
        """Adds a new item to the heap"""
        childIndex = self.heapElementsCount + 1 #Items in the array +1 is index of next available spot
        childValue = value
        if self.heapElementsCount >= (self.heapArraySize - 1): #If adding new element would exceed array size, need to resize
            self.heapArray = self.heapArray + ([EMPTY] * self.heapArraySize)
            self.heapArraySize =  self.heapArraySize * 2
        self.heapArray[childIndex] = childValue
        self.heapElementsCount += 1    
        doneAdding = False
        if childIndex == self.rootIndex: #If the new element will be placed in root, flag as rootFound so no further execution takes place
            doneAdding = True
        while doneAdding == False:
            parentIndex = (childIndex // 2)
            parentValue = self.heapArray[parentIndex]
            if parentIndex == self.rootIndex: #If the parent is the root, flag as doneAdding so no further execution takes place after loop
                doneAdding = True
            if parentValue > value: #If the parent value was greater, bubble up (for MIN SORT)
                self.heapArray[parentIndex] = childValue
                self.heapArray[childIndex] = parentValue
                childIndex = parentIndex
            else:
                doneAdding = True
        # # #========================================================================
        # # #TEMP FOR TESTING ONLY ==================================================
        # print (f"   New value {value} has been added...") #TEMP FOR TESTING ONLY
        # # #TEMP FOR TESTING ONLY ==================================================
        # # #========================================================================
                
    def getItem(self):
        """Removes and returns smallest item from the heap"""
        if self.heapElementsCount == 0:
            raise IndexError('out_of_range')
        output = str(self.heapArray[self.rootIndex])
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout = f"\nRemoving smallest value from root... \n" #TEMP FOR TESTING ONLY
        # tempout += f"Current Array:\n" #TEMP FOR TESTING ONLY
        # tempout += f"   {self.heapArray}\n" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================
        newRoot = self.heapArray[self.heapElementsCount] #New root can be found at index of the total # of elements (until the )
        self.heapArray[self.rootIndex] = newRoot #Sets the root to the new value for the root
        self.heapArray[self.heapElementsCount] = EMPTY
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout = f"Item remove/swap has completed... \n" #TEMP FOR TESTING ONLY
        # tempout += f"Current Array:\n" #TEMP FOR TESTING ONLY
        # tempout += f"   {self.heapArray}\n" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================
        self.heapElementsCount -= 1
        doneRemoving = False
        parentIndex = self.rootIndex
        leftChildIndex = 2 * parentIndex
        rightChildIndex = (2 * parentIndex) + 1
        if self.heapElementsCount == 1: #If heap only has one item left, no need to perform bubble down
            doneRemoving = True
        while doneRemoving == False: 
            parentValue = self.heapArray[parentIndex]
            leftChildValue = self.heapArray[leftChildIndex]
            rightChildValue = self.heapArray[rightChildIndex]
            # #========================================================================
            # #TEMP FOR TESTING ONLY ==================================================
            # tempout += f"   Checking if parent is greater than either child...\n" #TEMP FOR TESTING ONLY
            # tempout += f"   Parent [value:{parentValue}][index:{parentIndex}]\n" #TEMP FOR TESTING ONLY
            # tempout += f"   Left   [value:{leftChildValue}][index:{leftChildIndex}]\n" #TEMP FOR TESTING ONLY
            # tempout += f"   Right  [value:{rightChildValue}][index:{rightChildIndex}]\n" #TEMP FOR TESTING ONLY
            # tempout += f"   Count  [{self.heapElementsCount}]\n" #TEMP FOR TESTING ONLY
            # # print(tempout) TEMP FOR TESTING ONLY
            # #TEMP FOR TESTING ONLY ==================================================
            # #========================================================================

            #NEED TO ACCOUNT OF IF EITHER INDEX IS OUT OF RANGE. I THINK LEFT IS ALWAYS FILLED FIRST...?

            if rightChildIndex > self.heapElementsCount or leftChildValue < rightChildValue: #Check the values of each child to find smallest, if right is empty, left is smallest be default
                smallestChildValue = leftChildValue
                smallestChildIndex = leftChildIndex
                # #========================================================================
                # #TEMP FOR TESTING ONLY ==================================================
                # tempout += f"   Left child[{leftChildValue}] was smaller than right[{rightChildValue}]...\n" #TEMP FOR TESTING ONLY
                # #TEMP FOR TESTING ONLY ==================================================
                # #========================================================================
            else:
                smallestChildValue = rightChildValue
                smallestChildIndex = rightChildIndex
                # #========================================================================
                # #TEMP FOR TESTING ONLY ==================================================
                # tempout += f"   Right child[{rightChildValue}] was smaller than left[{leftChildValue}]...\n" #TEMP FOR TESTING ONLY
                # #TEMP FOR TESTING ONLY ==================================================
                # #========================================================================
            if smallestChildValue < parentValue: #If the smallest child is smaller than parent, swap
                # #========================================================================
                # #TEMP FOR TESTING ONLY ==================================================
                # tempout += f"   Child[{smallestChildValue}] was smaller than parent[{parentValue}]...\n" #TEMP FOR TESTING ONLY
                # #TEMP FOR TESTING ONLY ==================================================
                # #========================================================================
                self.heapArray[parentIndex] = smallestChildValue
                self.heapArray[smallestChildIndex] = parentValue
                parentIndex = smallestChildIndex #Set the new parent index and the child index we'll be stepping into as we continue bubble down
                leftChildIndex = 2 * parentIndex #Set the new leftchild index for next iteration
                rightChildIndex = (2 * parentIndex) + 1 #Set the new rightchild index for next iteration
                # #========================================================================
                # #TEMP FOR TESTING ONLY ==================================================
                # tempout += f"   Indexes updated for next loop...\n" #TEMP FOR TESTING ONLY
                # tempout += f"   Parent index will be [{parentIndex}]\n" #TEMP FOR TESTING ONLY
                # tempout += f"   Left index will be   [{leftChildIndex}]\n" #TEMP FOR TESTING ONLY
                # tempout += f"   Right index wil be   [{rightChildIndex}]\n" #TEMP FOR TESTING ONLY
                # tempout += f"   Count is             [{self.heapElementsCount}]\n" #TEMP FOR TESTING ONLY
                # #TEMP FOR TESTING ONLY ==================================================
                # #========================================================================
                if leftChildIndex > self.heapElementsCount or rightChildIndex > self.heapElementsCount:
                    doneRemoving  = True #mark as done removing if either of the newly calcualted children index > elements count                
            else:
                # #========================================================================
                # #TEMP FOR TESTING ONLY ==================================================
                # tempout += f"   Child[{smallestChildValue}] was NOT smaller than parent[{parentValue}]...\n" #TEMP FOR TESTING ONLY
                # #TEMP FOR TESTING ONLY ==================================================
                # #========================================================================
                doneRemoving = True
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # # tempout += f"Current Array:\n" #TEMP FOR TESTING ONLY
        # tempout += f"   {self.heapArray}\n" #TEMP FOR TESTING ONLY
        # tempout += f"Finished resorting array...\n" #TEMP FOR TESTING ONLY
        # tempout += f"Exiting...\n" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================

                



        # output = f"\n{tempout}" #TEMP FOR TESTING ONLY
        return output

    

    def removeLargest(self):
        """"""

    def removeSmallest(self):
        """"""