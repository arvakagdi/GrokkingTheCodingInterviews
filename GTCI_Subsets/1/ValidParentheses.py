'''
Problem Statement #
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
'''

from collections import deque

class ParathesesString:
    def __init__(self,str,opencount,closecount):
        self.str = str
        self.opencount = opencount
        self.closecount = closecount


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParathesesString("",0,0))
    while queue:
        ps = queue.popleft()

        if ps.opencount == num and ps.closecount == num:
            result.append(ps.str)
        else:
            if ps.opencount < num:
                queue.append(ParathesesString(ps.str + '(', ps.opencount + 1, ps.closecount))
            
            if ps.opencount > ps.closecount:
                queue.append(ParathesesString(ps.str + ')', ps.opencount, ps.closecount + 1))
   
    return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))
main()


'''
Time complexity #
Let’s try to estimate how many combinations we can have for ‘N’ pairs of balanced parentheses. If we don’t care for the ordering - that ) can only come after ( - 
then we have two options for every position, i.e., either put open parentheses or close parentheses. This means we can have a maximum of 2^N combinations.
Because of the ordering, the actual number will be less than 2^N

If you see the visual representation of Example-2 closely you will realize that, in the worst case, it is equivalent to a binary tree, 
where each node will have two children. This means that we will have 2^N leaf nodes and 2^N-1 intermediate nodes. 
So the total number of elements pushed to the queue will be 2^N + 2^N-1,which is asymptotically equivalent to O(2^N). 
While processing each element, we do need to concatenate the current string with ( or ). This operation will take O(N),
so the overall time complexity of our algorithm will be O(N*2^N). This is not completely accurate but reasonable enough to be presented in the interview.

The actual time complexity ( O(4^n/\sqrt{n}) is bounded by the Catalan number and is beyond the scope of a coding interview. See more details here.

Space complexity #
All the additional space used by our algorithm is for the output list. Since we can’t have more than O(2^N)combinations, 
the space complexity of our algorithm is O(N*2^N).


'''