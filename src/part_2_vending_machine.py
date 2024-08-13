class VendingMachine:
    def __init__(self):
        self.credit = 0
        self.stock = {"A": {}, "B": {}, "C": {}}

    def add_credit(self, amount):
        self.credit += amount

    def credit_checker(self, price):
        pass
