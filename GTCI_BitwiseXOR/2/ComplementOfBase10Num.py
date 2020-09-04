def calculate_bitwise_complement (num):
    n,count = num, 0

    while n > 0:
        count += 1
        n = n >> 1

    setbits = pow(2,count) - 1

    return num ^ setbits




print('Bitwise complement is: ' + str(calculate_bitwise_complement(6)))
print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


#Time: O(b) b is numebr of bits required to store the curr number
#Space: O(1)
