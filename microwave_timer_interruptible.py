reverse_timer = int(input('Set the countdown time: '))
for time in range(reverse_timer, -1, -1):
    print('Time left:', time, 'seconds')
    
    stop = input('Do you want to stop the heating? (1 - Yes, 0 - No): ')
    
    if stop == '1':
        print('Your food is ready, you can take it. The timer was stopped at', time, 'seconds.')
        break
    elif stop == '0':
        print('Your food is still heating, be careful it\'s hot!')
    else:
        print('Invalid input. Continuing countdown...')
