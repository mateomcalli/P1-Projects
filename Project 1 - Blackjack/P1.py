# Project 1: Blackjack

import p1_random as p1
rng = p1.P1Random()

new_game = True
error = False
games = 0
wins = 0
ties = 0
losses = 0
val = 0
cards = []

def logic(num): # will process rng, turn it into cards with names and values
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
    if not error:
        if new_game:
            val = 0
            games += 1
            print(f'START GAME #{games}')
        num = rng.next_int(13) + 1
        card, new_val = logic(num)
        cards.append(card)
        val += new_val
        print(f'\nYour card is a {card}!')
        print(f'Your hand is: {val}\n')
        if val == 21:
            new_game = True
            print('BLACKJACK! You win!\n')
            wins += 1
            continue
        elif val > 21:
            new_game = True
            print('You exceeded 21! You lose.\n')
            losses += 1
            continue
    error = False
    print('1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n')
    option = input('Choose an option: ')

    if option == '1': # if user wants another card run the loop back
        new_game = False
        continue

    elif option == '2': # dealer logic
        dealer = rng.next_int(11) + 16
        print(f"\nDealer's hand: {dealer}\nYour hand is: {val}\n")
        if dealer <= 21 and dealer > val:
            new_game = True
            print('Dealer wins!\n')
            losses += 1
            continue
        elif dealer <= 21 and val > dealer:
            new_game = True
            print('You win!\n')
            wins += 1
            continue
        elif dealer > 21:
            new_game = True
            print('You win!\n')
            wins += 1
            continue
        elif dealer == val:
            new_game = True
            print("It's a tie! No one wins!\n")
            ties += 1
            continue
    elif option == '3': # prints stats
        error = True
        games -= 1
        print(f'\nNumber of Player wins: {wins}\nNumber of Dealer wins: {losses}\nNumber of tie games: {ties}\nTotal # of games played is: {games}\nPercentage of Player wins: {(wins/games) * 100:.1f}%\n')
    elif option == '4':
        break
    else: # invalid input case
        error = True
        print('Invalid input!\n\nPlease enter an integer value between 1 and 4.')
        continue
