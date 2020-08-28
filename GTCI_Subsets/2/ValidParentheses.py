from collections import deque

class Parantheses:
    def __init__(self,str,opencount,closecount):
        self.opencount = opencount
        self.closecount = closecount
        self.str = str

def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(Parantheses('',0,0))

    while queue:
        curr = queue.popleft()

        if curr.opencount == num and curr.closecount == num:
            result.append(curr.str)
        
        if curr.opencount < num:
            queue.append(Parantheses(curr.str + '(', curr.opencount + 1, curr.closecount))

        if curr.closecount < curr.opencount:
            queue.append(Parantheses(curr.str + ')', curr.opencount, curr.closecount+1))

    return result



def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
