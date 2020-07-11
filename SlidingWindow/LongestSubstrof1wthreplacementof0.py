def length_of_longest_substring(arr, k):
  # TODO: Write your code here
  win_start = 0
  max_length = 0
  count_of_1 = 0
  for win_end in range(0,len(arr)):
      right_char = arr[win_end]

      if right_char == 1:
          count_of_1 += 1

# Current window size is from window_start to window_end, overall we have a maximum of 1s
# repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
# and the remaining are 0s which should replace with 1s.
# now, if the remaining 1s are more than 'k', it is the time to shrink the window as we
# are not allowed to replace more than 'k' 0s

      if win_end - win_start + 1 - count_of_1 > k:
          if arr[win_start] == 1:
              count_of_1 -= 1
          win_start += 1
      max_length = max(max_length, win_end - win_start + 1)

  return max_length


def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
