import pprint
import time
# with open('addon/nameslist.txt','r') as file_name:
#     fcontent = file_name.read()
#
# usernames = {}
#
# for element in fcontent.split('\n'):
#     element = element.strip()
#     if element in usernames.keys():
#         usernames[element] += 1
#     else:
#         usernames[element] = 1
#
# pprint(usernames)

start_time = time.time()

categories = {}
with open('addon/Training_01.txt','r') as file_name:
    for line in file_name:
        line = line.strip()
        splitter = line.rfind('/')
        category = line[3:splitter]
        if category in categories.keys():
            categories[category] += 1
        else:
            categories[category] = 1

end_time = time.time()
print(end_time - start_time)

print('readlines done')


start_time = time.time()

categories = {}
with open('addon/Training_01.txt','r') as file_name:
    file_content = file_name.read().split('\n')

for line in file_content:
    line = line.strip()
    splitter = line.rfind('/')
    category = line[3:splitter]
    if category in categories.keys():
        categories[category] += 1
    else:
        categories[category] = 1

end_time = time.time()
print(end_time - start_time)

print('read done')

# for element in categories.items():
#     print(element)
