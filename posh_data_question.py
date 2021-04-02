from pymongo import MongoClient
import json

#Connect
client = MongoClient('localhost', 27017)
db = client.poshmark_db
coll = db.sold_clutches

#Rename the steve madden with a space after
db.sold_clutches.update_many(
    {'brand':'steve madden '},
    {'$set': {'brand':'steve madden'}}
)


#Verify counts for all
coach_count = coll.count_documents({'brand': 'coach'})
sm_count = coll.count_documents({'brand': 'steve madden'})
lv_count = coll.count_documents({'brand': 'louis vuitton'})
print('Coach: {}, Steve Madden: {}, Louis Vuitton: {}'.format(coach_count, sm_count, lv_count))

#How many listings did not have a condition set?
null_cond = coll.count_documents({'condition': ''})
nwt_cond = coll.count_documents({'condition': 'nwt'})
not_nwt_cond = coll.count_documents({'condition': 'not_nwt'})
ret_cond = coll.count_documents({'condition': 'ret'})
print('No condition listed: {} \nNew with tags: {} \nUsed: {}\nRet: {}'.format(
    null_cond, nwt_cond, not_nwt_cond, ret_cond))

#Get the average selling price per brand
avg_price = db.sold_clutches.aggregate([
    {
        '$group': {
            '_id':'$brand',
            'avg_price': {'$avg': '$sell_price'
                         }
        }
    }
])

for doc in avg_price: print('Brand: {}, Average Price: ${:.2f}'.format(doc['_id'], doc['avg_price']))

