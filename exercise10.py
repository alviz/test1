from random import randrange, sample
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = [randrange(1,100) for x in range(1,randrange(10,40))]
# b = [randrange(1,100) for x in range(1,randrange(10,40))]

a = sample(range(1,30), 12)
b = sample(range(1,30), 16)

c = set()

print(a)
print(b)

c = [x for x in a if x in b]

print(sorted(c))

