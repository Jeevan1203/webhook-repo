from pymongo import MongoClient

client = MongoClient("mongodb+srv://adapajeevan333:jeevan%401435@cluster0.bzhqmp6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["webhook_db"]
collection = db["events"]
