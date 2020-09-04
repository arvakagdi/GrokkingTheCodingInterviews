'''
Problem Statement (hard) #
Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally 
results in [1, 1, 0].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] 
 results in [0, 0, 1].
'''

def flip_an_invert_image(matrix):
    for row in matrix:
        start = 0
        end = len(row) - 1

        while start <= end:
            row[start], row[end] = row[end]^1, row[start]^1
            start += 1
            end -= 1

    return matrix


def main():
    print(flip_an_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_an_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()

'''
Time Complexity #
The time complexity of this solution is O(n)O(n) as we iterate through all elements of the input.

Space Complexity #
The space complexity of this solution is O(1)O(1).'''