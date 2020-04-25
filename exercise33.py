
birthdays = {'Albert Einstein': '22/01/1905',
             'Benjamin Franklin': '10/10/1925',
             'Ada Lovelace': '11/11/1911',}

for name in birthdays.keys():
    print(name)

while True:
    name = input('Choose name: ')
    if name in birthdays.keys():
        print(f'{name}\'s birthday is {birthdays[name]}')
    elif name == 'exit':
        break
    else:
        print(f'{name}\'s birthday not found!')
