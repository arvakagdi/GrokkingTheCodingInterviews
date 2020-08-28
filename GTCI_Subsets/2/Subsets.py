'''
Given a set with distinct elements, find all of its distinct subsets.

'''

def find_subsets(nums):
    subsets = []
    subsets.append([])

    for curr_num in nums:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(curr_num)
            subsets.append(set)
    return subsets
        
def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()