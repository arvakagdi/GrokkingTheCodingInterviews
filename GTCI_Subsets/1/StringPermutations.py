'''
Problem Statement #
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''

def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for k in range(n):
                newlist = list(permutations[k])
                newlist[i] = newlist[i].swapcase()
                permutations.append(''.join(newlist))
        
    return permutations

def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()


'''
Time complexity #
Since we can have 2^N permutations at the most and while processing each permutation we convert it into a character array,
the overall time complexity of the algorithm will be O(N*2^N).

Space complexity #
All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N)permutations,
the space complexity of our algorithm is O(N*2^N)
'''