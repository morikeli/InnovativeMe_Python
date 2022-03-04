"""
    Developed, debugged and maintained by Mori Keli.
    Created: 28-10-2021 15:00 Thursday
    Copyright 2021 MORI KELI | ALL RIGHTS RESERVED.
"""
# Python program to manage vehicles parked in a parking lot.


def this_program():
    print('==='*30)
    print('{:^80s}'.format('--- PARKING LOT MAINTENANCE PROGRAM ---'))
    print('==='*30)
    print('{:^90s}\n{}'.format('Enter one option from the menu below. (Enter:  1 or 2 or 3)', '---'*30))
    print('Type of vehicles parked?')
    print('{}\n{}\n{}'.format('1. Big Vehicles (trucks, lorries, buses, etc)', '2. Small vehicles (sedan, coupe, sports car, minivan, etc)', '3. Both big '
        'vehicles & small vehicles'))
    print('---'*30)


this_program()
area_parking_lot = 400*150


def program_menu(option):
    print('---'*30)

    if option == 1:
        no_of_big_vehicles = int(input('Enter the number of big vehicles in the parking lot: '))

        if no_of_big_vehicles < 0:
            print('INVALID INPUT!!! Enter a positive integer. Please try again.')
            exit(0)
        elif no_of_big_vehicles == 0:
            print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
            print('Space occupied: NULL')
            print('Space left: {:,d} cm²'.format(area_parking_lot))
        else:
            space_occupied = no_of_big_vehicles*(40*15)
            space_left = area_parking_lot - space_occupied
            if no_of_big_vehicles > 100:
                print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
                print('Space occupied by big vehicles: {:,d} cm²'.format(space_occupied))
                print('Space left: {:,d} cm²'.format(space_left))
                print('Space required: at least 600 cm² for a big vehicle and 300 cm² for a small vehicle.')
            elif no_of_big_vehicles == 100:
                print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
                print('Space occupied by big vehicles: {:,d} cm²'.format(space_occupied))
                print('Space left: {:,d} cm²'.format(space_left))
                print('Space required: at least 600 cm² for big vehicles and 300 cm² for small vehicles')
            else:
                print('No. of big vehicles in the parking lot: {:d}'.format(no_of_big_vehicles))
                print('Space occupied: {:,d} cm²'.format(space_occupied))
                print('Space left: {:,d} cm²'.format(space_left))
                print('{:d} big vehicles and {:d} small vehicles can occupy the space left.'.format(int(space_left/600), int(space_left/300)))

    elif option == 2:
        no_of_small_vehicles = int(input('Enter the no. of small vehicles in the parking lot: '))
        if no_of_small_vehicles < 0:
            print('INVALID INPUT!!! Enter a positive integer. PLease try again.')
            exit(0)
        elif no_of_small_vehicles == 0:
            print('No. of small vehicles in the parking lot: {:d}'.format(no_of_small_vehicles))
            print('Space occupied: NULL')
            print('Space left: {:,d} cm²'.format(area_parking_lot))
        else:
            space_occupied = no_of_small_vehicles*(20*15)
            space_left = area_parking_lot - space_occupied
            if no_of_small_vehicles > 200:
                print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
                print("Space occupied by the small vehicles: {:,d} cm²".format(space_occupied))
                print('Space left: {:,d} cm²'.format(space_left))
                print('Space required: at least 300 cm² for small vehicles and 600 cm² for big vehicles')

            elif no_of_small_vehicles == 200:
                print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
                print('Space occupied by small vehicles: {:,d} cm²'.format(space_occupied))
                print('Space left: {:,d} cm²'.format(space_left))
                print('Space required: at least 300 cm² for small vehicles & 600 cm² for big vehicles.')

            else:
                print('No. of small vehicles in the parking lot: {:d}'.format(no_of_small_vehicles))
                print('Space occupied by small vehicles: {:,d} cm²'.format(space_occupied))
                print('Space left: {:,d} cm²'.format(space_left))
                print('{:d} small vehicles and {:d} big vehicles can occupy the space left.'.format(int(space_left/300), int(space_left/600)))

    elif option == 3:
        big_vehicles = int(input('Enter the number of big vehicles in the parking lot: '))
        space_occupied = big_vehicles*(40*15)
        space_left = area_parking_lot - space_occupied
        if big_vehicles < 0:
            print('INVALID INPUT!!! Enter a positive integer. Please try again.')
            exit(0)
        elif big_vehicles == 100:
            print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
            print('No. of big vehicles in the parking lot: {:d}'.format(big_vehicles))
            print('Space occupied: {:,d} cm²'.format(area_parking_lot))
            print('Space required: at least 600 cm² for big vehicles and 300 cm² for small vehicles.')
        elif big_vehicles > 100:
            print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
            print('No. of big vehicles in the parking lot: 100')
            print('Space occupied: {:,d} cm²'.format(space_left))
            print('Space required: at least 600 cm² for big vehicles and 300cm² for small vehicles.')
        else:
            small_vehicles = int(input('Enter the number of small vehicles in the parking lot: '))
            if small_vehicles < 0:
                print('INVALID INPUT!!! Enter a positive integer. Please try again.')
                exit(0)
            elif big_vehicles == 0 and small_vehicles == 0:
                print('No. of big vehicles: {:d}'.format(big_vehicles))
                print('No. of small vehicles: {:d}'.format(small_vehicles))
                print('Space left: {:,d} cm²'.format(area_parking_lot))
            elif small_vehicles == 200:
                print('{:^80s}'.format('*** NO SPACE LEFT!!! ***'))
                print('No. of small vehicles in the parking lot: {:d}'.format(small_vehicles))
                print('Space occupied: {:,d} cm²'.format(space_occupied))
                print('Space left: {:,d} cm²'.format(space_left))
                print('Space required: at least 300 cm² for small vehicles and 600 cm² for big vehicles.')
            else:
                if small_vehicles > big_vehicles:
                    space_occupied = (big_vehicles*(40*15)+small_vehicles*(20*15))
                    space_left = area_parking_lot - space_occupied
                    print('No. of small vehicles parked: {:d}'.format(small_vehicles))
                    print('No. of big vehicles parked: {:d}'.format(big_vehicles))
                    print('Space occupied by the vehicles: {:,d} cm²'.format(space_occupied))
                    print('Space left: {:,d}'.format(space_left))
                    print('{:d} big vehicles and {:d} small vehicles can occupy the space left.'.format(int(space_left/600), int(space_left/300)))
                elif small_vehicles > 200:
                    print('{:^80s}'.format('*** NO SPACE LEFT ***'))
                    print('No. of small vehicles parked: {:d}'.format(small_vehicles))
                    print('Space left: 0 cm²')
                    print('Space required: at 600 cm² for a big vehicle and 300 cm² for a small vehicle.')

                else:
                    space_occupied = big_vehicles*(40*15) + small_vehicles*(20*15)
                    space_left = area_parking_lot - space_occupied
                    print('No. of big vehicles in the parking lot: {:d}'.format(big_vehicles))
                    print('No. of small vehicles in the parking lot: {:d}'.format(small_vehicles))
                    print('Space occupied by the vehicles: {:,d} cm²'.format(space_occupied))
                    print('Space left: {:,d} cm²'.format(space_left))

    else:
        print('INVALID INPUT!!! Enter 1 or 2 or 3 as your option. Please try again.')
        exit(0)


program_menu(int(input('Enter your option: ')))
