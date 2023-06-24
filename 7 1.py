from pymongo import *


client = MongoClient(host="mongodb://localhost:27017")
collection = client['practical']['emp']
collection.insert_one({"Name":'RK',"Profession":'Django+React'})
collection.insert_one({"Name":'John',"Profession":'SpringBoot'})
collection.insert_one({"Name":'Bob',"Profession":'NodeJs'})
collection.insert_one({"Name":'Seth',"Profession":'Linux'})
collection.insert_one({"Name":'Nick',"Profession":'Device Drivers'})