'''
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
'''

def non_repeat_substring(str1):
    win_start = 0
    max_len = 0
    char_index = {}

    for win_end in range(0, len(str1)):
        right_char = str1[win_end]
        # if the map already contains the 'right_char', shrink the window from the beginning so that
        # we have only one occurrence of 'right_char'
        if right_char in char_index:
            # In the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            win_start = max(win_start, char_index[right_char] + 1)
        # insert the 'right_char' into the map
        char_index[right_char] = win_end
        # max length count
        max_len = max(max_len, win_end - win_start + 1)

    return max_len

#Tests
def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
