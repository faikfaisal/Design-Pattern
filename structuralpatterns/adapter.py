import unittest

'''
The Adapter Pattern converts the interface of a class into another interface the clients expect.
Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.

Notes:
1) When you need to use an existing class and its interface is not the one you need, use an adapter.
2) An adapter changes an interface into one a client expects
3) An adapter wraps an object to change its interface
'''


class Duck(object):
    def quack(self):
        raise NotImplemented

    def fly(self):
        raise NotImplemented


class Turkey(object):
    def gobble(self):
        raise NotImplemented

    def fly(self):
        raise NotImplemented


class WildTurkey(Turkey):
    def gobble(self):
        return "WildTurkey gobble"

    def fly(self):
        return "WildTurkey fly"


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        return self.turkey.gobble()

    def fly(self):
        return self.turkey.fly()


class AdapterUnitTest(unittest.TestCase):
    def test_adapter(self):
        turkey = TurkeyAdapter(WildTurkey())
        self.assertEqual(turkey.quack(), "WildTurkey gobble")
