import random

lst = random.sample(range(1, 1000), 30)
print(lst)

max = lst[0]
for elem in lst:
    if elem > max: max = elem

print(max)
