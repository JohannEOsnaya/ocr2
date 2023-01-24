# Connecting to the MongoDB database.
from pymongo import MongoClient
from config.keys import MongoCli

conn = MongoClient(MongoCli['docker'])