import pymongo
import frappe

_client = None

def get_db():
    global _client
    if _client is None:
        mongo_uri = frappe.conf.get("mongodb_uri") or "mongodb://127.0.0.1:27017/"
        _client = pymongo.MongoClient(mongo_uri)
    return _client["employee_db"]

def get_collection(collection_name):
    return get_db()[collection_name]
