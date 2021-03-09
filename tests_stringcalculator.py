import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.add(""), 0)


    def test_one_arg(self):
        self.assertEqual(stringcalculator.add("1"), 1)


    def test_two_args(self):
        self.assertEqual(stringcalculator.add("1,2"), 3)


    def test_non_numeric_value(self):
        self.assertRaises(ValueError, stringcalculator.add, "1,a")

    
    def test_new_line_as_valid_delimiter(self):
        self.assertEqual(stringcalculator.add("1,2\n3"), 6)
        self.assertRaises(ValueError, stringcalculator.add, "1,\n3")


    def test_custom_delimiter_declaration(self):
        self.assertEqual(stringcalculator.add(";\n1;2;3"), 6)
        self.assertRaises(ValueError, stringcalculator.add, "[\n1,2,3")


if __name__ == '__main__':
    unittest.main()
