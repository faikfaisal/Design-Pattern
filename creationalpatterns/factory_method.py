import unittest


# Abstract Product
class Pizza(object):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = None

    def prepare(self):
        print("Preparing {}".format(self.name))
        print("Tossing Dough {}".format(self.dough))
        print("Adding Sauce... {}".format(self.sauce))
        print("toppings {}".format(self.toppings))

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the Pizza in diagonal sizes")

    def box(self):
        print("Pleace it in official box")


# Concrete Product
class NYCheesePizza(Pizza):
    def __init__(self):
        super(NYCheesePizza, self).__init__()
        self.name = "Ny Style Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marina sauce"
        self.toppings = ['Granted Reggiano Cheese']


# Concrete Product
class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super(ChicagoStyleCheesePizza, self).__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

    def cut(self):
        print("Cutt the pizza as square")


# Abstract Store
class PizzaStore(object):
    def create_pizza(self, type_of_pizza):
        raise NotImplemented

    def order_pizza(self, type_of_pizza):
        pizza = self.create_pizza(type_of_pizza)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


# Concrete Store
class NYPizzaStore(PizzaStore):
    def create_pizza(self, type_of_pizza):
        if type_of_pizza == "cheese":
            return NYCheesePizza()


# Concrete Store
class ChicagoStyleStore(PizzaStore):
    def create_pizza(self, type_of_pizza):
        if type_of_pizza == "cheese":
            return ChicagoStyleCheesePizza()


class FactoryMethodUnitTest(unittest.TestCase):
    def test_order_ny_style_cheese_pizza(self):
        ny_pizza_store = NYPizzaStore()
        pizza = ny_pizza_store.order_pizza("cheese")
        self.assertEqual(pizza.name, 'Ny Style Cheese Pizza')

    def test_order_chicago_style_cheese_pizza(self):
        chicago_pizza_store = ChicagoStyleStore()
        pizza = chicago_pizza_store.order_pizza("cheese")
        self.assertEqual(pizza.name, "Chicago Style Deep Dish Cheese Pizza")
