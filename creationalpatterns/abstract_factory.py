import unittest

#Abstract Factory
class PizzaIngredientFactory(object):
    def create_dough(self):
        raise NotImplemented

    def create_sauce(self):
        raise NotImplemented

    def create_toppings(self):
        raise NotImplemented


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        print("NY dough created")

    def create_sauce(self):
        print("NY create_sauce")

    def create_toppings(self):
        print("NY create_toppings")


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        print("Chicago Gough created")

    def create_sauce(self):
        print("Chicago create_sauce")

    def create_toppings(self):
        print("Chicago create_toppings")


class Pizza(object):
    def prepare(self):
        raise NotImplemented

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into dialonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.ingredient_factory.create_dough()
        self.ingredient_factory.create_sauce()
        self.ingredient_factory.create_toppings()


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


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type_of_pizza):
        pizza_factory = NYPizzaIngredientFactory()
        if type_of_pizza == "cheese":
            return CheesePizza(pizza_factory)


class AbstractFactoryUnitTest(unittest.TestCase):
    def test_order_ny_style_cheese_pizza(self):
        pizza_store = NYPizzaStore()
        pizza_store.order_pizza("cheese")
