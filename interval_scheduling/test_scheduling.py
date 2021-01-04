import unittest
import scheduling


class TestScheduling(unittest.TestCase):
    def test(self):
        expectation = [
            ({(0, 1)}, [(0, 1)]),
        ]
        for argument, expected_output in expectation:
            actual_output = scheduling.get_schedule(argument)
            self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
