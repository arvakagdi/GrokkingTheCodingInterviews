def cyclic_equiv(list1,list2):
    if len(list1) != len(list2):
        return False

    n = len(list1)
    i,j = 0,0

    while i < n and j < n:
        k = 1

        while k <= n and list1[(i + k) % n] == list2[(j + k) % n]:
            k+=1
        if k>n:
            return True
        
        if list1[(i + k) % n] > list2[(j + k) % n]:
            i += k
        else:
            j +=k 
    return False



def rot(l1,l2):
    from collections import deque
    if l1 == l2:
        return True
    # if length is different we cannot get a match
    if len(l2) != len(l1):
        return False
    # if any elements are different we cannot get a match
    if set(l1).difference(l2):
        return False
    l2,l1 = deque(l2),deque(l1)
    for i in range(len(l1)):
        l2.rotate() # l2.appendleft(d.pop()) 
        if l1 == l2:
            return True
    return False


def main():
    a = [3,1,2,3,4]   
    b =[3,4,3,1,2]   
    print(rot(a,b))
    
    b =[3,4,3,2,1]    
    print(rot(a,b))
    
    b =[3,4,3,2]    
    print(rot(a,b))
    
    print(rot([1,2,3],[1,2,3]))
    print(rot([3,1,2],[1,2,3]))


main()
