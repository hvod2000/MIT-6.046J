import unittest
from finding import get_by_index
from random import randint

expectation = [
    ({1, 2, 3, 4, 5}, 3),
]


class TestScheduling(unittest.TestCase):
    def test_size(self):
        for arg, expected_output in expectation:
            actual_output = get_by_index(arg, (len(arg) - 1) // 2)
            self.assertEqual(actual_output, expected_output, f"In: {arg}")


if __name__ == "__main__":
    unittest.main()
