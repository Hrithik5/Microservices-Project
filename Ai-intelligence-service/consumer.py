import json
from app import analyze_media
from events import publish_event

def on_message(channel, method, properties, body):
    event = json.loads(body)
    analyze_media(event)
    channel.basic_ack(delivery_tag=method.delivery_tag)