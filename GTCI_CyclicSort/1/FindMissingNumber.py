'''
Problem Statement #
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ 
numbers out of the total ‘n+1’ numbers, find the missing number.

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
        j = nums[i]           # as we have numbers from 0 to n we will have current number on each index
        if nums[i] < len(nums)  and nums[i] != nums[j]:  # check if the number is not at correct place and if it is less than n, swap
            nums[i], nums[j] = nums[j], nums[i] 
        else:
            i += 1     #if the number is at the correct place or the largest number is at the wrong place, increment

    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(n)

def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
    print(find_missing_number([7, 3, 5, 2, 4, 6, 0, 1]))
main()


'''
Time Complexity: O(N)
Space Complexity: O(1)
'''