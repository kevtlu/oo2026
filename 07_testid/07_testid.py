from abc import ABC, abstractmethod
import unittest

class Konto(ABC):
    @abstractmethod
    def lisa(self, s): pass

    @abstractmethod
    def vota(self, s): pass

    @abstractmethod
    def saldo(self): pass

class Saastukonto(Konto):
    def __init__(self):
        self.s = 0

    def lisa(self, s):
        self.s += s

    def vota(self, s):
        if s <= self.s:
            self.s -= s
            return True
        return False
    
    def saldo(self):
        return self.s

class Test(unittest.TestCase):
    def setUp(self):
        self.k = Saastukonto()

    def test_alg(self):
        self.assertEqual(self.k.saldo(), 0)

    def test_lisa(self):
        self.k.lisa(100)
        self.assertEqual(self.k.saldo(), 100)

    def test_vota(self):
        self.k.lisa(50)
        self.assertTrue(self.k.vota(30))

unittest.main(verbosity=2)