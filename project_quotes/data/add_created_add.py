import pymongo
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["project_quotes"]

# Update authors collection
authors_collection = db["authors"]
authors_collection.update_many(
    {"created_at": {"$exists": False}},
    {"$set": {"created_at": datetime.now()}}
)

# Update quotes collection
quotes_collection = db["quotes"]
quotes_collection.update_many(
    {"created_at": {"$exists": False}},
    {"$set": {"created_at": datetime.now()}}
)

print("Created_at field added to authors and quotes collections.")
