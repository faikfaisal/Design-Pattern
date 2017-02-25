"""
The Decorator Pattern attaches additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending functionality.

In Decorator pattern players

Abstract component class
Abstract decorator class which inherits component class
Concrete component class
Concrete Decorator class where component is the dependency
"""
import abc
import unittest


# Abstract component class
class Beverage(object, metaclass=abc.ABCMeta):
    def __init__(self):
        self.description = "Unknown Description"

    @abc.abstractmethod
    def cost(self):
        raise NotImplemented("cost is not implemented")


# Abstract decorator class which inherits component class
class CondimentDecorator(Beverage):
    @abc.abstractmethod
    def cost(self):
        raise NotImplemented("cost is not implemented")


# Concrete component class
class Espresso(Beverage):
    def __init__(self):
        super(Espresso, self)
        self.description = "Expresso Coffee"

    def cost(self):
        return 1.99


# Concrete component class
class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self)
        self.description = "House blend coffeee"

    def cost(self):
        return 0.89


# Concrete Decorator class where component is the dependency
class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super(Mocha, self)
        self.beverage = beverage
        self.description = self.beverage.description

    def cost(self):
        return 0.20 + self.beverage.cost()


class DecoratorUnitTest(unittest.TestCase):
    def test_serving_coffee(self):
        first_beverage = Espresso()
        self.assertEqual(first_beverage.cost(), 1.99)
        first_beverage = Mocha(first_beverage)
        self.assertEqual(first_beverage.cost(), 2.19)
        first_beverage = Mocha(first_beverage)
        self.assertEqual(first_beverage.cost(), 2.39)
