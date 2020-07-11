'''
Smallest Window containing Substring (hard) #
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''

def find_substring1(str1, pattern):
    win_start, matched, substr_start = 0,0,0
    char_freq = {}
    min_length = len(str1) + 1

    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for win_end in range(len(str1)):
        right_char = str1[win_end]

        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] >= 0:   # if pattern has more than 1 number of same char
                matched += 1

        while matched == len(pattern):
            if min_length > win_end - win_start + 1:
                min_length = win_end - win_start + 1
                substr_start = win_start

            left_char = str1[win_start]
            win_start += 1

            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

    if min_length == len(str1) + 1:
        return  " "
    return str1[substr_start: substr_start + min_length]



print( " ")
def main():
    print(find_substring1("aabdec", "abc"))
    print(find_substring1("abdabca", "abc"))
    print(find_substring1("adcad", "abc"))
    print(find_substring1("adcadbdjkjkdkdjauuz", "auz"))
    print(find_substring1("abdhqbaghc","abc"))
main()
