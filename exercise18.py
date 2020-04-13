from random import randint,choice,sample

def game(game_number, user_number):
    if game_number == user_number:
        print('You are done!')
        return True
    bulls = 0
    cows = 0
    for id, elem in enumerate(user_number):
        if elem == game_number[id]:
            cows = cows + 1
        elif elem in game_number:
            bulls = bulls + 1
    print(f'Cows: {cows} and Bulls: {bulls}')
    return False  

if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game!")
    game_number = ''.join(map(str,sample(range(1, 10), 4)))
    attempts = 0
    #print(game_number)
    # user_num = input("Enter a number: ")
    while True:
        user_number = input('Your guess(4 numbers):')
        if len(user_number) == 4 and user_number.isdigit():
            attempts = attempts + 1
            if game(game_number, user_number):
                break
        else:
            print("Incorrect number!")
    print('Number of attempts: ' + str(attempts))
