#
#  SortingLab_main.py
#  Lab 7 Recursive Sorts
#
#  Created by Jim Bailey on 11/15/19.
#  Licensed under a Creative Commons Attribution 4.0 International License.
#
from Heap import Heap
from PriorityQ import PriorityQ
from RecSorts import heapSort
from RecSorts import mergeSort
from RecSorts import quickSort
from RecSorts import findNth


def main():
    # Uncomment line to run test

    # # Basic Lab Tests
    testHeap()
    testPriorityQ()

    # # Advanced Lab Tests
    # # These require the implementation of a static class containing the appropriate methods
    # testHeapSort()
    # testMergeSort()
    # testQuickSort()
    #
    # # Thinking Problem Test
    # testFindNth()

# constant for test functions
NUM_VALUES = 15


def testHeap():
    heapVals = [10, 5, 30, 15, 20, 40, 60, 25, 50, 35, 45, 65, 70, 75, 55]

    print("Creating heap of default size (10)")
    pile = Heap()

    print("Now filling it with 15 values, should cause doubling of size")
    for item in heapVals:
        pile.addItem(item)

    print("Now removing values to see if properly ordered")
    print(" In order s/b: 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75")
    print(" Actual order: ", end="")
    for index in range(NUM_VALUES):
        print(str(pile.getItem()), end=" ")
    print("\n")

    print("Now testing for exception on removing")
    try:
        pile.getItem()
        print("Should have failed, but did not")
    except:
        print("Caught an exception")

    print("\nDone with testing heap\n\n")


def testPriorityQ():
    pqVals = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11, 15, 12, 14, 13]

    print("Creating priority queue of default size (10)")
    pList = PriorityQ()

    print("Now filling it with 15 values, should cause doubling of size")
    for item in pqVals:
        pList.addItem(item)

    print("Now removing values to see if properly ordered")
    print(" In order s/b: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
    print(" Actual order: ", end="")
    for index in range(NUM_VALUES):
        print(str(pList.getItem()), end=" ")
    print("\n")

    print("Now testing for exception on removing")
    try:
        pList.getItem()
        print("Should have failed, but did not")
    except:
        print("Caught an exception")

    print("\nDone with testing priority Queue\n\n")


def testHeapSort():
    heapArray = [41, 2, 3, 5, 13, 17, 43, 23, 29, 7, 11, 19, 31, 37, 47]

    # show starting array
    print("Starting array for heap sort is ")
    for item in heapArray:
        print(str(item), end=" ")
    print("\n")

    # now sort it
    heapSort(heapArray, NUM_VALUES)

    # show sorted array, should be in ascending order
    print("Now the array should be sorted")
    print(" expected: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47")
    print(" actually: ", end="")
    for item in heapArray:
        print(str(item), end=" ")
    print()

    print("\nDone with testing heap sort\n")


def testMergeSort():
    mergeArray = [41, 2, 3, 5, 13, 17, 43, 23, 29, 7, 11, 19, 31, 37, 47]

    # show starting array
    print("Starting array for merge sort is ")
    for item in mergeArray:
        print(str(item), end=" ")
    print("\n")

    # now sort it
    mergeSort(mergeArray, NUM_VALUES)

    # show sorted array, should be in ascending order
    print("Now the array should be sorted")
    print(" expected: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47")
    print(" actually: ", end="")
    for item in mergeArray:
        print(str(item), end=" ")
    print()

    print("\nDone with testing merge sort\n")


def testQuickSort():
    quickArray = [41, 2, 3, 5, 13, 17, 43, 23, 29, 7, 11, 19, 31, 37, 47]

    # show starting array
    print("Starting array quick sort is ")
    for item in quickArray:
        print(str(item), end=" ")
    print("\n")

    # now sort it
    quickSort(quickArray, NUM_VALUES)

    # show sorted array, should be in ascending order
    print("Now the array should be sorted")
    print(" expected: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47")
    print(" actually: ", end="")
    for item in quickArray:
        print(str(item), end=" ")
    print()

    print("\nDone with testing quick sort\n")


def testFindNth():
    findArray = [41, 2, 3, 5, 13, 17, 43, 23, 29, 7, 11, 19, 31, 37, 47]

    # show starting array
    print("Starting array is ")
    for item in findArray:
        print(str(item), end=" ")
    print("\n")

    # now find a value
    print("Finding the 7th value, should be 19")
    print(" actually is : ", end="")
    print(findNth(findArray, NUM_VALUES, 7))

    # show updated array, should be in partially sorted order
    print("Now the array should be partially sorted")
    print(" actually: ", end="")
    for item in findArray:
        print(str(item), end=" ")
    print()

    print("\nDone with testing findNth sort\n")


if __name__ == '__main__':
        main()
