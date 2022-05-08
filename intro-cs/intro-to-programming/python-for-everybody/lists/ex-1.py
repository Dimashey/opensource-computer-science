def chop(l):
    l.pop(0)
    l.pop(len(l) - 1)

def middle(l):
    return l[1:len(l) - 1]


list1 = [1,2,3]

chop(list1)
print(f"chop: {str(list1)}")

list2 = [4,5,6]

list3 = middle(list2)

print(f"prev: {str(list2)}")

print(f"middle: {str(list3)}")
