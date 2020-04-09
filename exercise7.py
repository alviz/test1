from random import randrange

a = []
a = [randrange(1,100) for x in range(1,30)]

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(a)

b = [x for x in sorted(a) if x % 2 == 0]

print(b)