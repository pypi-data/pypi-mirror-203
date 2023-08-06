import json

from src.solver.tsp_solver import optimize_tsp
from src.config import OUTBOUND_QUEUE


# Define a function to handle incoming messages
def process_message(channel, method, _properties, body):
    # Convert the message payload to a Python object
    payload = json.loads(body)

    # Extract the locations from the payload
    locations = payload["locations"]

    # Solve the TSP problem
    solution = optimize_tsp(locations)

    # Prepare the message payload for the outbound queue
    outbound_payload = {
        "locations": locations,
        "path": solution,
    }

    # Convert the payload to a JSON string
    outbound_message = json.dumps(outbound_payload)

    # Publish the message to the outbound queue
    channel.basic_publish(
        exchange="", routing_key=OUTBOUND_QUEUE, body=outbound_message
    )

    # Acknowledge the message
    channel.basic_ack(delivery_tag=method.delivery_tag)
