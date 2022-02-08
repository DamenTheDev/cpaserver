# Flask server for the Club Penguin API
# Will be used to interact with the database and the world servers
#
# Infrastructure:
# - API server          (Used for: logging in, registering, and getting penguin data)
# - Database server     (Used for: storing and retrieving penguin data)
# - World servers       (Used for: streaming world events to and from clients)
# - Game servers        (Used for: streaming game events to and from clients)
# - Website             (Hosts the client)
#
# Logging in:
# - User visits the website /login
# - User enters their username and password
# - The website sends a request to the API server (POST /account/login, with the username and password)
# - The API server checks the database for the username and password then returns a token
# - The website stores the token in a cookie
# - The website sends the user to the client
#
# Registering:
# - User visits the website /register
# - User fills out the create-a-penguin form (username, password, email, penguin colour, captcha)
# - The website sends a request to the API server (POST /account/register, with the username, password, email, penguin colour, and captcha)
# - The API server verifies the captcha and then creates a new account by adding the username, password, email and penguin colour to the database
# - The website sends the user to /login
#
# API endpoints:
# - /account/login
#     - POST:
#         - username
#         - password
#         - returns a token to be stored in a cookie and used for future requests
# - /account/register
#     - POST:
#         - username
#         - password
#         - email
#         - penguin colour
#         - captcha
#         - returns a token to be stored in a cookie and used for future requests (granted the captcha was correct)
# - /account/logout
#     - POST:
#         - token
#         - returns a success message
# - /account/buddies
#     - GET:
#         - token
#         - returns a list of buddies retrieved from the database
# - /account/buddies/request
#     - POST:
#         - token
#         - username
#         - returns a buddy request token
# - /account/buddies/accept
#     - POST:
#         - token
#         - buddy request token
#         - returns a success message
# - /account/buddies/decline
#     - POST:
#         - token
#         - buddy request token
#         - returns a success message
# - /account/buddies/remove
#     - POST:
#         - token
#         - username
#         - returns a success message
# - /account/penguin/get
#     - GET:
#         - token
#         - username
#         - returns a penguin object if it exists
# - /account/penguin/inventory
#     - GET:
#         - token
#         - returns a list of inventory items
# - /account/penguin/inventory/igloo
#     - GET:
#         - token
#         - returns a list of igloo items
# - /account/penguin/inventory/puffle
#     - GET:
#         - token
#         - returns a list of puffle items
# - /account/penguin/puffles
#     - GET:
#         - token
#         - returns a list of puffle objects
# - /account/penguin/puffle/get
#     - GET:
#         - token
#         - puffle id
#         - returns a puffle object

import os
import sys
import json
import time
import random
import string
import hashlib
import requests
import sqlite3
import flask
import flask_login
import flask_bcrypt
import flask_socketio
import flask_cors
import flask_sqlalchemy
import flask_migrate


# Import the database models
from models import *


# Import the configuration
from config import *


# Import the utilities
from utilities import *


# Import the API endpoints
from endpoints import *


