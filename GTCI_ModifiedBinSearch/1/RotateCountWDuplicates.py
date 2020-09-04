def count_rotations_with_duplicates(arr):
    start,end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start)//2  
    
        # if element at mid is smaller than the previous element
        if mid > start and arr[mid] < arr[mid - 1]:
            return mid

        # if element at mid is greater than the next element  
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1


    # if numbers at indices start, mid, and end are same, we can't choose a side
    # the best we can do is to skip one number from both ends if they are not the smallest number
        if arr[mid] == arr[start] and arr[mid] == arr[end]:
            if arr[start] > arr[start + 1]:
                return start + 1
            start += 1

            if arr[end] < arr[end - 1]:        
                return end
            end -= 1

    # left side is sorted, so the pivot is on right side
        elif arr[mid] > arr[start] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:   # right side is sorted, so the pivot is on the left side
            end = mid - 1

    return 0   # No Rotations

    
def main():
  print(count_rotations_with_duplicates([3, 3, 7, 3]))


main()
