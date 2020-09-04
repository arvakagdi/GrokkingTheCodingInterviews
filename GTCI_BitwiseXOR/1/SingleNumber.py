'''
Problem Statement #
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:

Input: 7, 9, 7
Output: 9

Solution with XOR #
following are the two properties of XOR:

It returns zero if we take XOR of two same numbers.
It returns the same number if we XOR with zero.
So we can XOR all the numbers in the input; duplicate numbers will zero out each other and we will be left with the single number.
'''


def find_single_number(arr):
    x2 = arr[0]

    for i in arr[1:]:
        x2 = x2 ^ i

    return x2    

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()

'''
Time Complexity: Time complexity of this solution is O(n) as we iterate through all numbers of the input once.

Space Complexity: The algorithm runs in constant space O(1).'''