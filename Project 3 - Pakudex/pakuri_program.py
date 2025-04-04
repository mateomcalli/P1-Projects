from pakudex import Pakudex

def main():
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    found = False
    s_list = []
    while True:
        try:
            capacity = int(input('Enter max capacity of the Pakudex: '))
            if capacity <= 0:
                raise ValueError
            break
        except ValueError:
            print('Please enter a valid size.')
    pakudex = Pakudex(capacity)
    print(f'The Pakudex can hold {capacity} species of Pakuri.\n')

    while True:
        print('Pakudex Main Menu')
        print('-----------------')
        print('1. List Pakuri')
        print('2. Show Pakuri')
        print('3. Add Pakuri')
        print('4. Evolve Pakuri')
        print('5. Sort Pakuri')
        print('6. Exit\n')

        while True:
            choice = input('What would you like to do? ')
            if choice.isdigit() and int(choice) in [1,2,3,4,5,6]:
                choice = int(choice)
            else:
                print('Unrecognized menu selection!\n')
                print('Pakudex Main Menu')
                print('-----------------')
                print('1. List Pakuri')
                print('2. Show Pakuri')
                print('3. Add Pakuri')
                print('4. Evolve Pakuri')
                print('5. Sort Pakuri')
                print('6. Exit\n')
                continue
            break

        if choice == 1:
            if pakudex.species:
                print('Pakuri In Pakudex:')
                number = 1
                if s_list:
                    for _ in s_list:
                        print(f'{number}. {s_list[number-1]}')
                        number += 1
                else:
                    for p in pakudex.species:
                        print(f'{number}. {p.species}')
                        number += 1
                    print()
            else: print('No Pakuri in Pakudex yet!\n')

        elif choice == 2:
            chosen_species = input('Enter the name of the species to display: ')
            for pakuri in pakudex.species:
                if pakuri.get_species() == chosen_species:
                    found = True
                    print(f'\nSpecies: {chosen_species}')
                    print(f'Attack: {pakudex.get_stats(chosen_species)[0]}')
                    print(f'Defense: {pakudex.get_stats(chosen_species)[1]}')
                    print(f'Speed: {pakudex.get_stats(chosen_species)[2]}\n')
            if not found: print('Error: No such Pakuri!\n')

        elif choice == 3:
            try:
                if pakudex.tally == capacity:
                    raise ValueError
                to_add = input('Enter the name of the species to add: ')
                if to_add in pakudex.species:
                    print('Error: Pakudex already contains this species!\n')
                else:
                    pakudex.add_pakuri(to_add)
                    print(f'Pakuri species {to_add} successfully added!\n')
            except:
                print('Error: Pakudex is full!\n')

        elif choice == 4:
            found = False
            to_evo = input('Enter the name of the species to evolve: ')
            for pakuri in pakudex.species:
                if pakuri.get_species() == to_evo:
                    found = True
                    pakudex.evolve_species(to_evo)
                    print(f'{to_evo} has evolved!\n')
            if not found: print('Error: No such Pakuri!\n')

        elif choice == 5:
            s_list = pakudex.sort_pakuri()
            print('Pakuri have been sorted!\n')

        elif choice == 6:
            print('Thanks for using Pakudex! Bye!')
            break

        else: print('Unrecognized menu selection!\n')

if __name__ == '__main__':
    main()

