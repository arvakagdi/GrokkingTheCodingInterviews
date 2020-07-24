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
