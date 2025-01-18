
# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        LUNCH_COST = 2.50
        if payment >= LUNCH_COST:
            self.funds += LUNCH_COST
            self.lunches += 1
            payment -= LUNCH_COST
        return payment
        
    def eat_special(self, payment: float):
        SPECIAL_COST = 4.30
        if payment >= SPECIAL_COST:
            self.funds += SPECIAL_COST
            self.specials += 1
            payment -= SPECIAL_COST
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        LUNCH_COST = 2.50
        if card.balance >= LUNCH_COST:
            card.balance -= LUNCH_COST
            self.lunches += 1
            return True
        else:
            return False
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        

    def eat_special_lunchcard(self, card: LunchCard):
        SPECIAL_COST = 4.30
        if card.balance >= SPECIAL_COST:
            card.balance -= SPECIAL_COST
            self.specials += 1
            return True
        else:
            return False
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        self.funds += amount



if __name__ == "__main__":
    LUNCH_COST = 2.50
    SPECIAL_COST = 4.30
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials) 
