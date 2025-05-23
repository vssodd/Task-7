boys = int(input('Enter the number of boys: '))
girls = int(input('Enter the number of girls: '))

if 2 * girls + 2 < boys or 2 * boys + 2 < girls:
    print('No solution')
else:
    for _ in range(boys + girls):
        if boys >= girls and boys > 0:
            print('B', end='')
            boys -= 1
            if girls >= boys and girls > 0:
                print('G', end='')
                girls -= 1
