def search_next_letter(letters, key):
    start,end = 0,len(letters) -1 
    if key < letters[start] or key > letters[end]:
        return letters[start]

    while start <= end:
        mid = start + (end - start)//2

        if key == letters[mid]:
            return letters[((mid + 1) % len(letters))]
        
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    return letters[start]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
