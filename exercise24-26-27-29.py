game_field = [['','',''],
              ['','',''],
              ['','','']]

game_field_test = [['x','x','0'],
              ['0','x','0'],
              ['x','0','x']]

def print_field(game_field):
    for row in range(3):
        print(' ' + '--- ' * 3)
        print('|', end='')
        for column in range(3):
            if game_field[row][column] == '':
                print('   |', end='')
            else:
                print(' ' + game_field[row][column] + ' |', end = '')
        print('')
    print(' ' + '--- ' * 3)

def transpose(old_list):
    new_list = []
    for column in range(len(old_list[0])):
        new_list_row = []
        for row in range(len(old_list)):
            new_list_row.append(old_list[row][column])
        new_list.append(new_list_row)

    return new_list


def transpose_diag(old_list):
    new_list = []
    new_list_diag = []
    for row in range(len(old_list)):
        new_list_diag.append(old_list[row][row])

    new_list.append(new_list_diag)

    new_list_diag = []
    column = 0
    for row in range(len(old_list)-1,-1,-1):
        new_list_diag.append(old_list[row][column])
        column += 1

    new_list.append(new_list_diag)

    return new_list


def checks(lst,char):
    for row in lst:
        counter = 0
        for elem in row:
            if elem == char:
                counter += 1
        if counter == 3:
            return True
    return False


def game(game_field, char):
    if checks(game_field,char) or checks(transpose(game_field),char) or checks(transpose_diag(game_field),char):
        return True
    else:
        return False

def is_full (game_fiels):
    filled = 0
    for row in range(3):
        for col in range(3):
            if game_field[row][col]:
                filled += 1
    return True if filled == 9 else False

def input_value(game_field, char):
    availability = True
    while availability:
        row = int(input(f'Please input ROW for {char}: ' )) - 1
        col = int(input(f'Please input COLUMN for {char}: ')) - 1
        if row not in range(0,3) or col not in range(0,3):
            print("Allowed value 1,2 or 3!")
        elif game_field[row][col]:
            print("It's busy. Try again!")
        else:
            game_field[row][col] = char
            availability = False

    return game_field


if __name__=="__main__":
    print_field(game_field)
    char = 'X'
    while True:
        game_field = input_value(game_field, char)
        print_field(game_field)
        if game(game_field,char):
            print(char + 's are won!')
            break
        if is_full(game_field):
            print('Game Finished! Nobody won!')
            break
        char = '0' if char == 'X' else 'X'


