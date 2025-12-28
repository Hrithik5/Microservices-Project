import json

def publish_event(event_type, payload):
    message = {
        "event_type": event_type,
        "payload": payload
    }
    rabbitmq_channel.basic_publish(
        exchange="",
        routing_key="media_events",
        body=json.dumps(message)
    )
