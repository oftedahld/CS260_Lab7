from Heap import Heap

class PriorityQ:
    """"""
    def __init__(self, size=10):
        self.theQueue = Heap(size)

    def addItem(self, value):
        """adds a new item to the priority queue"""
        self.theQueue.addItem(value)

    def getItem(self):
        """removes and returns the smallest from the priority queue"""
        return self.theQueue.getItem()