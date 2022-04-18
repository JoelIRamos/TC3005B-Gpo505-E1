import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://JoelIRamosH:JoelI@cluster0.htyzr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["TernData"]