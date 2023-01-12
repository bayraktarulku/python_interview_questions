import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_add_two_negative_numbers(self):
        result = add(-1, -2)
        self.assertEqual(result, -3)

    def test_add_positive_and_negative_numbers(self):
        result = add(-1, 2)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
