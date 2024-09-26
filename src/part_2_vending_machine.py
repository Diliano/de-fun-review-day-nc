class InsufficientCreditError(Exception):
    def __init__(self):
        self.message = "Insufficient credit!"
        super().__init__(self.message)

class OutOfStockError(Exception):
    def __init__(self):
        self.message = "Item out of stock"
        super().__init__(self.message)

class VendingMachine:
    def __init__(self):
        self.credit = 0
        self.stock = {"A": {}, "B": {}, "C": {}}

    def add_credit(self, amount):
        self.credit += amount

    def credit_checker(self, price):
        return self.credit >= price

    def add_stock(self, stock_to_add, position):
        if not isinstance(stock_to_add, dict):
            raise TypeError("Stock must be a dictionary")
        if not isinstance(position, str):
            raise TypeError("Position must be a string")
        if position not in self.stock:
            raise ValueError("Position does not exist")
        
        self.stock[position] = stock_to_add

    def purchase_item(self, position):
        if not isinstance(position, str):
            raise TypeError("Position must be a string")
        if position not in self.stock:
            raise ValueError("Position does not exist")
        
        if self.stock[position]["quantity"] == 0:
            raise OutOfStockError

        if self.credit < self.stock[position]["price"]:
            raise InsufficientCreditError
        
        self.stock[position]["quantity"] -= 1
        self.credit -= self.stock[position]["price"]
        return self.stock[position]["name"]