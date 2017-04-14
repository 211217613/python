import unittest
from primes import is_prime


class PrimesTestCase(unittest.TestCase):
    """Tests for 'primes.py'."""

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))
    
    def test_is_34_prime(self):
        self.assertFalse(is_prime(34))

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='Four is not a prime')

    def test_is_zero_not_prime(self):
        """Test if zero is a prime."""
        self.assertFalse(is_prime(0), msg='Zero is not a prime')
    
    def test_negative_number(self):
        """Is a negative number correctly determined not to be a prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{}'.format(index))

if __name__ == '__main__':
    unittest.main()
