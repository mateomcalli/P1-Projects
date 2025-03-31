import pakudex
import pakuri

def main():
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    while True:
        capacity = input('Enter max capacity of the Pakudex: ')
        if not isinstance(capacity, int):
            print('Please enter a valid size.')
            continue
        else: break
    # pkdx = pakudex(capacity)
    print(f'The Pakudex can hold {capacity} species of Pakuri.\n')

    print('Pakudex Main Menu')
    print('-----------------')
    print('1. List Pakuri')
    print('2. Show Pakuri')
    print('3. Add Pakuri')
    print('4. Evolve Pakuri')
    print('5. Sort Pakuri')
    print('6. Exit')

    choice = int(input('What would you like to do?'))

    if choice == 1:
        pass
