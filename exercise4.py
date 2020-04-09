########################  exercise 4 (Divisors)
# !!! best
num = int(input("choose a number: "))
x = list(range(1, num))
print([i for i in x if num % i == 0])

# --- my
# number = int(input())
#
# for elem in range(1,number+1):
#     if number % elem == 0:
#         print(elem)
#

