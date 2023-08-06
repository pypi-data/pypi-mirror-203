from typing import List
from math import sqrt


def euclidean_distance(*locations: List[float]) -> float:
    """
    Calculates the Euclidean distance between any number of locations.
    """
    if len(locations) < 2:
        raise ValueError(
            "At least two locations are required to calculate the Euclidean distance."
        )
    distance = 0
    for i in range(len(locations) - 1):
        squared_distance = sum(
            (p1 - p2) ** 2 for p1, p2 in zip(locations[i], locations[i + 1])
        )
        distance += sqrt(squared_distance)
    return distance
