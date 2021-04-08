def primemum(a):
    number = []
    for x in range(2, int(a)):
        i = 0
        if a % x == 0:
            for a in range(1, int(a)):
                if x % a == 0:
                    i = i + 1
            if i == 1:
                number.append(a)
    print(max(number))

primemum(600851475143)