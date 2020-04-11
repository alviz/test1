import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

#print(soup)
titles = soup.find_all("p")

for story_heading in titles:
    print(story_heading.text)
