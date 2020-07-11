'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
'''


def longest_substring_with_k_distinct(str1, k):
    # TODO: Write your code here
    start = 0
    distinct_words = {}
    distinctTotal = 0
    curr_length = 0
    max_len = 0

# Iterating through all elements and keeping track of length
    for index in range(len(str1)):
        curr_letter = str1[index]
        if str1[index] in distinct_words:
            distinct_words[curr_letter] += 1
        else:
            distinct_words[curr_letter] = 1
            distinctTotal += 1

        if distinctTotal <= k:
            curr_length += 1

        while len(distinct_words) > k:
            start_word = str1[start]
            distinct_words[start_word] -= 1
            if distinct_words[start_word] == 0:
                del distinct_words[start_word]
                distinctTotal -= 1
            start += 1

        max_len = max(max_len, curr_length)
    return max_len

String="cbbeblkjaaaaamo"
K=3
print(longest_substring_with_k_distinct(String,K))



############################################################################################################

#2nd method

def longest_substring_with_k_distinct1(str1, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
      left_char = str1[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


def main():
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
