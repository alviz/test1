from random import randrange, randint

size = 1000
goal = randint(1,size)
# goal = 626
print(goal)

attempts = 0
guesses_array = [i for i in range(1,size)]

while True:
    attempts = attempts + 1
    guess = int(len(guesses_array) / 2)
    print('is it ' + str(guesses_array[guess]) + '?')
    if guesses_array[guess] == goal:
        print('you won!')
        break

    user_input = input('Answer [low/high]: ')
    if user_input == 'low':
        guesses_array = guesses_array[:guess]
    else:
        guesses_array = guesses_array[guess:]


print("Number of attempts is " + str(attempts))