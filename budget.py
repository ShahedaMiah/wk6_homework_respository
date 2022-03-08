class Budget:

    def __init__(self, opening_balance):
        self.__balance = opening_balance

    def income(self, amount):
        self.__balance += amount
        return

    def rent(self, amount):
        self.__balance -= amount

    def council_tax(self, amount):
        self.__balance -= amount

    def utilities(self, amount):
        self.__balance -= amount

    def bonus(self, amount):
        self.__balance += amount

    def closing_balance(self):
        return self.__balance

    def __str__(self):
        return "You have {} left".format(self.__balance)

def main():
    jodie = Budget(1000)
    jodie.income(700)
    jodie.rent(300)
    jodie.utilities(50)
    jodie.council_tax(15)
    print("Jodie has", jodie.closing_balance())

if __name__ == "__main__":
    main()
