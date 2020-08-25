from heapq import *

class SlidingWindowMedian:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for _ in range(len(nums) - k + 1)]
        for i in range(0,len(nums)):
            if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.adjust_heap()
            
            if i - k + 1 >= 0:
                if len(self.minHeap) == len(self.maxHeap):
                    result[i-k+1] = (-self.maxHeap[0] + self.minHeap[0] ) / 2.0
                else:
                    result[i-k+1] = - self.maxHeap[0]/1.0
            
                elementToBeDeleted = nums[i-k+1]

                if -self.maxHeap[0] >= elementToBeDeleted:
                    self.remove(self.maxHeap, -elementToBeDeleted)
                else:
                    self.remove(self.minHeap,elementToBeDeleted)

                self.adjust_heap()
                        
        return result

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]

        if ind < len(heap):
            heapify(heap)


    def adjust_heap(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

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
