import os
import logging
from ortools.constraint_solver import routing_enums_pb2, pywrapcp

logger = logging.getLogger(__name__)


def create_data_model(locations):
    """Stores the data for the problem."""
    data = {}
    data["locations"] = locations
    data["num_locations"] = len(locations)
    data["depot"] = 0
    return data


def compute_euclidean_distance_matrix(locations):
    """Computes the pairwise distance matrix between locations."""
    matrix = []
    for i, location_i in enumerate(locations):
        row = []
        for j, location_j in enumerate(locations):
            if i == j:
                row.append(0)
            else:
                distance = (
                    (location_i[0] - location_j[0]) ** 2
                    + (location_i[1] - location_j[1]) ** 2
                ) ** 0.5
                row.append(distance)
        matrix.append(row)
    return matrix


def optimize_tsp(locations):
    """Optimizes the TSP problem and returns the optimized tour."""
    data = create_data_model(locations)
    distance_matrix = compute_euclidean_distance_matrix(locations)

    # Create routing model
    manager = pywrapcp.RoutingIndexManager(data["num_locations"], 1, data["depot"])
    routing = pywrapcp.RoutingModel(manager)

    transit_callback_index = routing.RegisterTransitCallback(
        lambda i, j: distance_matrix[i][j]
    )
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    logger.debug(
        f"Locations of the problem: {locations}"
        + os.linesep
        + f"The solution:{solution}"
    )

    # Extract the optimized tour
    tour = []
    index = routing.Start(0)
    while not routing.IsEnd(index):
        tour.append(data["locations"][index])
        index = solution.Value(routing.NextVar(index))
    tour.append(data["locations"][0])

    return tour
