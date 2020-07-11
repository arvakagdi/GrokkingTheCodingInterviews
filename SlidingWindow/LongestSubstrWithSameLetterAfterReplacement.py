'''
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
'''

def length_of_longest_substring(str1, k):
  win_start, max_length, max_repeat_char = 0,0,0
  repeat_count = {}

  for win_end in range(len(str1)):
      right_char = str1[win_end]

      if right_char not in repeat_count:
          repeat_count[right_char] = 0
      repeat_count[right_char] += 1

      max_repeat_char = max(max_repeat_char, repeat_count[right_char])

      if win_end - win_start + 1 - max_repeat_char > k:
          left_char = str1[win_start]
          repeat_count[left_char] -= 1
          win_start += 1

      max_length = max(max_length, win_end - win_start + 1)
  return  max_length


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()