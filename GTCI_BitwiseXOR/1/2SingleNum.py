'''
Problem Statement #
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

Example 1:

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:

Input: [2, 1, 3, 2]
Output: [1, 3]'''

def find_single_numbers(nums):
    # first xor all the nums so the remaining would be xor of required 2 nums

    n1xn2 = 0

    for num in nums:
        n1xn2 ^= num

    rightsetbit = 1      # keep track of a right set bit to find the righmost bit set in n1xn2

    while (rightsetbit & n1xn2) == 0:       # keep shifting rightsetbit to left until you find the set bit in n1xn2
        rightsetbit = rightsetbit << 1
    
    num1, num2 = 0,0    

    # now according to the set bit put numbers in 2 lists and keep xoring them to find the required nums

    for num in nums:            
        if (rightsetbit & num) != 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()


# Time : O(N)
# Space : O(1)