game_test = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

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


def calc_nums(lst):
    new_dic = {'0':0, '1':0, '2':0}
    for elem in lst:
            new_dic[str(elem)] += 1

    return new_dic


def checks(lst):
    for row in lst:
        result = calc_nums(row)
        if result['1'] == 3:
            return(1)
        elif result['2'] == 3:
            return(2)
        else:
            return(0)

def game(game_lst):
    check_row = checks(game_lst)
    check_col = checks(transpose(game_lst))
    check_diag = checks(transpose_diag(game_lst))

    if check_row:
        print('First won!' if check_row == 1 else 'Second won!')
    elif check_col:
        print('First won!' if check_col == 1 else 'Second won!')
    elif check_diag:
        print('First won!' if check_diag == 1 else 'Second won!')
    else:
        print('Nobody won!')

game(winner_is_also_1)
#
# for row in game:
#     result = calc_nums(row)
#     if result['1'] == 3: print("First won!")
#     if result['2'] == 3: print("Second won!")
#
# for row in transpose(game):
#     result = check_nums(row)
#     if result['1'] == 3: print("First won!")
#     if result['2'] == 3: print("Second won!")
#
# for row in transpose_diag(game):
#     result = check_nums(row)
#     if result['1'] == 3: print("First won!")
#     if result['2'] == 3: print("Second won!")

