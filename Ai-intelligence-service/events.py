import json
import pika
from config import RABBITMQ_URL

def publish_event(event_type: str, payload: dict):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.basic_publish(
        exchange="",
        routing_key="media_events",
        body=json.dumps({
            "event_type": event_type,
            "payload": payload
        })
    )
    connection.close()
