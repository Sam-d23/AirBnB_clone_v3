#!/usr/bin/python3
"""
The blueprints app is in this file
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def api_status():
    """The status of the api is returned"""
    response = {'status': "OK"}
    return jsonify(response)


@app.route('/stats')
def get_stats():
    """The no. of items in classes is returned"""
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State')
    }

    return jsonify(stats)
