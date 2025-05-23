start_of_the_segment = int(input('Enter the start of the segment: '))
end_of_the_segment = int(input('Enter the end of the segment: '))
step = int(input('Enter the step: '))

for x in range(end_of_the_segment, start_of_the_segment - 1, step):
    y = x**3 + 2*x**2 - 4*x + 1
    print('At point', x, 'the function equals', y)
