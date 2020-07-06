import pytest
from pizza_project import VeganPizza, CarnivoraPizza, PepperoniPizza, HawaiianPizza, Client, Order

@pytest.fixture
def vegan_pizza():
    return VeganPizza('vegan', 'small')


@pytest.fixture
def carnivora_pizza():
    return CarnivoraPizza('carnivora', 'large')


@pytest.fixture
def first_client():
    return Client("John Wick", "Bucharest", True)


@pytest.fixture
def second_client():
    return Client("Liviu Miu", "Pisoni")


@pytest.fixture
def order_one(first_client, vegan_pizza, carnivora_pizza):
    return Order(client=first_client, products=[vegan_pizza, carnivora_pizza])


#Test 1 Create some Pizzas, one of each type and assert the price for each one.
def test_vegan_price(vegan_pizza):
    assert vegan_pizza.price == 9


def test_carnivora_price(carnivora_pizza):
    assert carnivora_pizza.price == 22.5


# Test 2 Create two Client objects and assert some client attributes
def test_first_client_address(first_client):
    assert first_client.address == "Bucharest"


def test_second_client_name(second_client):
    assert second_client.name == "Liviu Miu"


# Test 3 Create an Order having a client with a card. Assert the total_price
def test_order_total_price_with_card(order_one):
    assert order_one.total_price == 28.35


# Test 4 Create an Order having a client without a card. Assert the total_price\
def test_order_total_price_no_card(vegan_pizza, carnivora_pizza):
    third_client = Client(name="Stefan", address="Tamasi", has_card=False)
    pepperoni_pizza = PepperoniPizza("pepperoni", "small")
    hawaiian_pizza = HawaiianPizza("hawaiian", "medium")
    third_order = Order(client=third_client, products=[pepperoni_pizza, carnivora_pizza, vegan_pizza, hawaiian_pizza])
    assert third_order.total_price == 61.5


# Test 5 Create an Order. Test invoice property
def test_order_invoice(order_one):
    assert order_one.total_price == 28.35
    assert order_one.client.address == "Bucharest"
    assert order_one.products[0].name == "vegan"


# Test 6 Create an Order. Test Client attributes.
def test_client_attributes(order_one):
    assert order_one.client.address == "Bucharest"


#Test 7. Create an Order. Test Pizzas attributes and prices
def test_pizza_attributes(order_one):
    assert order_one.products[1].size == "large"
    assert order_one.products[1].ingredients == ['tomato_sauce', 'cheese', 'chicken', 'parmesan', 'spinach']
    assert order_one.products[1].price == 22.5
