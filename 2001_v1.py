from Dice import roll_the_dice

usr1_points = 0
usr2_points = 0
usr2 = 0  # if False its computer, if True its human
use_dice = 'D6'
num_of_dice = '2'

round = 1

while usr2 is True or usr2 is False:
    mode = input('\nWpisz 0 jeśłi chcesz zagrać z komputerem, lub 1 jeśli gra ma być dla 2 osób, a następnie naciśnij enter:    ')
    if mode == '1':
        usr2 = True
        break
    elif mode == '0':
        usr2 = False
        break
    else:
        print('Niewłaściwy wybór. Sróbuj jeszcze raz\n')

while usr1_points < 2001 and usr2_points < 2001:
    print(f'\nRunda {round}. Gracz 1. Twoja ilość punktów to {usr1_points} Naciśnij enter aby rzucić kością')
#    input()
    rolls = roll_the_dice(use_dice)
    print(f'Wylosowałeś {rolls}. Naciśnij enter aby rzucić 2 raz')
#    input()
    rolls += roll_the_dice(use_dice)
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
        print(f'\nKomputer ma {usr2_points} punktów. Następują 2 rzuty kostką.')
        rolls = roll_the_dice(use_dice) + roll_the_dice(use_dice)
        usr2_points += rolls
        if round >= 2:
            if rolls == 7:
                usr2_points = usr2_points // 7
                print('Komputer wylosował 7 w 2 rzutach. Punty są dzielone przez 7')
            if rolls == 11:
                usr2_points *= 11
                print('Komputer wylosował 11 w 2 rzutach. Punkty są mnożone rzez 11')
        else:
            print(f'Komputer wyosował {rolls} w 2 rzutach.')
        print(f'Komputer ma {usr2_points} punktów')
    else:
        print(f'\nGracz 2. Twoja ilość punktów to {usr2_points} Naciśnij enter aby rzucić kością')
#        input()
        rolls = roll_the_dice(use_dice)
        print(f'Wylosowałeś {rolls}. Naciśnij enter aby rzucić 2 raz')
#        input()
        rolls += roll_the_dice(use_dice)
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
