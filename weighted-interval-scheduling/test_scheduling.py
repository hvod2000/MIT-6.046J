import unittest
import scheduling


class TestScheduling(unittest.TestCase):
    def test_simple(self):
        expectation = [
            ({(0, 1, 1)}, [(0, 1, 1)]),
            ({(0, 2, 1), (1, 2, 1)}, ([(0, 2, 1)], [(1, 2, 1)])),
            ({(1, 5, 1), (0, 2, 1), (3, 6, 1)}, [(0, 2, 1), (3, 6, 1)]),
            (
                {(5, 100, 1), (2, 7, 1), (8, 12, 1), (15, 80, 1)},
                [(2, 7, 1), (8, 12, 1), (15, 80, 1)],
            ),
            ({(0, 2, 1), (1, 5, 1)}, ([(1, 5, 1)], [(0, 2, 1)])),
        ]
        for x, y in expectation:
            actual_y = scheduling.get_schedule(x)
            test = self.assertIn if isinstance(y, tuple) else self.assertEqual
            test(actual_y, y, f"Input: {x}")


if __name__ == "__main__":
    unittest.main()
