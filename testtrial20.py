import unittest
import trial20, mikeprime


class TestCases(unittest.TestCase):

    def testPrimeNumbers(self):
        self.assertTrue(mikeprime.isPrime(2))
        self.assertTrue(mikeprime.isPrime(3))
        self.assertTrue(mikeprime.isPrime(5))
        self.assertTrue(mikeprime.isPrime(7))
        self.assertTrue(mikeprime.isPrime(11))
        self.assertTrue(mikeprime.isPrime(19))
        self.assertTrue(mikeprime.isPrime(29))


if __name__ == '__main__':
    unittest.main()
