
array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in (num for num in array if num < 5):
    print(item)

test_num = int(input('Test num: '))

for item in (num for num in array if num < test_num):
    print(item)
