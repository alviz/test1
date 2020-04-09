#######################  exercise 8 (Rock-Paper-Scissors game)

game = ['Rock', 'Scissors', 'Paper']
gamer1 = input('Gamer 1 name: ')
gamer2 = input('Gamer 2 name: ')

while True:
    first = 0
    second = 0
    print('\n')

    for index,val in enumerate(game):
        print (f'{index+1}:{val}')

    while not first:
        first = int(input(f'{gamer1} chooses: '))
        if first not in range(1,4):
            print('Try again! Allowed only 1,2 or 3')
            first = 0
    while not second:
        second = int(input(f'{gamer2} chooses: '))
        if second not in range(1,4):
            second = 0

    print(f'{game[first-1]} vs {game[second-1]}')

    if first == second:
        print('Nobody won!')
    elif (first == 1 and second == 2) or \
            (first == 2 and second == 3) or \
            (first == 3 and second == 1):
        print(f'{gamer1} won!')
    else:
        print(f'{gamer2} won!')

    if input('Continue game?[y/n] ').lower() != 'y':
        break
