import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.add(""), 0)


    def test_non_numeric_value(self):
        with self.assertRaises(ValueError) as context:
            stringcalculator.add("1,a"))
        self.assertTrue('only integers allowed - a' in context.exception)


if __name__ == '__main__':
    unittest.main()
