from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.2caednd.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
