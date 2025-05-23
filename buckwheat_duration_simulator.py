buckwheat = int(input('Enter how much buckwheat is left - '))
month = 0
for i in range(buckwheat // 4):
    month += 1
    buckwheat -= 4
    print(month, 'Month: ', buckwheat)
print('Buckwheat ran out after', month, 'months!')
