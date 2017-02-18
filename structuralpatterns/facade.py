import unittest

'''
The Facade Pattern provides a unified interface to a set of interfaces in a subsytem.
Facade defines a higher-level interface that makes the subsystem easier to use.

Note:
1) When you need to simplify and unify a large interface or complex set of interfaces, use a facade.
2) A facade decouples a client from a complex subsystem.
3) Implementing a facade requires that we compose the facade with its subsystem and use delegation to perform the work of the facade.
4) You can implement more than one facade for a subsystem.

Remember the Principle of least knowledge:
Take any object; now from any method in that object,
the principle tells us that we should only invoke methods that belong to:

- The Object itself
- Objects passed in as a parameters to the method
- Any object the method creates or instantiates
- Any components of the object
'''


class Device(object):
    def turn_on(self):
        raise NotImplemented


class Phone(Device):
    def turn_on(self):
        return "Turning Phone on"


class Computer(Device):
    def turn_on(self):
        return "Turning Computer on"


class App(object):
    def launch_app(self):
        raise NotImplemented


class WeatherApp(App):
    def launch_app(self):
        return "launch weather app"


class AppFacade(object):
    def __init__(self, device, app):
        self.device = device
        self.app = app

    def launch_app_in_a_device(self):
        self.device.turn_on()
        return self.app.launch_app()


class FacadeUnitTest(unittest.TestCase):
    def test_facade(self):
        facade = AppFacade(Phone(), WeatherApp())
        self.assertEqual(facade.launch_app_in_a_device(), "launch weather app")
