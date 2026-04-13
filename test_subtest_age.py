import unittest
from age import categorize_by_age

class TestSubtestAge(unittest.TestCase):

    def test_is_child(self):
        for age in range(0, 10):  # 0 to 9
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")

    def test_is_adult(self):
        for age in range(19, 66):  # 19 to 65
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")

    def test_is_golden(self):
        for age in range(66, 151):  # 66 to 150
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Golden age")

if __name__ == "__main__":
    unittest.main(verbosity=2)
