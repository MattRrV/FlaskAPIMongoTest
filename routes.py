from distutils.log import debug
from http import client
import json
from api import get_db
from flask import Flask, jsonify
from pymongo import MongoClient

# Initiate Flask api
api = Flask(__name__)

# Routes
@api.route('/')
def ping_server():
    {"welcome":  "Welcome to the world of Mongo!"}
    return json.dumps({"welcome":  "Welcome to the world of Mongo!"})

@api.route('/animals' , methods=['GET'])
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.animal_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@api.route('/animals/wild', methods=['GET'])
def get_wild_animals():
    db=""
    try:
        db = get_db()
        wild_animals = db.animal_tb.query.filter_by(type='Wild')
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in wild_animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()
