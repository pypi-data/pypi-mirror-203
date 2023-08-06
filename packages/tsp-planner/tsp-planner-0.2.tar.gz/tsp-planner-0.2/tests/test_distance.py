import unittest
from src.utils.distance import euclidean_distance


class TestEuclideanDistance(unittest.TestCase):

    def test_euclidean_distance(self):
        # # test with two points with same coordinates
        self.assertEqual(euclidean_distance((0, 0), (0, 0)), 0)

        # # test with two points with different coordinates
        self.assertEqual(euclidean_distance((0, 0), (3, 4)), 5)

        # test with three points
        self.assertEqual(euclidean_distance((0, 0), (3, 4), (6, 8)), 10)

        # test with four points
        self.assertEqual(euclidean_distance((0, 0), (3, 4), (6, 8), (9, 12)), 15)
