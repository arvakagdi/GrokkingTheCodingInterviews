'''
Find the First K Missing Positive Numbers (hard) #
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
'''

def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i = 0
    maxnuminarray = 0


    while i < len(nums):
        j = nums[i]
        maxnuminarray = max(maxnuminarray, nums[i])
        if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1



    for i in range(1,len(nums)):
        if nums[i] != i:
            missingNumbers.append(i)
            k -= 1
                
    if k != 0:
        while k > 0:
            missingNumbers.append(maxnuminarray + 1)
            maxnuminarray += 1
            k -= 1

    return missingNumbers




def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()




'''
#### can be done this way too!! ####

    missingNumbers = []
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    maxnuminarray = 0
    for i in range(0,len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)
            maxnuminarray = max(maxnuminarray, nums[i])
            k -= 1
                
    if k != 0:
        while k > 0:
            missingNumbers.append(maxnuminarray + 1)
            maxnuminarray += 1
            k -= 1

    return missingNumbers




Time complexity #
The time complexity of the above algorithm is O(n + k), as the last two for loops will run for O(n) and O(k) times respectively.

Space complexity #
The algorithm needs O(1) space to store the max number
'''