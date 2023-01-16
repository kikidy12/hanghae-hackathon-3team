from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(
        "mongodb+srv://test:sparta@cluster0.zphghpj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.recommendbook


