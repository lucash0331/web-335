#
#========================================================================================================
# Title: Assignment 9.3 Updating and deleting documents
# Author: Lucas Hoffman
# Date: December 17, 2021
# Description: Updating and deleting documents in a MongoDB database instance through Python and pymongo.
#=========================================================================================================
#

# Imports
from pymongo import MongoClient
import pprint
import datetime

# Connect to MongoDB using local host 27017.
client = MongoClient('localhost', 27017)
db = client.web335

# Update user email from users collection using the update_one() method to my Bellevue University account.
db.users.update_one(
    {"employee_id": "69896989"},
    {
        "$set": {
            "email": "luhoffman@my365.bellevue.edu"
        }
    }
)

# Query the users collection using find_one() method
pprint.pprint(db.users.find_one({"employee_id": "69896989"}))
