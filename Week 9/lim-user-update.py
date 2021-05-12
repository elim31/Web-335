# ========================================
# Title: Exercise 9.3
# Author: Eunice Lim
# Date: 12 May 2021
# Description: Exercise 9.3 Updating and Deleting Documents
# ========================================


#import MongoClient, pprint, datetime
from pymongo import MongoClient
import pymongo
import pprint
import datetime

#connect to MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

#update email address
db.users.update_one(
    {"employee_id": "0000010"},
    {
        "$set": {
            "email": "euelim@my365.bellevue.edu"
        }
    }
)

#print/output
pprint.pprint(db.users.find_one({"email": "euelim@my365.bellevue.edu"}))
