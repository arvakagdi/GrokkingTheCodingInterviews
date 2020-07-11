'''
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Input: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: Output: [2.2, 2.8, 2.4, 3.6, 2.8]

'''


def find_averages_of_subarrays(K, arr):
  result = []
  windowSum, windowStart = 0.0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]

    if windowEnd >= K - 1:
       result.append(windowSum/K)
       windowSum  -= arr[windowStart]
       windowStart += 1

  return result

def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
