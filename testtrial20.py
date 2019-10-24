import unittest
import trial20


class TestCases(unittest.TestCase):

    def testPrimeNumbers(self):
        self.assertTrue(trial20.isPrime(2))
        self.assertTrue(trial20.isPrime(3))
        self.assertTrue(trial20.isPrime(5))
        self.assertTrue(trial20.isPrime(7))
        self.assertTrue(trial20.isPrime(11))
        self.assertTrue(trial20.isPrime(19))
        self.assertTrue(trial20.isPrime(29))


if __name__ == '__main__':
    unittest.main()
