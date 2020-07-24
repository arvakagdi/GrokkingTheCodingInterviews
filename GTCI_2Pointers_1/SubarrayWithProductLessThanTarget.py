def find_subarrays_mine(arr, target):
    result = []
    left = 0

    while left < len(arr):
        right = left + 1
        if arr[left] < target:
            result.append([arr[left]])
            curr_list = [arr[left]]
            curr_product = arr[left]
        while right < len(arr):
            curr_product *= arr[right]
            if curr_product < target:
                curr_list.append(arr[right])
                result.append(list(curr_list))
                right += 1
            else:
                left += 1
                break
        if right == len(arr):
            left += 1
    return result



from collections import deque
def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from left to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))
  print(find_subarrays([8,2,3,7,8], 60))
  print(find_subarrays([10,30], 30))



main()

print(" ")
print ("-------------------------------------------")

def main():
  print(find_subarrays_mine([2, 5, 3, 10], 30))
  print(find_subarrays_mine([8, 2, 6, 5], 50))
  print(find_subarrays_mine([8,2,3,7,8], 60))
  print(find_subarrays_mine([10,30], 30))


main()

