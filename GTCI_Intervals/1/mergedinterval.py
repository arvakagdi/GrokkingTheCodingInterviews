
'''
Problem Statement #
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
svg viewer
Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
'''


from __future__ import print_function

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  merged = []
  
  if len(intervals)  < 2:
      return intervals
  intervals.sort(key=lambda x: x.start)
  start = intervals[0].start
  end = intervals[0].end

  merged.append(Interval(start, end))

  for i in range(1,len(intervals)):
      if intervals[i].start <= merged[-1].end:
          end = max(intervals[i].end, merged[-1].end)
          merged[-1] = (Interval(merged[-1].start,end))
      else:
          merged.append(Interval(intervals[i].start, intervals[i].end))

  return merged


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()


'''
Time complexity: O(NLogN)
Space: O(N)
'''