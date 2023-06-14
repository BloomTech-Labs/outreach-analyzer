from bson.objectid import ObjectId
from pymongo import UpdateOne


def find_timestamp(mongo_id: ObjectId):
    today = mongo_id.generation_time
    return today.isoformat()


def add_timestamp(mongo_db):
    bulk_ops = []
    for doc in mongo_db.collection.find({}):
        if "timestamp" not in doc.keys():
            timestamp = find_timestamp(doc["_id"])
            op_to_add = UpdateOne(
                {"_id": doc["_id"]},
                {"$set": {"timestamp": timestamp}}
            )
            bulk_ops.append(op_to_add)
            mongo_db.collection.bulk_write(bulk_ops)
