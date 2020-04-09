from random import randint,choice
import string

def gen_password(size, pwd_level):
    password = ""
    for _ in range(1,size):
        if pwd_level == 1:
            password = password + choice(string.ascii_lowercase)
        elif pwd_level == 2:
            password = password + choice(string.ascii_lowercase + string.ascii_uppercase)
        elif pwd_level == 3:
            password = password + choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        else:
            password = password + choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    return password


pwd_size = int(input('size of password: '))
pwd_level_list = ['1:Lower Letters', '2:Upper Letters', '3:Numbers', '4:Symbols']

for pwd_line in pwd_level_list:
    print(pwd_line)

pwd_level = int(input('Password straight[1-4]: '))

while True:
    print("Generated Password: " + gen_password(pwd_size,pwd_level))
    if input("Repeat?[y/n] ") == 'n':
        break


# from random import randint,choice
# import string
#
# MIN_PWD_LENGHT = 5
#
# def randomUpperLetters():
#     chars_list = 'ABCDEFGHIGKLMNOPQRSTUVXYZW'
#     return chars_list[randint(0,len(chars_list) - 1)]
#
# def randomLowerLetters():
#     chars_list = 'abcdefghijklmnopqrstuvxyzw'
#     return chars_list[randint(0,len(chars_list) - 1)]
#
# def randomSymbols():
#     symbols_list = '!@#$%^&*()<>?{}|'
#     return symbols_list[randint(0, len(symbols_list) - 1)]
#
# def randomNum():
#     return str(randint(1, 9))
#
#
# def gen_password(size, pwd_level):
#     password = ""
#     for i in range(1,size):
#         if pwd_level == 1:
#             password = password + randomLowerLetters()
#         elif pwd_level == 2:
#             password = password + choice(randomLowerLetters() + randomUpperLetters())
#         elif pwd_level == 3:
#             password = password + choice(randomLowerLetters() + randomUpperLetters() + randomNum())
#         else:
#             password = password + choice(randomLowerLetters() + randomUpperLetters() + randomNum() + randomSymbols())
#     return password
#
#
# pwd_size = int(input('size of password: '))
# pwd_level_list = ['1:Lower Letters', '2:Upper Letters', '3:Numbers', '4:Symbols']
#
# for pwd_line in pwd_level_list:
#     print(pwd_line)
#
# pwd_level = int(input('Password straight[1-4]: '))
#
# while True:
#     print("Generated Password: " + gen_password(pwd_size,pwd_level))
#     if input("Repeat?[y/n] ") == 'n':
#         break
#
#
#
#


