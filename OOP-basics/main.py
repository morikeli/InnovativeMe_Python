import csv


class Item:
    pay_rate = 0.8  # pay rate after 20% discount
    all_items = []


    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        # validate arguments data types
        assert price >= 0, f"Price {price} must be equal to or greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} must be equal to or greater than 0!"

        # append items in the list "all_items"
        Item.all_items.append(self)
        

    def calculate_total_price(self):
        return self.price * self.quantity
    

    def give_discount(self):
        self.price = self.price * self.pay_rate
    

    @classmethod
    def load_csv_file(cls):
        with open('items.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)
        
        # iterate list and print every item
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer() # check for .0 in the number, e.g. if a number is in the form 5.0, 7.0, 10.0, 300.0, etc
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        # return f"Item('{self.name}', {self.price}, {self.quantity})"
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"



class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        # validate arguments data types
        assert broken_phones >= 0, f"Broken_phones {broken_phones} must be equal to or greater than 0!"

        self.broken_phones = broken_phones


# item_1 = Item("Phone", 100, 1)
# item_2 = Item("Laptop", 1000, 3)


# Item.load_csv_file()

# print(Item.all_items)


# print(item_1.calculate_total_price())
# print(item_2.calculate_total_price())

# print(Item.__dict__)    # print all the attributes at the class level
# print(item_1.__dict__)  # print all the attributes at the instance level

# item_1.give_discount()
# print(f'Discount: {item_1.price}')

# item_2.pay_rate = 0.7
# item_2.give_discount()
# print(f'Discount: {item_2.price}')

# print(Item.is_integer(7.0))


# phone_1 = Phone('Redmi', 500, 5, 1)
# print(phone_1.calculate_total_price())
# phone_2 = Phone('Samsung', 700, 5, 1)

# print(Item.all_items)
# print(Phone.all_items)

item_1 = Item("Item 1", 750)

print(item_1.read_only_name)

item_1.read_only_name = 'BBB'