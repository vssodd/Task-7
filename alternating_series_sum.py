N = int(input('Enter number N: '))
elem = sum((-1) ** n * 1 / (2 ** n) for n in range(N))
print('The sum is:', elem)
