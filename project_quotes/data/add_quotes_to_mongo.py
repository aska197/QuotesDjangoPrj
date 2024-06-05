import json
from bson.objectid import ObjectId
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Access the project_quotes database
db = client.project_quotes

# Read the quotes from the JSON file
with open('data/quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

# Check if quotes are already present in the database
existing_quotes = db.quotes.find({}, {'_id': 0, 'quote': 1})
existing_quotes_text = {quote['quote'] for quote in existing_quotes}

# Iterate through the quotes and insert them into the database if they are not already present
for quote in quotes:
    if quote['quote'] not in existing_quotes_text:
        # Find the author in the authors collection
        author = db.authors.find_one({'fullname': quote['author']})
        if author:
            # Insert the quote into the quotes collection
            db.quotes.insert_one({
                'quote': quote['quote'],
                'tags': quote['tags'],
                'author': ObjectId(author['_id'])
            })
        else:
            print(f"Author {quote['author']} not found in database")

print("Quotes have been imported successfully.")
