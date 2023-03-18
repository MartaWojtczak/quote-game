# quote-game
Web scraping project where you download quotes from web: https://quotes.toscrape.com/. Quotes are used to build guessing game with hints. Give it a try! Built with help and guidance of Colt Steele's Python Bootcamp

## project content

- guess_quote_download_data.py: script downloading data from https://quotes.toscrape.com/ to csv files. There are two types of data, quotes saved in quotes.csv and authors bio data saved in a file bio.csv

- quess_quote_game.py: actual game, where you play with computer guessing who said a quote randomly chosen by computer. You have 4 tries and 3 clues after each try. After finishing one round you can play again or finish the game. 

- quotes.csv: csv file containing quote, author and bio link to authors bio
 
- bio.csv: csv file containing author link, born date and born place of an author

## how to play

Open quess_quote_game.py and enjoy :) If you want the newest data from a website, before starting a game please run guess_quote_download_data.py. It will overwrite csv files with new data from the website. 
