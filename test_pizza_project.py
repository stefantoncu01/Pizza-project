from pizza_project import VeganPizza, CarnivoraPizza, PepperoniPizza, HawaiianPizza, Client, Order
import pytest

@pytest.fixture
def vegan_pizza():
    """
    Creates a vegan pizza based on VeganPizza class
    """
    return VeganPizza('vegan', 'small')


@pytest.fixture
def carnivora_pizza():
    """
    Creates a carnivora pizza based on CarnivoraPizza class
    """
    return CarnivoraPizza('carnivora', 'large')


@pytest.fixture
def first_client():
    """
    Creates a client based on Client class, with card
    """
    return Client('John Wick', 'Bucharest')


@pytest.fixture
def second_client():
    """
    Creates a client based on Client class, without card
    """
    return Client('John Doe', 'Pisoni', False)


@pytest.fixture
def order_one(first_client, vegan_pizza, carnivora_pizza):
    """
    Creates an order based on the first_client, vegan_pizza, carnivora_pizza objects
    """
    return Order(client=first_client, products=[vegan_pizza, carnivora_pizza])


def test_vegan_price(vegan_pizza):
    """
    Creates a vegan pizza and the price is tested
    """
    assert vegan_pizza.price == 9


def test_carnivora_price(carnivora_pizza):
    """
    Creates a carnivora pizza and the price is tested
    """
    assert carnivora_pizza.price == 22.5


def test_first_client_address(first_client):
    """
    Creates a client and the attributes are tested
    """
    assert first_client.address == 'Bucharest'
    assert first_client.name == 'John Wick'


def test_second_client_name(second_client):
    """
    Creates a client and the attributes are tested
    """
    assert second_client.name == 'John Doe'
    assert second_client.address == 'Pisoni'


def test_order_total_price_with_card(order_one):
    """
    Creates an order having a client with a card and the total_price is tested
    """
    assert order_one.total_price == 28.35


def test_order_total_price_no_card(second_client,vegan_pizza, carnivora_pizza):
    """
    Creates an order having a client without a card and the total_price is tested
    """
    pepperoni_pizza = PepperoniPizza('pepperoni', 'small')
    hawaiian_pizza = HawaiianPizza('hawaiian', 'medium')
    second_order = Order(client=second_client, products=[pepperoni_pizza, carnivora_pizza, vegan_pizza, hawaiian_pizza])
    assert second_order.total_price == 61.5


def test_order_invoice(order_one):
    """
    Creates an order and the invoice property is tested
    """
    assert '28.35' in order_one.invoice
    assert 'Bucharest' in order_one.invoice
    assert 'vegan' in order_one.invoice


def test_client_attributes(order_one):
    """
    Creates an order and the client attributes are tested
    """
    assert order_one.client.address == "Bucharest"
    assert order_one.client.name == "John Wick"

def test_pizza_attributes(order_one):
    """
    Creates an order and the attributes of Pizza objects are tested
    """
    assert order_one.products[1].size == "large"
    assert order_one.products[1].ingredients == ['tomato_sauce', 'cheese', 'chicken', 'parmesan', 'spinach']
    assert order_one.products[1].price == 22.5
