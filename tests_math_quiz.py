import unittest
from math_quiz import random_integer, random_operator, calculation


class TestMathGame(unittest.TestCase):

    def random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num =  random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def random_operator(self):
        rand_operator = random_operator()
         self.assertIn(rand_operator, operators)
        pass

    def calcultion(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 5, '-', '10 - 5', 5),
                (3, 6, '*', '3 * 6', 18),
                (8, 4, '/', '8 / 4', 2),
            ]

            for number1, number2, operator, expected_problem, expected_answer in test_cases:
                result = calculation(num1, num2, operator)
                self.assertEqual(result, expected_answer)
                pass

if _name_ == "_main_":
    unittest.main()
