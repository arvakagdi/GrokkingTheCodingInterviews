'''
Problem Statement #
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
'''


def dutch_flag_sort(arr):
    # all elements < left are 0, and all elements > right are 2
    # all elements from >= low < i are 1
    left = 0
    right = len(arr) - 1
    index = 0

    while index <= right:
        if arr[index] == 0:
            arr[left],arr[index] = arr[index], arr[left]
            index += 1
            left += 1
        elif arr[index] == 1:
            index += 1
        else:
            arr[right],arr[index] = arr[index], arr[right]
            right -= 1

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)


main()
