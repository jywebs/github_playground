import unittest
from src.main import your_function


class TestMain(unittest.TestCase):

    def test_your_function(self):
        self.assertEqual(your_function(), "Hello, GitHub features learning!")


if __name__ == '__main__':
    unittest.main()