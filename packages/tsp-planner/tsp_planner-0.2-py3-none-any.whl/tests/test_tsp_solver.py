import unittest
from src.solver.tsp_solver import optimize_tsp
from src.utils.distance import euclidean_distance


class TestTspSolver(unittest.TestCase):

    def test_optimize_tsp_with_3_locations(self):
        locations = [(0, 0), (3, 0), (0, 4)]
        expected_tour = [(0, 0), (0, 4), (3, 0), (0, 0)]
        actual_tour = optimize_tsp(locations)
        self.assertEqual(actual_tour, expected_tour)

    def test_optimize_tsp_with_4_locations(self):
        locations = [(0, 0), (1, 0), (2, 0), (0, 1)]
        expected_tour = [(0, 0), (0, 1), (2, 0), (1, 0), (0, 0)]
        actual_tour = optimize_tsp(locations)
        self.assertEqual(actual_tour, expected_tour)

    def test_optimize_tsp_with_5_locations(self):
        locations = [(0, 0), (1, 0), (2, 0), (2, 1), (0, 1)]
        expected_tour = [(0, 0), (0, 1), (2, 1), (2, 0), (1, 0), (0, 0)]
        actual_tour = optimize_tsp(locations)
        self.assertEqual(actual_tour, expected_tour)
