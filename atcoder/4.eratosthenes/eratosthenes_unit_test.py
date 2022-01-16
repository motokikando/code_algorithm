import unittest
from eratosthenes_2 import is_prime2

class PrimeTest(unittest.TestCase):

    def test_is_prime_ok(self): #primenumberでないもの
        for i in [2, 3, 5, 7, 11]:
            self.assertTrue(is_prime2(i))

    def test_is_prime_no(self):
        for i in [1,4,6,8,10]:
            self.assertFalse(is_prime2(i))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime2(-3))

    def test_is_prime_raise_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime2('string')

if __name__ == '__main__':
    unittest.main()