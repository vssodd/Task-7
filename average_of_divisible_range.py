number_a = int(input('Enter number a: '))
number_b = int(input('Enter number b: '))
number_c = int(input('Enter number c: '))
total = 0
count = 0

for arithmetic_mean in range(number_a, number_b):
    if arithmetic_mean % number_c == 0:
        total += arithmetic_mean
        count += 1

if count > 0:
    avg = total // count
    print('Average of all numbers in range', number_a, 'to', number_b, 'divisible by', number_c, ':')
    print('Answer:', avg)
else:
    print('No numbers in the range', number_a, 'to', number_b, 'are divisible by', number_c)
