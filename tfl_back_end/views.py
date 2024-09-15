from flask import Flask, jsonify, request
from algo import *
from utils import name_to_coordinates, get_nearest_station
from create_stations import create_stations
from cache_client import station_cache
import json


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask("TFL_Back_End")

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/find_optimal_path', methods=['GET'])
def find_optimal_path():
    # Get 'start' and 'end' from query parameters
    start = request.args.get('start')
    end = request.args.get('end')
    
    if not start or not end:
        return jsonify({"error": "Please provide both start and end locations."}), 400

    # Find nearest station to start location
    start_loc = name_to_coordinates(start)
    start_station = get_nearest_station(start_loc)

    # Find nearest station to end location
    end_loc = name_to_coordinates(end)
    end_station = get_nearest_station(end_loc)
    
    # Find shortest path using A* search
    shortest_path = a_star_search(start_station, end_station)

    return shortest_path  # Return JSON response

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()