boys = int(input('Enter the number of boys: '))
girls = int(input('Enter the number of girls: '))
answer = ''

if (boys > 2 * girls) or (girls > 2 * boys):
    print('No solution!')
elif boys >= girls:
    seats = boys - girls
    for _ in range(seats):
        answer += 'BGB'
    for _ in range(girls - seats):
        answer += 'BG'
else:
    seats = girls - boys
    for _ in range(seats):
        answer += 'GBG'
    for _ in range(boys - seats):
        answer += 'GB'

print(answer)
