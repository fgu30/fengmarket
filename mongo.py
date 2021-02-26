from pymongo import MongoClient
from twitter import twitteranalyze

client = MongoClient("mongodb+srv://gufengmsa:daxia504@cluster0.24r91.mongodb.net/sentiment?retryWrites=true&w=majority")
db = client.get_database('sentiment')
twitterCollection = db.get_collection('twitter')

def fetchData(ticker:str):
    return  twitterCollection.find_one({"ticker":ticker})

    
    