from collections import deque

def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])

    numLen = len(nums)

    for curr_num in nums:
        n = len(permutations)

        for _ in range(n):
            oldPerm = permutations.popleft()

            for i in range(len(oldPerm)+1):
                newperm = list(oldPerm)
                newperm.insert(i,curr_num)

                if len(newperm) == numLen:
                    result.append(newperm)
                else:
                    permutations.append(newperm)    
    return result


def main():
    print("Here are all the per`mutations: " + str(find_permutations([1, 3, 5])))


main()
