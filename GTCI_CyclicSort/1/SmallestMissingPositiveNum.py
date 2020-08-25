'''
Find the Smallest Missing Positive Number (medium) #
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4

'''

def find_first_missing_positive(nums):
    i = 0

    while i < len(nums):
        j = nums[i]

        if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

        else:
            i += 1

    for i in range(1,len(nums)):
        if nums[i] != i:
            return i

    return len(nums)



def main():
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([-10,-5,-7, 3, 4, -2, 0, 1, 2, 8]))
    print(find_first_missing_positive([3, 2, 5, 1]))
main()


'''
Time complexity #
The time complexity of the above algorithm is O(n).

Space complexity #
The algorithm runs in constant space O(1)
'''