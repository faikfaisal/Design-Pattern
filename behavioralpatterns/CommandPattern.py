"""
The Command Pattern encapsulates a request as an object,
thereby letting you parameterize other objects with different requests,
queue or log requests, and support undoable operations.
"""

import abc
import unittest


class Command(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        raise NotImplemented


class Light(object):
    def on(self):
        return "Light On"

    def off(self):
        return "Light Off"


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.on()


class SimpleRemoteControl():
    def __init__(self, command):
        self.command = command

    def button_pressed(self):
        return self.command.execute()


class CommandPatternUnitTest(unittest.TestCase):
    def test_command_pattern(self):
        light_command = LightOnCommand(Light())
        remote_control = SimpleRemoteControl(light_command)
        self.assertEqual(remote_control.button_pressed(), "Light On")
