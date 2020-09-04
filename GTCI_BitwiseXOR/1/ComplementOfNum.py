'''
Complement of Base 10 Number

Problem Statement #
Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” 
in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1. 
For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

Example 1:

Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.
Example 2:

Input: 10
Output: 5
Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.
'''

def calculate_bitwise_complement(num):
  n = num 
  count = 0

  while n > 0:
    count += 1
    n = n >> 1

  all_ones = pow(2,count) - 1

  return num ^ all_ones


print('Bitwise complement is: ' + str(calculate_bitwise_complement(6)))
print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


#Time: O(b) b is numebr of bits required to store the curr number
#Space: O(1)