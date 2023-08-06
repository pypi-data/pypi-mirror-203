import os
import sys
import pika
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.messaging.inbound import process_message
from src.config import RABBITMQ_HOST, INBOUND_QUEUE

logger = logging.getLogger(__name__)

# Define the RabbitMQ connection parameters
params = pika.ConnectionParameters(host=RABBITMQ_HOST)

# Connect to RabbitMQ and set up the inbound and outbound queues
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=INBOUND_QUEUE)

# Set up a consumer for the inbound queue
channel.basic_consume(queue=INBOUND_QUEUE, on_message_callback=process_message)

# Start consuming messages from the inbound queue
logger.debug("Start consuming messages from the inbound queue")
channel.start_consuming()
