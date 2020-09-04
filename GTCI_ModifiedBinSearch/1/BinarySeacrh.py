'''
Problem Statement #
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, 
we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
Example 2:

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Example 3:

Input: [10, 6, 4], key = 10
Output: 0
Example 4:

Input: [10, 6, 4], key = 4
Output: 2
'''

def binary_search(arr, key):
    start = 0
    end = len(arr) - 1

    isAscending = arr[start] < arr[end]    # check if seq is ascending or decending


    while start <= end:
        middle = start + (end - start)//2  # find the middle index

        if arr[middle] == key:             # return if we find the key
            return middle
                                           # adjust the start and end points
        if isAscending:                    # Ascending order
            if arr[middle] < key:
                start = middle + 1
            else:
                end = middle - 1

        else:                             # Decending order
            if arr[middle] > key:
                start = middle + 1
            else:
                end = middle - 1
    
    return -1                               # return -1 if key is not found

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()


'''
Time complexity #
Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
where ‘N’ is the total elements in the given array.

Space complexity #
The algorithm runs in constant space O(1).'''
