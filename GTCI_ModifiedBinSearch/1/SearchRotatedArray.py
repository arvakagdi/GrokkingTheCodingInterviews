'''
Search in Rotated Array (medium) #
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Original array: 1 3 8 10 15   
Array after 2 rotations: 10 15 1 3 8


Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.

Original array: -1 2 4 5 7 9 10   
Array after 5 rotations:  4 5 7 9 10 -1 2 


Solution #
The problem follows the Binary Search pattern. We can use a similar approach as discussed in Order-agnostic Binary Search and modify it similar to Search Bitonic Array to search for the ‘key’ in the rotated array.

After calculating the middle, we can compare the numbers at indices start and middle. This will give us two options:

If arr[start] <= arr[middle], the numbers from start to middle are sorted in ascending order.
Else, the numbers from middle+1 to end are sorted in ascending order.
Once we know which part of the array is sorted, it is easy to adjust our ranges. For example, if option-1 is true, we have two choices:

By comparing the ‘key’ with the numbers at index start and middle we can easily find out if the ‘key’ lies between indices start and middle; if it does, we can skip the second part => end = middle -1.
Else, we can skip the first part => start = middle + 1.
'''

def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end)//2

        if arr[mid] == key:
            return mid
        if arr[mid] < arr[start]:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

  # we are not able to find the element in the given array
    return -1


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()
