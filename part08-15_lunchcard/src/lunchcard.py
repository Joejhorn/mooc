class LunchCard:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self,cost):
        return (self.balance - cost) > 0
    
    def deposit_money(self, money):
        if money < 0:
            raise ValueError('You cannot deposit an amount of money less than zero')
        self.balance += money

    def eat_lunch(self):
        LUNCH = 2.60
        if self.check_balance(LUNCH):
            self.balance -= LUNCH         

    def eat_special(self):
        SPECIAL = 4.60
        if self.check_balance(SPECIAL):
            self.balance -= SPECIAL

    def __str__(self):
        return (f'The balance is {self.balance:.1f} euros')
    

    
peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')

peters_card.deposit_money(20)
graces_card.eat_special()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')




