from random import randrange

def remove_duplicate(lst):
    new_lst = []
    [new_lst.append(x) for x in lst if x not in new_lst]
    # new_lst = []
    # for x in lst:
    #     if x not in new_lst:
    #         new_lst.append(x)
    return new_lst


def remove_duplicate_set(lst):
    return list(set(lst))

a = [randrange(1,100) for x in range(1,randrange(10,40))]

print(sorted(a))
print(sorted(remove_duplicate(a)))
print(sorted(remove_duplicate_set(a)))
