'''
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
'''

def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    for fir_num in range(0,len(arr) - 3):
        if fir_num > 0 and arr[fir_num] == arr[fir_num - 1]:
            continue
        for sec_num in range(fir_num + 1, len(arr) - 2):
            if sec_num > fir_num + 1 and arr[sec_num] == arr[sec_num - 1]:
                continue
            left = sec_num + 1
            right = len(arr) - 1

            remaining = target - arr[fir_num] - arr[sec_num]

            while left < right:
                if remaining == arr[left] + arr[right]:
                    quadruplets.append([arr[fir_num], arr[sec_num],arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1  # skip same element to avoid duplicate quadruplets
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1  # skip same element to avoid duplicate quadruplets
                elif remaining < arr[left] + arr[right]:
                    right -= 1
                else:
                    left += 1
    return quadruplets

def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()