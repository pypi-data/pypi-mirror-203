import os
import sys
import unittest
from io import StringIO
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.messaging.outbound import callback


class TestCallback(unittest.TestCase):
    def test_callback(self):
        # Create mock objects for the channel and the method
        channel_mock = MagicMock()
        method_mock = MagicMock(delivery_tag='mock_delivery_tag')

        # Create a mock message body
        message_body = b'Test message'

        # Redirect the standard output to a string buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the callback function with the mock objects
        callback(channel_mock, method_mock, None, message_body)

        # Restore the standard output
        sys.stdout = sys.__stdout__

        # Get the printed output as a string
        print_calls = captured_output.getvalue()

        # Assert that the message body was decoded and printed correctly
        channel_mock.basic_ack.assert_called_once_with(delivery_tag='mock_delivery_tag')
        self.assertEqual(channel_mock.basic_ack.call_count, 1)

        # Check that the printed message contains the expected string
        self.assertIn('Optimized Tour:', print_calls)

        # Check that the printed message contains the decoded message body
        self.assertIn(message_body.decode(), print_calls)  
