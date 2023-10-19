from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost:27017/")
database = mongoClient.assassins
players = database.players
jobs = database.jobs