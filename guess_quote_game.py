import csv
import random

# download data from flat files
def reader(filename):
    with open(filename, encoding='utf-8') as file:
        r = csv.DictReader(file)
        return list(r)

quotes = reader("quotes.csv")
bio = reader("bio.csv")

# play game
def play_game():
    random_quote = random.choice(quotes)
    for b in bio:
        if b['author_link'] == random_quote['bio_link']:
            random_bio = b
    quote_to_guess = random_quote['quote']
    quote_answer = random_quote['author']
    bio_date = random_bio['born_date']
    bio_place = random_bio['born_place']
    counter = 4
    answer = ''
    # start guessing
    print(f'Hey! Please guess who said that: {quote_to_guess}')
    while counter > 0:
        print(f'You have {counter} guesses remaining')
        answer = input()
        counter -= 1
        if answer.lower() == quote_answer.lower():
            print('Correct!')
            break
        elif counter > 0:
            if counter == 3:
                hint = f'Author born in {bio_place} at {bio_date}'
            elif counter == 2:
                hint = f'first letter of a name is {quote_answer[0]}'
            elif counter == 1:
                hint = f'second letter of a name is {quote_answer[1]}'
            print(f"here is a hint: {hint}")
        else:
            print(f'You loose, here is the answer: {quote_answer}')
    #do you want to play again
    play_again = ''
    while play_again not in ('y', 'n'):
        print('Do you want to play again? (y/n)')
        play_again = input().lower()[0]
    if play_again == 'y':
        play_game()
    return 'bye!'

play_game()