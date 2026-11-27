import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
news = soup.select(".titleline > a")
for line, new in enumerate(news[:30], start=1):
    headline = new.get_text()
    link = new.get("href")
    print(headline)
    print(link)
