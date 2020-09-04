'''
How do we search in a sorted and rotated array that also has duplicates?

The code above will fail in the following example!

Example 1:

Input: [3, 7, 3, 3, 3], key = 7
Output: 1
Explanation: '7' is present in the array at index '1'.

Solution #
The only problematic scenario is when the numbers at indices start, middle, and end are the same, as in this case, we can’t decide which part of the array is sorted. In such a case, the best we can do is to skip one number from both ends: start = start + 1 & end = end - 1.
'''

def search_rotated_with_duplicates(arr, key):
    start,end = 0,len(arr)  - 1

    while start <= end:
        mid = (start + end)//2

        if arr[mid] == key:
            return mid

        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1

        
        if arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:
            if key <= arr[end] and key > arr[mid]:
                start = mid + 1

            else:
                end = mid - 1

    return -1
            


def main():
  print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))


main()
