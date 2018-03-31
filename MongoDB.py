# This program makes a connection to MongoDB
# Importing python driver PyMongo for MongoDB
# The URL format has to be: Host Name, Password, Username:Port number
from pymongo import MongoClient

client = MongoClient("mongodb://xpressit-sample-data:ioUgLmN27dgfqjnnCfaWVH2HhSbbWJJIOpg539jHmWCjaQzLaM8npfj4lZdzbVDB5I76bGr05iHoYRWrrrMVCQ==@xpressit-sample-data.documents.azure.com:10255/logs?ssl=true")

db = (client['logs'].get_collection('data'))
# logs is the db and data is the collection

t = db.find()
no_of_documents = 0
for data in t:
    print(data)
    no_of_documents += 1

print(no_of_documents)



# import pymongo
# from pymongo import MongoClient
#
# # pprint library is used to make the output look more pretty
# from pprint import pprint
# # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# client1 = MongoClient("mongodb://xpressit-sample-data:ioUgLmN27dgfqjnnCfaWVH2HhSbbWJJIOpg539jHmWCjaQzLaM8npfj4lZdzbVDB5I76bGr05iHoYRWrrrMVCQ==@xpressit-sample-data.documents.azure.com:10255/logs?readPreference=primary&ssl=true")
# #client =MongoClient("xpressit-sample-data.documents.azure.com:10255")
# client2=(client1['logs'].get_collection('data'))
