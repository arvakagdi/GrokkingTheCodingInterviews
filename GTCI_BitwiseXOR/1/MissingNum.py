'''
Given an array of n-1n−1 integers in the range from 11 to nn, find the one number that is missing from the array.
Input: 1, 5, 2, 6, 4
Answer: 3

The important property of XOR that it returns 0 if both the bits in comparison are the same. In other words, XOR of a number with itself will always result in 0. This means that if we XOR all the numbers in the input array with all numbers from the range 11 to nn then each number in the input is going to get zeroed out except the missing number. Following are the set of steps to find the missing number using XOR:

XOR all the numbers from 1 to nn, let’s call it x1.
XOR all the numbers in the input array, let’s call it x2.
The missing number can be found by x1 XOR x2.
'''

def find_missing_number(arr):
  n = len(arr) + 1
  # x1 represents XOR of all values from 1 to n
  x1 = 1
  for i in range(2, n+1):
    x1 = x1 ^ i

  # x2 represents XOR of all values in arr
  x2 = arr[0]
  for i in range(1, n-1):
    x2 = x2 ^ arr[i]
  
  # missing number is the xor of x1 and x2
  return x1 ^ x2

def main():
  arr = [1, 5, 2, 6, 4] 
  print('Missing number is:' + str(find_missing_number(arr)))

main()
  

#time O(n)
#Space O(1)