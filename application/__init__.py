import os
from flask import Flask, render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from application.forms import LoginForm, RegisterForm
from config import Config
from flask_mongoengine import MongoEngine


app = Flask(__name__)
#app.register_error_handler(404, page_not_found)
app.config.from_object(Config)



app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes

if __name__ == '__main__':
    app.run(host=os.envriron.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
