#
#=======================================================
# Title: Assignment 9.2 Querying and Creating Documents
# Author: Lucas Hoffman
# Date: December 17, 2021
# Description: Query and create documents in a MongoDB database instance through Python and pymongo
#=======================================================
#

# Imports for the assignment
from pymongo import MongoClient
import pprint
import datetime

# Connect to MongoDB using local host 27017
client = MongoClient('localhost', 27017)
db = client.web335

# Creating a new User document
user = {
    "first_name": "Lucas",
    "last_name": "Hoffman",
    "email": "Lucas@hoffman.com",
    "employee_id": "69896989",
    "date_created": datetime.datetime.utcnow()
}

# Insert new user document into users database
user_id = db.users.insert_one(user).inserted_id

# Output auto-generated user_id
print(user_id)

# Query users collection with find_one() method
pprint.pprint(db.users.find_one({"employee_id": "69896989"}))
