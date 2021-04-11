list1 = []
list2 = []
def mul1():
    global list1
    for i in range(1000, 100 , -1):
        for j in range(1000, 100 ,-1):
            q = i*j
            list1.append(q)
    return(list1)

print(mul1())

def isPal():
    global list2
    for w in list1:
        w = str(w)
        h = w[::-1]
        if w == h:
          list2.append(int(h))
    return list2

print(max(isPal()))

   
   