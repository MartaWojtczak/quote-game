#guessing game, where you can guess author's name
from bs4 import BeautifulSoup
from time import sleep
from random import choice 
import requests

#quotes, authors, bio links from one page
searched_quotes = []
http = 'https://quotes.toscrape.com/'
page_result = requests.get(http)
soup = BeautifulSoup(page_result.text, "html.parser")
all_quotes = soup.find_all(class_ = "quote")
for q in all_quotes:
    quote = q.find(class_ = "text").get_text()
    author = q.find(class_ = "author").get_text()
    bio_link = q.find("a")["href"]
    searched_quotes.append({"quote":quote, "author": author, "bio_link": bio_link})

print(searched_quotes)