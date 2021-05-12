# ========================================
# Title: Exercise 9.2
# Author: Eunice Lim
# Date: 12 May 2021
# Description: Exercise 9.3 Querying and Creating Documents
# ========================================


#import pymongo, pprint, datetime
from pymongo import MongoClient
import pymongo
import pprint
import datetime

#connect to MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

#create new user document
user = {
    "first_name": "Franz",
    "last_name": "Schubert",
    "email": "fschubert@me.com",
    "employee_id": "0000010",
    "date_created": datetime.datetime.utcnow()
}
#insert user document
user_id = db.users.insert_one(user).inserted_id

#print/output user_id
print(user_id)

#print/output using find_one query
pprint.pprint(db.users.find_one({"employee_id": "0000010"}))