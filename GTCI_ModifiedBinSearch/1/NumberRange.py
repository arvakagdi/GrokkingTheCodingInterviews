'''
Problem Statement #
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
'''


def find_range1(arr, key):
    result = [-1, -1] 
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2

        if key == arr[mid]:
            
            startIndex = mid
            while startIndex >= start and arr[startIndex - 1] == key:
                startIndex -= 1

            result[0] = startIndex

            endIndex = mid
            while endIndex <= end and arr[endIndex + 1] == key:
                endIndex += 1
            result[1] = endIndex
            return result

        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return result
#############################################################################################

def find_range(arr, key):
    result = [-1, -1]

    result[0] = binarySearch(arr,key, False)
    result[1] = binarySearch(arr,key,True)

    return result
    

def binarySearch(arr,key,MaxIndex):
    keyIndex = -1
    start,end = 0, len(arr)

    while start <= end:
        mid = (start + end)//2

        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            keyIndex = mid
            if MaxIndex:
                start = mid + 1
            else:
                end = mid - 1

    return keyIndex

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()


def main():
  print(find_range1([4, 6, 6, 6, 9], 6))
  print(find_range1([1, 3, 8, 10, 15], 10))
  print(find_range1([1, 3, 8, 10, 15], 12))


main()


# O(log(n))