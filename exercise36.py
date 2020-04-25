import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

source_data = 'addon/test_json.json'
graph_page = 'addon/bdays.html'

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
x = []
y = []

with open(source_data, "r+") as f:
    info = json.load(f)

for bdate in info.values():
    list_of_monthes.append(dic_monthes[int(bdate.split('/')[1])])

for x_item, y_item in Counter(list_of_monthes).items():
    x.append(x_item)
    y.append(y_item)

output_file(graph_page)

graph = figure(x_range=[value for value in dic_monthes.values()],
               plot_width=800,
               plot_height=400,
               title='Birthdays'
               )

graph.vbar(x=x, top=y, width=0.5)

show(graph)