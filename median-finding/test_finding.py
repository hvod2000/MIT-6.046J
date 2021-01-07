import unittest
from finding import get_by_index
from random import randint

class TestScheduling(unittest.TestCase):
    def test_median(self):
        for _ in range(16):
            arg  = {randint(0, 2**10) for _ in range(2**randint(1, 11))}
            expected_output = list(sorted(arg))[(len(arg) - 1) // 2]
            actual_output = get_by_index(arg, (len(arg) - 1) // 2)
            self.assertEqual(actual_output, expected_output, f"In: {arg}")

    def test_index(self):
        for _ in range(16):
            elements = [randint(0, 2**10) for _ in range(2**randint(1, 11))]
            index = randint(0, len(elements) - 1)
            expected_output = list(sorted(elements))[index]
            actual_output = get_by_index(elements, index)
            self.assertEqual(actual_output, expected_output,
                    f"In: {index}, {elements}")


if __name__ == "__main__":
    unittest.main()
