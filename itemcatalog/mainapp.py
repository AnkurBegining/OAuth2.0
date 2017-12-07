from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Items, User

# Step -1
# New imports for this step
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show all restaurants
@app.route('/')
@app.route('/categories/')
def showRestaurants():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('main.html', categories=categories)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5001)