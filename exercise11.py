########################  exercise 4 (Divisors)
# !!! best

def input_num(help_text = 'Input a number: '):
    return int(input(help_text))

num = input_num('test: ')
x = list(range(1, num))

print([i for i in x if num % i == 0])

prime_list = []
for z in x:
    if len([i for i in range(1,z) if z % i == 0]) == 1:
        prime_list.append(z)

print("Prime list from 1 to " + str(num) + ": ")
print(prime_list)
# --- my
# number = int(input())
#
# for elem in range(1,number+1):
#     if number % elem == 0:
#         print(elem)
#

