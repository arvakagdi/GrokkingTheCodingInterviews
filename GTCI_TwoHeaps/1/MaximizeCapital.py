'''
Problem Statement #
Given a set of investment projects with their respective profits, we need to find the most profitable projects. 
We are given an initial capital and are allowed to invest only in a fixed number of projects. 
Our goal is to choose projects that give us the maximum profit.

We can start an investment project only when we have the required capital. Once a project is selected, 
we can assume that its profit has become our capital.

Example 1:

Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
Output: 6
Explanation:

With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. 
Once we selected our first project, our total capital will become 3 (profit + initial capital).
With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
After the completion of the two projects, our total capital will be 6 (1+2+3).

Example 2:

Input: Project Capitals=[], Project Profits=[], Initial Capital=0, Number of Projects=3
Output: 8
Explanation:

With ‘0’ capital, we can only select the first project, bringing out capital to 1.
Next, we will select the second project, which will bring our capital to 3.
Next, we will select the fourth project, giving us a profit of 5.
After selecting the three projects, our total capital will be 8 (1+2+5).
'''

from heapq import *

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minHeap = []
    maxHeap = []

    maxcap = initialCapital

    for i in range(len(capital)):
            heappush(minHeap, (capital[i], i))         # keep update of index and capital both to find relevant profit

    while numberOfProjects > 0:       
        # find all projects that can be selected within the available capital and insert them in a max-heap
        while minHeap and minHeap[0][0] <= maxcap:
            capital, i = heappop(minHeap) 
            heappush(maxHeap, -profits[i])

        # terminate if we are not able to find any project that can be completed within the available capital
        if not maxHeap:
            break

        # select the project with the maximum profit
        maxcap += -heappop(maxHeap)

        numberOfProjects -= 1

    return maxcap
            

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
The space complexity will be O(N) because we will be storing all the projects in the heaps.
'''