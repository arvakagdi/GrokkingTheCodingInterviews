def flip_an_invert_image(matrix):
    for row in matrix:
        start,end = 0, len(row) - 1

        while start <= end:
            row[start], row[end] = row[end] ^ 1, row[start] ^ 1
            start += 1
            end -= 1
    return matrix

def main():
    print(flip_an_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_an_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()