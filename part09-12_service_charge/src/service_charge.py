# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def __service_charge(self):
        self.__balance -= self.__balance * .01

    def deposit(self,amount):
        self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount):
        self.__balance -= amount
        self.__service_charge()


    
    @property
    def balance(self):
        return self.__balance
    

if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)