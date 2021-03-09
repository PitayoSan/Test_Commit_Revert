import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.add(""), 0)


    def test_non_numeric_value(self):
        self.assertRaises(ValueError, stringcalculator.add, "1,a")


if __name__ == '__main__':
    unittest.main()
