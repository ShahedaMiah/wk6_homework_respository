class Budget:
# creating a class celled 'Budget' in a module called 'budget'

    def __init__(self, opening_balance):
        self.__balance = opening_balance

    def add_income(self, amount):
        self.__balance += amount
        return

    def minus_rent(self, amount):
        self.__balance -= amount

    def minus_council_tax(self, amount):
        self.__balance -= amount

    def minus_utilities(self, amount):
        self.__balance -= amount

    def add_bonus(self, amount):
        self.__balance += amount

    def closing_balance(self):
        return self.__balance

    def __str__(self):
        return "You have {} left".format(self.__balance)

def main():
    jodie = Budget(1000)
    # here we are instantiating an object called 'jodie' from the class (template) 'Budget'
    jodie.add_income(700)
    jodie.minus_rent(300)
    jodie.minus_utilities(50)
    jodie.minus_council_tax(15)
    print("Jodie has", jodie.closing_balance())

if __name__ == "__main__":
    main()
