"""
Publishers + Subscribers = Observer Pattern

Design Principle: Strive for loosely coupled designs between objects that interact.

The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state,
all its dependents are notified and updated automatically.

"""
import abc
import unittest


class Subject(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_observer(self, observer):
        raise NotImplemented("register_observer is not implemented")

    @abc.abstractmethod
    def remove_observer(self, observer):
        raise NotImplemented("remove_observer is not implemented")

    @abc.abstractmethod
    def notify_observers(self):
        raise NotImplemented("notify_observers is not implemented")


class Observer(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, temperature, humidity, pressure):
        raise NotImplemented("update is not implemented")


class DisplayElement(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        raise NotImplemented("display is not implemented")


class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(
                self.temperature,
                self.humidity,
                self.pressure
            )

    def set_measurement(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurement_changed()

    def measurement_changed(self):
        self.notify_observers()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, subject):
        self.subject = subject
        self.temperature = None
        self.humidity = None
        self.subject.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions temperature={}, humidity={}".format(
            self.temperature,
            self.humidity))


class ObserverUnitTest(unittest.TestCase):
    def test_weather_app_using_observer_pattern(self):
        weather_data = WeatherData()
        current_conditions_display_observer = CurrentConditionsDisplay(weather_data)
        self.assertEqual(current_conditions_display_observer.temperature, None)
        self.assertEqual(current_conditions_display_observer.humidity, None)

        # Temperature got updated
        weather_data.set_measurement(80, 65, 30)

        # Since temperature was updated, the observers temperature also got updated
        self.assertEqual(current_conditions_display_observer.temperature, 80)
        self.assertEqual(current_conditions_display_observer.humidity, 65)
