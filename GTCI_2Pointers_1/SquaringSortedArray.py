'''
Problem Statement #
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

'''

#Time & Space complexity = O(N)

def make_squares(arr):
  n = len(arr)
  squares = [None] * n
  right = n -1
  left = 0
  last_index = n - 1

  while left <= right:
      leftsq = arr[left] * arr[left]
      rightsq = arr[right] * arr[right]

      if leftsq > rightsq:
          squares[last_index] = leftsq
          left += 1
      else:
          squares[last_index] = rightsq
          right -= 1
      last_index -= 1
  return  squares



def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()