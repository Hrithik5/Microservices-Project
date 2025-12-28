from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
collection = client.media_platform.media_metadata

def save_metadata(metadata: dict):
    collection.update_one(
        {"media_id": metadata["media_id"]},
        {"$set": metadata},
        upsert=True
    )
