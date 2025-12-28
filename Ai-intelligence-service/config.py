import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

RABBITMQ_URL = os.getenv(
    "RABBITMQ_URL", "amqp://guest:guest@localhost:5672/"
)
QUEUE_NAME = os.getenv("QUEUE_NAME", "MediaProcessingCompleted")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
