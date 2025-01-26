# Write your solution here

eat_weekly_caf = int(input('How many times a week do you eat at the student cafeteria? '))
eat_price = float(input('The price of a typical student lunch? '))
eat_weekly_groc = float(input('How much money do you spend on groceries in a week? '))

print('Average food expenditure:')
weekly = eat_weekly_caf * eat_price + eat_weekly_groc
print(f'Daily: {weekly/7} euros')
print(f'Weekly: {weekly} euros')
