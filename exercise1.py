from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


username = input("Input username:")
age = int(input("Input age:"))

output = f'{username} left {100 - age} years till 100 and it will {currentYear - age + 100} year'
print(output)

repeater = int(input('Input number of repeats: '))
print(repeater * (output + '\n'))

