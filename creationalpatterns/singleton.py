import unittest


class Singleton(object):
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(
                Singleton,
                class_). \
                __new__(
                class_,
                *args,
                **kwargs
            )
        return class_._instances[class_]


class PizzaSingleton(Singleton):
    name = "NY Pizza"
    dough = "good dough"

    def change_name(self, name):
        self.name = name


class SingletonUnitTest(unittest.TestCase):
    def test_singleton(self):
        pizza = PizzaSingleton()
        pizza.change_name("ChicagoPizza")
        second_pizza = PizzaSingleton()
        self.assertEqual(second_pizza.name, "ChicagoPizza")
        second_pizza.name = "Changing name"
        self.assertEqual(pizza.name, "Changing name")
