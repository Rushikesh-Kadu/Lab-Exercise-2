from pymongo import *



client = MongoClient(host="mongodb://localhost:27017")
collection = client['practical']['emp']
collection.insert_many( [{'Name':"M.S Dhoni","Profession":"Cricketor"},{'Name':'Guido van Rossum','Profession':'Creator'}] )    # Inserting/creating Record

d1={'Name':'Suyog','Profession':'Actor',"Height":'6.1'}
collection.update_one({"Name":'John'},{'$set':d1})          # Updating Record

collection.delete_one({'Name':'Suyog'})                 # Deleting Record

for record in collection.find():        # Reading Record
    print(record)