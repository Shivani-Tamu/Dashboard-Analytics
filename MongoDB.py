# This program makes a connection to MongoDB
# Importing python driver PyMongo for MongoDB
# The URL format has to be: Host Name, Password, Username:Port number
from pymongo import MongoClient

client = MongoClient("mongodb://Host-Name:Password==@Username.azure.com:10255/DBName?ssl=true")

db = (client['logs'].get_collection('data'))
# logs is the db and data is the collection

t = db.find()
no_of_documents = 0
for data in t:
    print(data)
    no_of_documents += 1

print(no_of_documents)
