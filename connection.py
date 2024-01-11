import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

try:
    ok = client.admin.command("ping")
except PyMongoError as e:
    print("Cannot connect to db:", e)

# client.close()
