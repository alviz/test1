from random import randrange, sample
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = [randrange(1,100) for x in range(1,randrange(10,40))]
# b = [randrange(1,100) for x in range(1,randrange(10,40))]

def return_number(a):
    if len(a) > 1:
        return [a[0],a[-1]]
    else:
        return []

a = sample(range(1,30), 2)
print(len(a))
print(return_number(a))

