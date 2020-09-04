def calculate_bitwise_complement(n):
    count, num = 0, n

    while num > 0:
        count += 1
        num = num >> 1

    setBits = pow(2,count) - 1
    return n ^ setBits


def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()