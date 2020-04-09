
def fibonnaci(size):
    if size == 0:
        lst = []
    elif size == 1:
        lst = [1]
    elif size == 2:
        lst = [1,1]
    else:
        lst = [1,1]
        for x in range(2,size):
            lst.append(lst[-1]+lst[-2])
    return lst

size = int(input("input numbers: "))

print(fibonnaci(size))
