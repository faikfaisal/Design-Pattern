import unittest


class MethodNotImplementedException(Exception):
    pass


# Pizza is the product
class Pizza(object):
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""


# Abstract builder
class PizzaBuilder(object):
    def __init__(self):
        self.pizza = Pizza()

    def build(self):
        return self.pizza

    def build_dough(self):
        raise MethodNotImplementedException()

    def build_sauce(self):
        raise MethodNotImplementedException()

    def build_topping(self):
        raise MethodNotImplementedException()


# Concrete builder
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super(HawaiianPizzaBuilder, self).__init__()

    def build_dough(self):
        self.pizza.dough = "cross"
        return self

    def build_sauce(self):
        self.pizza.sauce = "mild"
        return self

    def build_topping(self):
        self.pizza.topping = "ham+pineapple"
        return self


# Concrete builder
class SpicyPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super(SpicyPizzaBuilder, self).__init__()

    def build_dough(self):
        self.pizza.dough = "pan baked"
        return self

    def build_sauce(self):
        self.pizza.sauce = "hot"
        return self

    def build_topping(self):
        self.pizza.topping = "pepperoni+salami"
        return self


# Director
class Waiter(object):
    def __init__(self, pizza_builder=HawaiianPizzaBuilder()):
        self.pizza_builder = pizza_builder

    def construct_pizza(self):
        return self.pizza_builder. \
            build_dough(). \
            build_sauce(). \
            build_topping(). \
            build()


class BuilderPatternUnitTest(unittest.TestCase):
    def test_hawaiian_pizza_builder(self):
        waiter = Waiter(pizza_builder=HawaiianPizzaBuilder())
        pizza = waiter.construct_pizza()
        self.assertEqual(pizza.dough, "cross")
        self.assertEqual(pizza.sauce, "mild")
        self.assertEqual(pizza.topping, "ham+pineapple")

    def test_spicy_pizza_builder(self):
        waiter = Waiter(SpicyPizzaBuilder())
        pizza = waiter.construct_pizza()
        self.assertEqual(pizza.dough, "pan baked")
        self.assertEqual(pizza.sauce, "hot")
        self.assertEqual(pizza.topping, "pepperoni+salami")

