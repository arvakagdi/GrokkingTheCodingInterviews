'''
Comparing Strings containing Backspaces (medium) #
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
'''

def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1

    while index1 >= 0 or index2 >= 0:
        char1 = get_next_char(str1,index1)
        char2 = get_next_char(str2,index2)

        if char1 < 0 and char2 < 0:
            return True
        if char1 < 0 or char2 < 0:
            return False
        if str1[char1] != str2[char2]:
            return False

        index1 = char1 - 1
        index2 = char2 - 1

    return True

def get_next_char(mystr, index):
    count = 0
    while index >= 0:
        if mystr[index] == '#':
            count += 1
        elif count > 0:
            count -= 1
        else:
            break
        index -= 1
    return index



def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))
    print(backspace_compare("mk#zz##", "z#m"))


main()
