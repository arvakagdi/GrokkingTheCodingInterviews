from heapq import *

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    maxHeap = []
    minHeap = []
    
    maxCap = initialCapital

    for i in range(len(capital)):
        heappush(minHeap, (capital[i], i))

    while numberOfProjects > 0:
        while minHeap and minHeap[0][0] <= maxCap:
            capital, i = heappop(minHeap)
            heappush(maxHeap, -profits[i])

        if not maxHeap:
            break

        maxCap += -heappop(maxHeap)
        numberOfProjects -= 1  
    return maxCap


def main():

  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()


'''
Since, at the most, all the projects will be pushed to both the heaps once, the time complexity of our algorithm is O(NlogN + KlogN),
where ‘N’ is the total number of projects and ‘K’ is the number of projects we are selecting.

Space complexity #
The space complexity will be O(N) because we will be storing all the projects in the heaps.'''