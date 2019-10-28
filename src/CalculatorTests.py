import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('/src/addition_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('/src/subtraction_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('/src/Multiply_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('/src/division_test.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.Divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
