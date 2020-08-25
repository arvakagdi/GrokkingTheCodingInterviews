'''
Problem Statement #
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits,
leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not 
include ‘1’.

Example 1:

Input: 23   
Output: true (23 is a happy number)  

Example 2:

Input: 12   
Output: false (12 is not a happy number)  

Solution #
The process, defined above, to find out if a number is a happy number or not, always ends in a cycle. If the number is a happy number, 
the process will be stuck in a cycle on number ‘1,’ and if the number is not a happy number then the process will be stuck in a cycle with a set 

of numbers. As we saw in Example-2 while determining if ‘12’ is a happy number or not, our process will get stuck in a cycle with the following 
numbers: 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

We saw in the LinkedList Cycle problem that we can use the Fast & Slow pointers method to find a cycle among a set of elements. 
As we have described above, each number will definitely have a cycle. Therefore, we will use the same fast & slow pointer strategy to find 
the cycle and once the cycle is found, we will see if the cycle is stuck on number ‘1’ to find out if the number is happy or not.

'''


def find_happy_number(num):
    fast,slow = num,num
    while True:
        slow = find_sq(slow)     # slow pointer
        fast = find_sq(find_sq(fast))  # fast pointer
        if slow == fast:
            break
    return slow == 1


def find_sq(num):      #take each digit square it and them add it
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit * digit
        num //= 10
    return sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
