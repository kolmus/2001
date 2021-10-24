from Dice import roll_the_dice
from random import shuffle

allowed = [
    'D3',
    'D4',
    'D6',
    'D8',
    'D10',
    'D12',
    'D20',
    'D100',
]

usr1_points = 0
usr2_points = 0
usr2 = 0  # if False its computer, if True its human
use_dice = 'D6'
num_of_dice = '2'
cor_choice = False
round = 1

while usr2 == True or usr2 == False:
    mode = input('\nWpisz 0 jeśli chcesz zagrać z komputerem, lub 1 jeśli gra ma być dla 2 osób, a następnie naciśnij enter:    ')
    if mode == '1':
        usr2 = True
        break
    elif mode == '0':
        usr2 = False
        break
    else:
        print('Niewłaściwy wybór. Sróbuj jeszcze raz\n')

while usr1_points < 2001 and usr2_points < 2001:
    print(f'\nRunda {round}. Gracz 1. Twoja ilość punktów to {usr1_points}.')
    while cor_choice == False:
        choice = input('Wybierz pierwszą kość: ')
        if choice.upper() in allowed:
            roll1 = roll_the_dice(choice)
            print(f'Wylosowałeś {roll1}.')
            cor_choice = True
        else:
            print('Wrong value or not allowed diece. Avalable types: ' + ', '.join(allowed))
    cor_choice = False

    while cor_choice == False:
        choice = input('Wybierz drugą kość: ')
        if choice.upper() in allowed:
            roll2 = roll_the_dice(choice)
            print(f'Wylosowałeś {roll2}.')
            cor_choice = True
        else:
            print('Wrong value or not allowed diece. Avalable types: ' + ', '.join(allowed))

    cor_choice = False
    rolls = roll1 + roll2
    usr1_points += rolls
    if round >= 2:
        if rolls == 7:
            usr1_points = usr1_points // 7
            print('Wylosowałeś 7 w 2 rzutach. Twoje punty są dzielone przez 7.')
        if rolls == 11:
            usr1_points *= 11
            print('Wylosowałeś 11 w 2 rzutach. Twoje punkty są mnożone rzez 11.')
    else:
        print(f'Wylosowałeś {rolls} w 2 rzutach.')
    print(f'Masz {usr1_points} punktów')

    if usr1_points >= 2001:
        break

    if usr2 is False:
        print(f'\nKomputer ma {usr2_points} punktów. Komputer wybiera pierwszą kość i rzuca.')
        shuffle(allowed)
        choice = allowed[0]
        roll1 = roll_the_dice(choice)
        print(f'Wynik rzutu kostką {choice} to: {roll1}')
        shuffle(allowed)
        choice = allowed[0]
        roll2 = roll_the_dice(choice)
        print(f'Komputer wybrał i rzucił drugą kostką {choice} i otrzymał {roll2} punktów')
        rolls = roll1 + roll2
        usr2_points += rolls

        if round >= 2:
            if rolls == 7:
                usr2_points = usr2_points // 7
                print('Komputer wylosował 7 w 2 rzutach. Punty są dzielone przez 7.')
            if rolls == 11:
                usr2_points *= 11
                print('Komputer wylosował 11 w 2 rzutach. Punkty są mnożone rzez 11.')
        else:
            print(f'Komputer wyosował {rolls} w 2 rzutach.')
        print(f'Komputer ma {usr2_points} punktów.')

    else:
        print(f'\nGracz 2. Twoja ilość punktów to {usr2_points}.')
        while cor_choice == False:
            choice = input('Wybierz pierwszą kość: ')
            if choice.upper() in allowed:
                roll1 = roll_the_dice(choice)
                print(f'Wylosowałeś {roll1}.')
                cor_choice = True
            else:
                print('Wrong value or not allowed diece. Avalable types: ' + ', '.join(allowed))
        cor_choice = False
        while cor_choice == False:
            choice = input('Wybierz drugą kość: ')
            if choice.upper() in allowed:
                roll2 = roll_the_dice(choice)
                print(f'Wylosowałeś {roll2}.')
                cor_choice = True
            else:
                print('Wrong value or not allowed diece. Avalable types: ' + ', '.join(allowed))
        cor_choice = False
        rolls = roll1 + roll2
        usr2_points += rolls
        if round >= 2:
            if rolls == 7:
                usr2_points = usr2_points // 7
                print('Wylosowałeś 7 w 2 rzutach. Twoje punty są dzielone przez 7.')
            if rolls == 11:
                usr2_points *= 11
                print('Wylosowałeś 11 w 2 rzutach. Twoje punkty są mnożone rzez 11.')
        else:
            print(f'Wylosowałeś {rolls} w 2 rzutach.')
        print(f'\nMasz {usr2_points} punktów\n')
    if usr2_points >= 2001:
        break
    round += 1


if usr1_points > usr2_points:
    print(f'Gratulacje!!! Gracz 1 wygrał z {usr1_points} punktami.')
elif usr2_points > usr1_points:
    if usr2 is False:
        print(f'Komputer wygrał z {usr2_points} punktami.')
    elif usr2 is True:
        print(f'Gratulacje!!! Gracz 2 wygrał z {usr2_points} punktami.')
