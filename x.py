import unittest

# Function to test
def add(x, y):
    return x + y

# Test case class
class SimpleTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(4, 5), 9)

# Run tests
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
