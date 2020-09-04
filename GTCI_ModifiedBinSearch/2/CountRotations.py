def count_rotations(arr):
    start,end = 0, len(arr) - 1

    # if arr[end] > arr[start]:
    #     return 0
    while start <= end:
        mid = start + (end - start)//2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > 0 and arr[mid] < arr[mid -1]:
            return mid

        if arr[mid] > arr[start]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


def count_rotations_with_duplicates(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        # if element at mid is greater than the next element
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        # if element at mid is smaller than the previous element
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        # this is the only difference from the previous solution
        # if numbers at indices start, mid, and end are same, we can't choose a side
        # the best we can do is to skip one number from both ends if they are not the smallest number
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            if arr[start] > arr[start + 1]:  # if element at start+1 is not the smallest
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:  # if the element at end is not the smallest
                return end
            end -= 1
        # left side is sorted, so the pivot is on right side
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:  # right side is sorted, so the pivot is on the left side
            end = mid - 1

    return 0  # the array has not been rotated


def main():
  print(count_rotations_with_duplicates([3, 3, 7, 3]))


main()




def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()
