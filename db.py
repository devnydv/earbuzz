from pymongo.mongo_client import MongoClient
import requests
from dotenv import load_dotenv, find_dotenv
import os
envpath = find_dotenv()
load_dotenv(envpath)
url = os.getenv('db')


api = url

client = MongoClient(api)
db = client.earbuzz
collection = db.item
detailsdb = db.details

def inddata():
    home = list(collection.find().limit(16))
    return home

def catdata(cat):
    filtered = list(collection.find({"cat": cat}))
    filtered.reverse()
    return filtered

def itemdetails(id):
    details = list(detailsdb.find({"id": id}))
    return details

