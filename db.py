from pymongo.mongo_client import MongoClient
import requests
api = "mongodb+srv://bittumail:12356789@cluster0.fqrswkj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(api)
db = client.earbuzz
collection = db.item
detailsdb = db.details

def inddata():
    home = list(collection.find().limit(16))
    return home

def catdata(cat):
    filtered = list(collection.find({"cat": cat}))
    return filtered

def itemdetails(id):
    details = list(detailsdb.find({"id": id}))
    return details

