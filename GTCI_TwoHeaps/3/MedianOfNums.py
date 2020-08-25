from heapq import *

class CalculateMedian:
    def __init__(self):
        self.MaxHeap = []
        self.MinHeap = []

    def insertNum(self,num):
        if not self.MaxHeap or -self.MaxHeap[0] > num:
            heappush(self.MaxHeap, -num)
        else:
            heappush(self.MinHeap, num)

        
        if len(self.MaxHeap) >= len(self.MinHeap) + 1:
            heappush(self.MinHeap, -heappop(self.MaxHeap))
        elif len(self.MinHeap) > len(self.MaxHeap):
            heappush(self.MaxHeap, -heappop(self.MinHeap))

    def findMedian(self):
        if len(self.MaxHeap) == len(self.MinHeap):
            return (-self.MaxHeap[0])/2.0 + self.MinHeap[0]/2.0
        else:
            return -self.MaxHeap[0]/1.0

def main():
    medianOfStream = CalculateMedian()
    medianOfStream.insertNum(3)
    medianOfStream.insertNum(1)
    print("The median is: " + str(medianOfStream.findMedian()))
    medianOfStream.insertNum(5)
    print("The median is: " + str(medianOfStream.findMedian()))
    medianOfStream.insertNum(4)
    print("The median is: " + str(medianOfStream.findMedian()))

main()