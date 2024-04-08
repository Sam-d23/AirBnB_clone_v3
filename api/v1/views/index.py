#!/usr/bin/python3
"""
The blueprints app is in this file
"""
from api.v1.views import app_views
from flask import jsonify
from ..app import app
from models.engine.db_storage import *


@app_views.route('/status')
def status():
    """The status of the api is returned"""
    return jsonify({"status": "OK"})


@app.route('/api/v1/stats')
def retrieve():
    """The no. of items in classes is returned"""
    new_dictionary = {}
    for obj in classes:
        total = count(obj)
        new_dictionary[obj] = total
    return jsonify(new_dictionary)
