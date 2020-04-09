from random import randrange, randint

goal = randint(1,10)
# goal = randrange(1,10)
attempts = 0
print(goal)

while True:
    user_input = input('Input number: ')
    if user_input == "exit":
        break
    attempts = attempts + 1
    user_input = int(user_input)
    if user_input < goal:
        print("Too low")
        continue
    elif user_input > goal:
        print("Too high")
        continue
    else:
        print("You are right!")
        break

print("Number of attempts is " + str(attempts))