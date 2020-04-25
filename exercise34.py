import json

# info_about_me = {
#     "name": "Michele",
#     "has_a_dog": False
# }
#
# with open('addon/test_json.json','w') as file:
#     json.dump(info_about_me,file)

with open('addon/test_json.json', "r+") as f:
    info = json.load(f)

for names in info:
    print(names)

new_name = input('Input new name:')
new_birthday = input('Input birthday:')

info[new_name] = new_birthday

for names in info:
    print(names)

with open('addon/test_json.json', "w") as f:
    json.dump(info,f)
