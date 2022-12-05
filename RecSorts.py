def heapSort(array, length):
    """Sorts an array from smallest to largest at location 0 to largest"""
    #start with first node that has children (length/2)    
    #FIRST SORT INTO A MAX HEAP
    startIndex = (length // 2)
    
    # #========================================================================
    # #TEMP FOR TESTING ONLY ==================================================
    # tempout = "" #TEMP FOR TESTING ONLY
    # tempout += f"Array: {array}\n" #TEMP FOR TESTING ONLY
    # tempout += f"Array length: {length}\n" #TEMP FOR TESTING ONLY
    # tempout += f"   Starting node [index:{startIndex}] [value:{array[startIndex]}]\n" #TEMP FOR TESTING ONLY
    # print (tempout) #TEMP FOR TESTING ONLY
    # #TEMP FOR TESTING ONLY ==================================================
    # #========================================================================
    parentIndex = startIndex
    for i in range(startIndex, -1, -1):
        heapify(array, length, i)
        
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout = "" #TEMP FOR TESTING ONLY
        # tempout += f"Heapification has finished...\n" #TEMP FOR TESTING ONLY
        # tempout += f"\n\n" #TEMP FOR TESTING ONLY
        # tempout += f"Moving to array order swap...\n" #TEMP FOR TESTING ONLY
        # print (tempout) #TEMP FOR TESTING ONLY
        # tempout = "" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================
    # #========================================================================
    # #TEMP FOR TESTING ONLY ==================================================
    # print (f"\nReturned from the initial heapify with array:") #TEMP FOR TESTING ONLY
    # print (f"   {array}") #TEMP FOR TESTING ONLY
    # #TEMP FOR TESTING ONLY ==================================================
    # #========================================================================

    for i in range(length - 1, 0, -1):
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout = "" #TEMP FOR TESTING ONLY
        # tempout += f"Swapping array items (index:[0] value:[{array[0]}]) <--> (index:[{i}] value:[{array[i]}])\n" #TEMP FOR TESTING ONLY
        # print (tempout) #TEMP FOR TESTING ONLY
        # tempout = "" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================
        iValue = array[i]
        array[i] = array[0]
        array[0] = iValue
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout = "" #TEMP FOR TESTING ONLY
        # tempout += f"Array items swapped, submitting items root through index [{i}] for reheapification...\n" #TEMP FOR TESTING ONLY
        # print (tempout) #TEMP FOR TESTING ONLY
        # tempout = "" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================

        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # print (f"\nEntering heapify with array:") #TEMP FOR TESTING ONLY
        # print (f"   {array}") #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================

        heapify(array, i, 0) #Heapify items root through current index

        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # print (f"Returned from heapify with array:") #TEMP FOR TESTING ONLY
        # print (f"   {array}\n") #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================



def heapify(array, length, root):
    """Given an array of a certain length and the parent index recursively set the root as the largest"""
    maxValueIndex = root
    leftChildIndex =  (2 * root) + 1
    rightChildIndex =  (2 * root) + 2
    # #========================================================================
    # #TEMP FOR TESTING ONLY ==================================================
    # tempout = "" #TEMP FOR TESTING ONLY
    # tempout += f"\nEntered heapify for [index:{root}] [value:{array[root]}]\n" #TEMP FOR TESTING ONLY
    # tempout += f"   Left node [index:{leftChildIndex}]\n" #TEMP FOR TESTING ONLY
    # tempout += f"   Right node [index:{rightChildIndex}]" #TEMP FOR TESTING ONLY
    # print (tempout) #TEMP FOR TESTING ONLY
    # tempout = "" #TEMP FOR TESTING ONLY
    # #TEMP FOR TESTING ONLY ==================================================
    # #========================================================================
    if leftChildIndex < length and array[root] < array[leftChildIndex]: #If the left child is in the array it's value is greater than the root value
        maxValueIndex = leftChildIndex #Root should now become the leftChild
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout += f"   Left node [{array[leftChildIndex]}] was larger than root [{array[maxValueIndex]}]. Set left node to max for swap...\n" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================

    if rightChildIndex < length and array[maxValueIndex] < array[rightChildIndex]: #If the right child is in the array it's value is greater than the largest (either root or left if it already )
        maxValueIndex = rightChildIndex #Root should now become the rightChild
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout += f"   Right node [{array[rightChildIndex]}] was larger than current max [{array[maxValueIndex]}]. Set left node to max for swap...\n" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================
    
    if maxValueIndex != root: #If child was identiied as having larger value, perform the swap
        oldRootValue = array[root]
        array[root] = array[maxValueIndex]
        array[maxValueIndex] = oldRootValue
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout += f"   Swapping occured. Sending new root {array[maxValueIndex]} to heapify...\n" #TEMP FOR TESTING ONLY
        # print (tempout) #TEMP FOR TESTING ONLY
        # tempout = "" #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================
        heapify(array, length, maxValueIndex) #Recursively run the heapify again based on the new root structure
    #     #========================================================================
    #     #TEMP FOR TESTING ONLY ==================================================
    # else: #TEMP FOR TESTING ONLY
    #     tempout += f"   Swapping did not occur. Returning from heapify...\n" #TEMP FOR TESTING ONLY
    #     print (tempout) #TEMP FOR TESTING ONLY
    #     tempout = "" #TEMP FOR TESTING ONLY
    #     #TEMP FOR TESTING ONLY ==================================================
    #     #========================================================================    
    



def mergeSort(array, length):
    """Sorts the current array by recursively splitting into halves until length <= 1, then pushes back the sorted array"""
    # print(f"======Starting mergeArrays run. Array: {array}\n") #TEMP FOR TESTING ONLY
    arrayFirst = array[:(length//2)]
    arrayFirstLength = len(arrayFirst)
    arraySecond = array[(length//2):]
    arraySecondLength = len(arraySecond)

    # #========================================================================
    # #TEMP FOR TESTING ONLY ==================================================
    # tempout = "" #TEMP FOR TESTING ONLY
    # tempout += f"Entered new mergeSort...\n" #TEMP FOR TESTING ONLY
    # tempout += f"   InputArray ({length}): {array}\n\n" #TEMP FOR TESTING ONLY
    # tempout += f"   arrayFirst ({arrayFirstLength}): {arrayFirst}\n\n" #TEMP FOR TESTING ONLY
    # tempout += f"   arraySecond ({arraySecondLength}): {arraySecond}\n" #TEMP FOR TESTING ONLY
    # print (tempout) #TEMP FOR TESTING ONLY
    # #TEMP FOR TESTING ONLY ==================================================
    # #========================================================================    

    if arrayFirstLength > 1: #If the array is larger than 1, split it again recursively
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout = "" #TEMP FOR TESTING ONLY
        # tempout += f"   First array length ({arrayFirstLength}) > 1. Submitting for recursion...\n" #TEMP FOR TESTING ONLY
        # print (tempout) #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================    

        mergeSort(arrayFirst, arrayFirstLength)

    if arraySecondLength > 1: #If the array is larger than 1, split it again recursively
        # #========================================================================
        # #TEMP FOR TESTING ONLY ==================================================
        # tempout = "" #TEMP FOR TESTING ONLY
        # tempout += f"   Second array length ({arraySecondLength}) > 1. Submitting for recursion...\n" #TEMP FOR TESTING ONLY
        # print (tempout) #TEMP FOR TESTING ONLY
        # #TEMP FOR TESTING ONLY ==================================================
        # #========================================================================

        mergeSort(arraySecond, arraySecondLength)
        
    # #========================================================================
    # #TEMP FOR TESTING ONLY ==================================================
    # tempout = "" #TEMP FOR TESTING ONLY
    # tempout += f"   Both arrays are <=1. Merging together and returning...\n" #TEMP FOR TESTING ONLY
    # print (tempout) #TEMP FOR TESTING ONLY
    # #TEMP FOR TESTING ONLY ==================================================
    # #========================================================================

    newArray = mergeArrays(arrayFirst, arraySecond)
    array[:] = newArray
    # print(f"======Last line of a mergeArrays run. Array: {array}\n") #TEMP FOR TESTING ONLY
    return array
        

def mergeArrays(firstArray, secondArray):
    """Merget the two arrays back into a single array"""
    mergedArray = []
    index1 = 0
    length1 = len(firstArray)
    index2 = 0
    length2 = len(secondArray)
    # #========================================================================
    # #TEMP FOR TESTING ONLY ==================================================
    # tempout = "" #TEMP FOR TESTING ONLY
    # tempout += f"   Arrays passed for merging...\n" #TEMP FOR TESTING ONLY
    # tempout += f"       arrayFirst ({length1}): {firstArray}\n" #TEMP FOR TESTING ONLY
    # tempout += f"       arraySecond ({length2}): {secondArray}\n\n" #TEMP FOR TESTING ONLY
    # #TEMP FOR TESTING ONLY ==================================================
    # #========================================================================

    while index1 < len(firstArray) and index2 < len(secondArray):
        # tempout += f"           Comparing {firstArray[index1]}[{index1}] to {secondArray[index2]}[{index2}]\n" #TEMP FOR TESTING ONLY
        if firstArray[index1] < secondArray[index2]:
            # tempout += f"               {firstArray[index1]}[{index1}] from first array added (inside comparison)\n" #TEMP FOR TESTING ONLY
            mergedArray.append(firstArray[index1])
            index1+=1
        else:
            # tempout += f"               {secondArray[index2]}[{index2}] from second array added (inside comparison)\n" #TEMP FOR TESTING ONLY
            mergedArray.append(secondArray[index2])
            index2+=1
    
    # tempout += f"           Checking standalone for first array[index1:{index1}] length1[{length1}]...\n" #TEMP FOR TESTING ONLY
    for i in range(index1, length1):
        # tempout += f"               {firstArray[index1]}[{index1}] from first array added (standalone)\n" #TEMP FOR TESTING ONLY
        mergedArray.append(firstArray[index1])
        index1+=1
        

    # tempout += f"           Checking standalone for second array[index1:{index2}] length1[{length2}]...\n" #TEMP FOR TESTING ONLY
    for i in range(index2, length2):
        # tempout += f"               {secondArray[index2]}[{index2}] from second array added (standalone)\n" #TEMP FOR TESTING ONLY
        mergedArray.append(secondArray[index2])
        index2+=1

    # #========================================================================
    # #TEMP FOR TESTING ONLY ==================================================
    # tempout += f"\n     mergedArray ({len(mergedArray)}): {mergedArray}\n\n" #TEMP FOR TESTING ONLY
    # print (tempout) #TEMP FOR TESTING ONLY
    # #TEMP FOR TESTING ONLY ==================================================
    # #========================================================================    


    return mergedArray




def quickSort(array, length):
    """Sorts an array from smallest to largest at location 0 to largest"""
    first = 0
    last = length-1
    recQuickSort(array, first, last)

def recQuickSort(theArray, first, last):
    """"""
    if first < last:
        pivot = partition(theArray, first, last)
        recQuickSort(theArray, first, pivot-1)
        recQuickSort(theArray, pivot+1, last)

def partition(theArray, first, last):
    """"""
    pivotIndex = first
    pivotElement = theArray[first]
    index = first + 1
    while index <= last:
        if theArray[index] <= pivotElement:
            pivotIndex += 1
            theArray[index], theArray[pivotIndex] = theArray[pivotIndex], theArray[index]
        index +=1

    theArray[first], theArray[pivotIndex] = theArray[pivotIndex], theArray[first]
    return pivotIndex




def findNth(array, length, n):
    """Returns the value at the Nth index of the array without doing a complete sort"""



