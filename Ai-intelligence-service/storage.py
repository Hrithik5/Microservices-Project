from db import collection

def save_metadata(metadata):
    collection.update_one(
        {"media_id": metadata["media_id"]},
        {"$set": metadata},
        upsert=True
    )
