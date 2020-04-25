import random

words_dic = []
with open('addon/sowpods.txt', 'r') as file_words:
    for line in file_words:
        words_dic.append(line.strip())

# random_word = words_dic[random.randint(0,len(words_dic)-1)]
random_word = 'UNDERGROUND'
print(random_word)

user_chars = set()

goal_word = ['_' for _ in range(0,len(random_word))]

print(''.join(goal_word))
failed_attempts = 6

while True:
    user_input = input('Your guess: ').upper()

    if user_input in user_chars:
        print('Repeated, try new one!')
        continue
    else:
        user_chars.add(user_input)

    if user_input in random_word:
        for id in range(0,len(random_word)):
            if user_input == random_word[id]:
                goal_word[id] = user_input
        print(''.join(goal_word))
    else:
        print('Incorrect!')
        failed_attempts -= 1
        print('Number of failed attemts left: ' + str(failed_attempts))

        if failed_attempts == 0:
            print('You have more 6 failed attempts. Game finished!')
            break

    if '_' not in goal_word:
        print('You are win!')
        break


