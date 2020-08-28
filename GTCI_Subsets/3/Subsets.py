def find_subsets(nums):
    subsets = []
    subsets.append([])

    for curr_num in nums:
        for i in range(len(subsets)):
            newlist = list(subsets[i])
            newlist.append(curr_num)
            subsets.append(newlist)
    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
