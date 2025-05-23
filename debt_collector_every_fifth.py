number_of_debtors = int(input('Enter the number of debtors: '))
total_debt = 0
for debtors in range(0, number_of_debtors, 5):
    print('Debtor number:', debtors)
    debt = int(input('How much do they owe? '))
    total_debt += debt
print('Total debt amount:', total_debt)
