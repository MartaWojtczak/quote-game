# guessing game, where you can guess author's name
from bs4 import BeautifulSoup
from time import sleep
from random import choice
import requests
import csv

# quotes, authors, bio links from all pages
i = 1
searched_quotes = []
while i:
    http = 'https://quotes.toscrape.com/page/' + str(i) + '/'
    page_result = requests.get(http)
    soup = BeautifulSoup(page_result.text, "html.parser")
    all_quotes = soup.find_all(class_="quote")
    for q in all_quotes:
        quote = q.find(class_="text").get_text()
        author = q.find(class_="author").get_text()
        bio_link = q.find("a")["href"]
        searched_quotes.append(
            {"quote": quote, "author": author, "bio_link": bio_link})
    if soup.find(class_="next"):
        i += 1
        sleep(choice([1, 2, 3, 4, 5]))
    else:
        break

# from bio links info
bio_info = []
authors = set()
for dictionary in searched_quotes:
    authors.add(dictionary["bio_link"])

for bio in authors:
    basic_http = 'https://quotes.toscrape.com/'
    bio_result = requests.get(basic_http + bio)
    soup = BeautifulSoup(bio_result.text, "html.parser")
    author_info = soup.find(class_='author-details').find('p')
    born_date = author_info.find(class_='author-born-date').get_text()
    born_place = author_info.find(class_='author-born-location').get_text()
    bio_info.append(
        {'author_link': bio, 'born_date': born_date, 'born_place': born_place})
    sleep(choice([1, 2, 3, 4, 5]))

with open("quotes.csv", "w", newline='', encoding='utf-8') as quotes_file:
    names = ['quote', 'author', 'bio_link']
    quotes_writer = csv.DictWriter(quotes_file, fieldnames=names)
    quotes_writer.writeheader()
    for q in searched_quotes:
        quotes_writer.writerow(q)


with open("bio.csv", "w", newline='', encoding='utf-8') as bio_file:
    names = ['author_link', 'born_date', 'born_place']
    bio_writer = csv.DictWriter(bio_file, fieldnames=names)
    bio_writer.writeheader()
    for q in bio_info:
        bio_writer.writerow(q)
