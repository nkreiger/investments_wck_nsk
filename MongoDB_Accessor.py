from pymongo import MongoClient
import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://Chaz:Chaz@eps-estimates.3emue.azure.mongodb.net/sample_airbnbtrue&w=majority")
db = client.test
mydb = client["sample_analytics"]
print(mydb.list_collection_names())


class Connect(object):
    @staticmethod
    def get_connection():
        return pymongo.MongoClient("mongodb+srv://Chaz:Chaz@eps-estimates.3emue.azure.mongodb.net/eedb&w=majority")


connection = Connect.get_connection()

