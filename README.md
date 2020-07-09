# Pizza-project

#Create a Pizza class with the following attributes:
 - name
 - size
 - ingredients
Sizes available: small, medium, large

##Create two Pizza subclasses: VeganPizza and CarnivoraPizza:
 - VeganPizza ingredients: 'tomato_sauce', 'pepper', 'olives'
 - CarnivoraPizza ingredients: 'tomato_sauce', 'cheese', 'chicken', 'parmesan', 'spinach'

###Add a method for calculating the price. The price should be based on size and ingredients using the following formula:
  - price = size_price * (no_of_ingredients * price_per_ingredient)
  - Price information:
    - price_per_ingredient - default value should be 3
    - Small size - $ 1
    - Medium size - $ 1.2
    - Big size - $ 1.5

####Create two new classes “Order” & “Client”
  - Client class:
    - attributes: name, address, has_card (bool)
  - Order class:
    - attributes: client, products (list of Pizza objects)
    - total_price property - calculated based on products attribute. If the client has_card a 10% discount should be applied.
    - invoice property - table formatted string containing all products associated with this order, their prices, the total price, and client information

#####Tests
1. Create some Pizzas, one of each type and assert the price for each one.
2. Create two Client objects and assert some client attributes
3. Create an Order having a client with a card. Assert the total_price
4. Create an Order having a client without a card. Assert the total_price
5. Create an Order. Test invoice property
6. Create an Order. Test Client attributes.
7. Create an Order. Test Pizzas attributes and prices
