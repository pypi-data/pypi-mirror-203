import os
import sys
import json
import unittest
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.messaging.inbound import process_message

OUTBOUND_QUEUE = "tsp.outbound"

class TestProcessMessage(unittest.TestCase):
    def test_process_message(self):
        # Define the input message
        input_message = {
            "locations": [[0, 0], [1, 1], [2, 2], [3, 3]],
        }
        input_message_json = json.dumps(input_message)

        # Define the expected output message
        expected_output_message = {
            "locations": [[0, 0], [1, 1], [2, 2], [3, 3]],
            "path": [[0, 0], [3, 3], [2, 2], [1, 1], [0, 0]],
        }
        expected_output_message_json = json.dumps(expected_output_message)

        # Set up the mock channel object
        mock_channel = mock.MagicMock()

        
        # Create a pika.spec.Basic.Deliver object to pass into process_message()
        method = mock.Mock()
        method.delivery_tag = 1

        # Call the function with the input message
        process_message(mock_channel, method, None, input_message_json)

        # Check that the mock channel's basic_publish method was called with the expected arguments
        mock_channel.basic_publish.assert_called_once_with(
            exchange="", routing_key=OUTBOUND_QUEUE, body=expected_output_message_json
        )

        # Check that the mock channel's basic_ack method was called with the expected argument
        mock_channel.basic_ack.assert_called_once_with(delivery_tag=1)
