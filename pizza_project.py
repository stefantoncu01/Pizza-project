class Pizza:
    """
    Creates a pizza with the attributes: name, size, ingredients
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.ingredients = None

    @property
    def price(self):
        """
        Calculates the price based on size and ingredients
        :return: an integer, it represents the price of the pizza
        """
        price_per_ingredient = 3
        size_price = {
            "small": 1,
            "medium": 1.2,
            "large": 1.5
        }
        return size_price[self.size] * len(self.ingredients) * price_per_ingredient


class VeganPizza(Pizza):
    """
    Creates a vegan pizza by inheriting attributes from Pizza class
    """
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'pepper', 'olives']


class CarnivoraPizza(Pizza):
    """
    Creates a carnivora pizza by inheriting attributes from Pizza class
    """
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'cheese', 'chicken', 'parmesan', 'spinach']


class PepperoniPizza(Pizza):
    """
    Creates a pepperoni pizza by inheriting attributes from Pizza class
    """
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'cheese', 'salami', 'habanero_pepper']


class HawaiianPizza(Pizza):
    """
    Creates a hawaiian pizza by inheriting attributes from Pizza class
    """
    def __init__(self, name, size):
        super().__init__(name, size)
        self.ingredients = ['tomato_sauce', 'cheese', 'pineapple', 'coocked_ham', 'onion']


class Client:
    """
    Creates a client with the attributes name, address, has_card(bool)
    """
    def __init__(self, name, address, has_card=True):
        self.name = name
        self.address = address
        self.has_card = has_card


class Order:
    """
    Creates an order based on the Client class and products (a list of Pizza objects)
    """
    def __init__(self, client, products):
        self.client = client
        self.products = products

    @property
    def total_price(self):
        """
        Calculates the total price of the order based on products attribute. If the client has_card a 10% discount should be applied.
        :return: an integer, it represents the total price of the order
        """
        price = sum([product.price for product in self.products])
        if self.client.has_card:
            return price * 0.9
        return price

    @property
    def invoice(self):\
        """
        Table formatted string containing all products associated with this order, their prices, the total price, and client information
        :return: Table formatted string
        """
        result ='\n'.join([f'{product.name} - {product.price}' for product in self.products])
        result += f'\nThe total price is {self.total_price}! \nThe delivery will be in {self.client.address}!'
        return result
