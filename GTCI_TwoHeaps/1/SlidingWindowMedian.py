from heapq import  *
import heapq

class SlidingWindowMedian:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for _ in range(len(nums) - k + 1)]
        for num in range(0, len(nums)):
            if not self.maxHeap or -self.maxHeap[0] >= nums[num]:
                heappush(self.maxHeap, -nums[num])
            else:
                heappush(self.minHeap, nums[num])

            self.heap_adjust()

            if num - k + 1 >= 0:    #if we have k elements in sliding window
                if len(self.minHeap) == len(self.maxHeap):
                    result[num - k + 1] = (-self.maxHeap[0] + self.minHeap[0])/2.0
                else:
                    result[num - k + 1] = -self.maxHeap[0]/1.0 

                elementToBeRemoved = nums[num - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap,-elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)

                self.heap_adjust()
        return result

    def heap_adjust(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]

        if ind < len(heap):
            heapify(heap)

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5,8,-2,10,4,7,2,1], 6)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()
