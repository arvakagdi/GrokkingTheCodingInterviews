from collections import deque

def find_permutations(nums):
    result = []

    permutations = deque()
    permutations.append([])

    for curr_num in nums:
        for i in range(len(permutations)):
            oldperm = permutations.popleft()
            n = len(oldperm)
            for j in range(n + 1):
                newperm = list(oldperm)
                newperm.insert(j,curr_num)

                if len(newperm) == len(nums):
                    result.append(newperm)
                else:
                    permutations.append(newperm)    
    return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
main()
