import unittest
from ch import get_convex_hull


class TestConvexHull(unittest.TestCase):
    def test_simple(self):
        x = {(1, 2), (3, 4)}
        y = get_convex_hull(x)
        self.assertEqual(set(y), x)


if __name__ == "__main__":
    unittest.main()
