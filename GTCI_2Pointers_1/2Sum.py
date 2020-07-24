'''
Problem Statement #
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

'''


# Method 1: Time Complexity: O(N), Space Compexity: O(1)
def pair_with_targetsum(arr, target_sum):
    # left and right pointers pointing  to first and last element of array
    left = 0
    right = len(arr) - 1

    if len(arr) <= 1:
        return []

    # find sum and if that sum is equal to target return the left and right index else adjust pointers
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            return [left,right]

        if sum < target_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]   # if no 2 element with target sum present


# Method 2: Time Complexity: O(N), Space Compexity: O(N)  -- This method works well when array is not sorted
def pair_with_targetsum1(arr, target_sum):
    num_seen = {}   # Hashtable for seen numbers and their indices

    for index,num in enumerate(arr):
        secondnum = target_sum - num
        if secondnum in num_seen:       #if we find a pair return indices else store the num in Hashtable
            return [num_seen[secondnum], index]
        else:
            num_seen[num] = index

    return [-1,-1]   #if no pair found


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum1([2, 5, 9, 11], 11))

main()
