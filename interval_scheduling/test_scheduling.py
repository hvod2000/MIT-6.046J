import unittest
import scheduling


class TestScheduling(unittest.TestCase):
    def test(self):
        expectation = [
            ({(0, 1)}, [(0, 1)]),
            ({(0, 2), (1, 2)}, [(0, 2)]),
            ({(1, 5), (0, 2), (3, 6)}, [(0, 2), (3, 6)]),
            ({(5, 100), (2, 7), (8, 12), (15, 80)}, [(2, 7), (8, 12), (15, 80)]),
            ({(0, 2), (1, 5)}, [(1, 5)]),
        ]
        for argument, expected_output in expectation:
            actual_output = scheduling.get_schedule(argument)
            self.assertEqual(
                actual_output, expected_output, f"Input: {argument}"
            )


if __name__ == "__main__":
    unittest.main()
