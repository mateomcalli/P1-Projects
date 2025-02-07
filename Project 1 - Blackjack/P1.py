# Project 1: Blackjack

import p1_random as p1
rng = p1.P1Random()
game = 0
cards = []

def logic(num): # will process rng, turn it into cards with names, ids, and values
    if num == 1:
        return 'ACE', 1
    elif num == 11:
        return 'JACK', 10
    elif num == 12:
        return 'QUEEN', 10
    elif num == 13:
        return 'KING', 10
    else:
        return str(num), num

while True:
    game += 1
    print(f'START GAME #{game}\n')
    num1 = rng.next_int(13) + 1
    card, val1 = logic(num1)
    cards.append(card)
    print(f'Your card is a {card}!')
    print(f'Your hand is: {val1}\n')
    print('1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n')
    option = input('Choose an option: ')

    if option == '1':
        num2 = rng.next_int(13) + 1
        card, val2 = logic(num2)
        cards.append(card)
        print(f'Your card is a {card}!')
        print(f'Your hand is: {val1 + val2}!\n')
    elif option == '2':
        pass


