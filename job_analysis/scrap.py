user = 'dev'
password = 'dev'
import pymongo
client = pymongo.MongoClient(f'mongodb+srv://{user}:{password}@cluster0.pjvh9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.playground
mycol = db.job_offers
# Tutaj scripting
# mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

