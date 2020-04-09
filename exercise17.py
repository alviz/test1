import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

#print(soup)
titles = soup.find_all("h2")

for story_heading in titles:
    print(story_heading.text)
