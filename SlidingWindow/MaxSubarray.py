'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
'''


def max_sub_array_of_size_k(k, arr):
  currSum = 0
  start = 0
  maxSum = 0

  for index in range(len(arr)):
    currSum += arr[index]

    if index >= k - 1:
      maxSum = max(maxSum,currSum)
      currSum -= arr[start]
      start += 1

  return maxSum


Input = [2, 1, 5, 1, 3, 2]
input1 = [10,1,0,4,-5,-6,10,2,5]

print(max_sub_array_of_size_k(3,Input))
print(max_sub_array_of_size_k(3,input1))


