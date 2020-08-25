from heapq import *

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    maxCap = initialCapital
    maxHeap = []
    minHeap = []

    for i in range(len(capital)):
        heappush(minHeap, (capital[i], i))
    
    while numberOfProjects > 0:
        while minHeap and minHeap[0][0] <= maxCap:
            capital,index = heappop(minHeap)
            heappush(maxHeap, -profits[index])

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
