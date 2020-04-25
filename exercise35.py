import json
from collections import Counter

dic_monthes = { 1:"January",
                2:"February",
                3:"March",
                4:"April",
                5:"May",
                6:"June",
                7:"July",
                8:"August",
                9:"September",
                10:"October",
                11:"November",
                12:"December" }

list_of_monthes = []

with open('addon/test_json.json', "r+") as f:
    info = json.load(f)

for bdate in info.values():
    list_of_monthes.append(dic_monthes[int(bdate.split('/')[1])])

print(Counter(list_of_monthes))
