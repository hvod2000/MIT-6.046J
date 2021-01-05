import unittest
import scheduling
from random import randint


class TestScheduling(unittest.TestCase):
    def test_colliding(self):
        def random_interval():
            start = randint(0, 100)
            end = start + randint(1, 25)
            value = randint(1, 25)
            return (start, end, value)
        intervals = [random_interval() for i in range(2**randint(4, 8))]
        output = scheduling.get_schedule(intervals)
        for i in output:
            for j in output:
                if i != j:
                    if i[0] < j[1] < i[1] or i[0] < j[0] < i[1]:
                        self.fail(f"{intervals} -> {output}")


    def test_size(self):
        expectation = [
            ({(0, 1, 1)}, 1),
            ({(0, 2, 1), (1, 2, 1)}, 1),
            ({(1, 5, 1), (0, 2, 1), (3, 6, 1)}, 2),
            ({(5, 100, 1), (2, 7, 1), (8, 12, 1), (15, 80, 1)}, 3),
            ({(0, 2, 1), (1, 5, 1)}, 1),
        ]
        for arg, expected_v in expectation:
            actual_output = scheduling.get_schedule(arg)
            v = sum(x[2] for x in actual_output)
            self.assertEqual(v, expected_v, f"In: {arg}")


if __name__ == "__main__":
    unittest.main()
