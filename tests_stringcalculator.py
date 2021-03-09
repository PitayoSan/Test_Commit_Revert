import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.add(""), 0)


    def test_one_arg(self):
        self.assertEqual(stringCalculator.add("1"), 1)


    def test_two_args(self):
        self.assertEqual(stringCalculator.add("1,2"), 3)


    def test_non_numeric_value(self):
        self.assertRaises(ValueError, stringCalculator.add("1,a"))


if __name__ == '__main__':
    unittest.main()
