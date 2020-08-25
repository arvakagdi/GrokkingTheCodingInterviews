from heapq import *

class SlidingWindowMedian:
    def __init__(self):
        self.MinHeap = []
        self.MaxHeap = []

    def find_sliding_window_median(self, nums, k):
        result = [0 for _ in range(len(nums)- k + 1)]

        for i in range(len(nums)):
            if not self.MaxHeap or -self.MaxHeap[0] >= nums[i]:
                heappush(self.MaxHeap, -nums[i])
            else:
                heappush(self.MinHeap, nums[i])

            self.adjust_heap()

            if i - k + 1 >= 0:
                if len(self.MinHeap) == len(self.MaxHeap):
                    result[i-k+1] = self.MinHeap[0]/2.0 + -self.MaxHeap[0]/2.0
                else:
                    result[i-k+1] = -self.MaxHeap[0]/1.0

                elementToBeRemoved = nums[i-k+1]

                if elementToBeRemoved <= -self.MaxHeap[0]:
                    self.remove(self.MaxHeap,-elementToBeRemoved)
                else:
                    self.remove(self.MinHeap, elementToBeRemoved)

                self.adjust_heap()
       
        return result

    def adjust_heap(self):
        if len(self.MinHeap) + 1 < len(self.MaxHeap):
            heappush(self.MinHeap, -heappop(self.MaxHeap))
        elif len(self.MinHeap) > len(self.MaxHeap):
            heappush(self.MaxHeap, -heappop(self.MinHeap))

    def remove(self,heap,elem):
        ind = heap.index(elem)
        heap[ind] = heap[-1]
        del heap[-1]
        heapify(heap)

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()
