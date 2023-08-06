import os
import logging
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
INBOUND_QUEUE = os.getenv("INBOUND_QUEUE")
OUTBOUND_QUEUE = os.getenv("OUTBOUND_QUEUE")

# Set up logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="app.log",
)
