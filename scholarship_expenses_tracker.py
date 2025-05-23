educational_grant = int(input('Enter the scholarship amount: '))
expenses = int(input('Enter living expenses: '))
parents = 0

for month in range(1, 11):
    if month != 1:
        expenses += expenses // 100 * 3  # increase expenses by 3%
    difference = educational_grant - expenses
    if difference < 0:
        parents += -difference
    print(month, 'month expenses:', expenses, 'short by:', -difference)

print('You need to ask your parents for', parents, 'rubles')
