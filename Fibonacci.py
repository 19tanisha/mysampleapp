def Series(a):
    n = [0, 1]
    while n[-1] < a:
        n.append(n[-1]+n[-2])
    return n

def Even(a):
    m = Series(a)
    b = [i for i in Series(a) if i % 2 == 0]
    return b
result = Even(10)
print(result)
