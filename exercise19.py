import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.cnet.com/reviews/thinkpad-x1-carbon-7th-gen-review/'
r = requests.get(url)
file = open('web/log.log','w')

# print(timeit.timeit(BeautifulSoup(r.text, "lxml")))
# start_time = time.time()

soup = BeautifulSoup(r.text, "lxml")
# soup = BeautifulSoup(r.text, "html.parser")

# end_time = time.time()
# print(end_time-start_time)
# print(soup)
containers = soup.find_all("article")

for element in containers:
    print(element.text)
    if hasattr(element,'href'):
        print(element['href'])
        file.write(element.text + '\n')
    else:
        print('NONE')
file.close()

#0.032446861267089844
#0.030868053436279297