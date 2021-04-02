from pymongo import MongoClient
import json

#Connect
client = MongoClient('localhost', 27017)
#Create database
db = client.poshmark_db
#Create collection
sold_clutches_coll = db.sold_clutches
sold_clutches_coll.drop()
#Insert file
file = json.load(open('posh_data_new.txt'))
#Set Collection to equal the file
sold_clutches_coll.insert_many(file)
docs = sold_clutches_coll.find()
#Check collection length and first 100
print(sold_clutches_coll.count())
for doc in docs[:100]:
    print(doc)