'''
Problem Statement #
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
'''


def find_missing_number(nums):

    i = 0

    while i < len(nums):
        j = nums[i]
        # place all numbers at it correct places except if its the last elem as we have no space for nth element
        # So, if nth elem is present it will take place of the missing element
        # if nth element is missing, we will get all numbers at it's correct place
        # so we will know the missing element is nth element
        if nums[i] < len(nums) and nums[i] != nums[j]:   
            nums[i],nums[j] = nums[j],nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)      # if  all numbers are on current index the missing one is the last number



def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))

main()
        
