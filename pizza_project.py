##Pizza Project
##Create a Pizza class with the following attributes:
## - name
## - size
## - ingredients
##Sizes available: small, medium, large
##
##Create two Pizza subclasses: VeganPizza and CarnivoraPizza:
## - VeganPizza ingredients: 'tomato_sauce', 'pepper', 'olives'
## - CarnivoraPizza ingredients: 'tomato_sauce', 'cheese', 'chicken', 'parmesan', 'spinach'
##
##Add a method for calculating the price. The price should be based on size and ingredients using the following formula:
##    price = size_price * (no_of_ingredients * price_per_ingredient)
##Price information:
##price_per_ingredient - default value should be 3
##Small size - $ 1
##Medium size - $ 1.2
##Big size - $ 1.5

##print(f'I would like a {vegan_pizza.name} {vegan_pizza.size} size pizza with {" ".join(vegan_pizza.ingredients)} please!')
##print(f'That will be {vegan_pizza.price} for your {vegan_pizza.name} pizza!')
##print(f'That will be {carnivora_pizza.price} for your {carnivora_pizza.name} pizza!')

##Create two new classes “Order” & “Client”
##Client class:
##attributes: name, address, has_card (bool)
##Order class:
##attributes: client, products (list of Pizza objects)
##total_price property - calculated based on products attribute. If the client has_card a 10% discount should be applied.
##invoice property - table formatted string containing all products associated with this order, their prices, the total price, and client information
##

##Tests
##
##Write tests using pytest module for your code:
##
##Test 1.
##Create some Pizzas, one of each type and assert the price for each one.
##
##Test 2.
##Create two Client objects and assert some client attributes
##
##Test 3.
##Create an Order having a client with a card. Assert the total_price
##
##Test 4.
##Create an Order having a client without a card. Assert the total_price
##
##Test 5.
##Create an Order. Test invoice property
##
##Test 6.
##Create an Order. Test Client attributes.
##
##Test 7.
##Create an Order. Test Pizzas attributes and prices

# from tabulate import tabulate

class Pizza:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.ingredients = None

    @property
    def price(self):
        price_per_ingredient = 3
        size_price = {
            "small": 1,
            "medium": 1.2,
            "large": 1.5
        }
        return size_price[self.size] * len(self.ingredients) * price_per_ingredient


class VeganPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'pepper', 'olives']


class CarnivoraPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'cheese', 'chicken', 'parmesan', 'spinach']


class PepperoniPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'cheese', 'salami', 'habanero_pepper']


class HawaiianPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'cheese', 'pineapple', 'coocked_ham', 'onion']


class Client:
    def __init__(self, name, address, has_card=True):
        self.name = name
        self.address = address
        self.has_card = has_card


class Order:
    def __init__(self, client, products):
        self.client = client
        self.products = products

    @property
    def total_price(self):
        price = sum([product.price for product in self.products])
        if self.client.has_card:
            return price * 0.9
        return price

    @property
    def invoice(self):
        # table = [element.split(',') for element in [f'{product.name},{product.price}' for product in self.products]]
        # table.append(['Total price',self.total_price])
        # table.append(['Client information:', self.client.address])
        # headers = ['Item\nname','price']
        # return tabulate(table, headers, tablefmt="rst")
        return '\n'.join([f'{product.name} - {product.price}' for product in self.products]) + \
               '\nThe total price is {}! \nThe delivery will be in {}!'.format(self.total_price, self.client.address)

# first_client = Client("John Wick", "Bucharest", True)
# second_client = Client("Liviu Miu", "Pisoni")
# third_client = Client(name="Stefan", address="Tamasi", has_card=False)
#
# vegan_pizza = VeganPizza("vegan", "small")
# carnivora_pizza = CarnivoraPizza("carnivora", "large")
# pepperoni_pizza = PepperoniPizza("pepperoni", "small")
# hawaiian_pizza = HawaiianPizza("hawaiian", "medium")
#
# first_order = Order(client=first_client, products=[vegan_pizza, carnivora_pizza])
# second_order = Order(client=second_client, products=[hawaiian_pizza])
# third_order = Order(client=third_client, products=[pepperoni_pizza, carnivora_pizza, vegan_pizza,hawaiian_pizza])

#Test1
vegan_pizza = VeganPizza("vegan", "small")
carnivora_pizza = CarnivoraPizza("carnivora", "large")
pepperoni_pizza = PepperoniPizza("pepperoni", "small")
hawaiian_pizza = HawaiianPizza("hawaiian", "medium")

assert vegan_pizza.price == 9
assert pepperoni_pizza.price == 12
assert carnivora_pizza.price == 22.5
assert hawaiian_pizza.price == 18

#Test2
first_client = Client("John Wick", "Bucharest", True)
second_client = Client("Liviu Miu", "Pisoni")
third_client = Client(name="Stefan", address="Tamasi", has_card=False)

assert first_client.address == "Bucharest"
assert third_client.address == "Tamasi"

#Test3
first_order = Order(client=first_client, products=[vegan_pizza, carnivora_pizza])

assert first_order.total_price == 28.35

#Test4
third_order = Order(client=third_client, products=[pepperoni_pizza, carnivora_pizza, vegan_pizza,hawaiian_pizza])

assert third_order.total_price == 61.5

# #Test5
# first_order = Order(client=first_client, products=[vegan_pizza, carnivora_pizza])
#
# assert first_order.invoice == ===================  =========
# Item                 price
# name
# ===================  =========
# vegan                9
# carnivora            22.5
# Total price          28.35
# Client information:  Bucharest
# ===================  =========


#Test6
first_order = Order(client=first_client, products=[vegan_pizza, carnivora_pizza])

assert first_order.client.address == "Bucharest"

#Test7
third_order = Order(client=third_client, products=[pepperoni_pizza, carnivora_pizza, vegan_pizza,hawaiian_pizza])

assert third_order.products[2].size == "small"
assert third_order.products[3].price == 18