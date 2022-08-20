
from distutils.log import debug
from flask import Flask
from pymongo import MongoClient

api = Flask(__name__)

# Get MongoDB Client
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    
    db = client["animal_db"]
    return db

if __name__=='__main__':
    api.run(host="0.0.0.0", port=5000, debug=True)