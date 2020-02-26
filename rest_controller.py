from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import controller
import sys
from olympe.messages.ardrone3.Piloting import Landing


app = Flask(__name__)
CORS(app)

drone = None # Global drone vriable

@app.route('/', methods=['POST'])
def hello_world():
    return jsonify({
        'message': f'Hello world!'
    }), 200

@app.route('/connectToDrone', methods=['POST'])
def connect_to_drone():
    global drone

    try:
        drone = controller.get_drone('192.168.42.1')
        connection = drone.connection()

        if connection[0]:
            return jsonify({
                'message': 'Connected to drone'
            }), 200
        else:
            return jsonify({
                'message': 'Could not connect to drone'
            }), 200
        
    except:
        print('error')

        return jsonify({
            'message': 'Could not connect to drone',
            'error' : sys.exc_info()[0]
        }), 500

@app.route('/getPosition', methods=['POST'])
def get_position():
    try:
        position = controller.position(drone)
        return jsonify({
            'message': f'Drone is at position: {position}'
        })
    except:
        return jsonify({
            'message': 'Could not get drone position',
            'error' : sys.exc_info()[0]
        }), 500

@app.route('/takeOff', methods=['POST'])
def take_off():
    try:
        controller.takeoff(drone)
        return jsonify({
            'message': 'Drone is taking off'
        })
    except:
        drone(Landing()).wait()
        return jsonify({
            'message': 'Failed when trying to take off. Landing...',
            'error': sys.exc_info()[0]
        }), 500

@app.route('/moveTo', methods=['POST'])
def move_to():
    try:
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        altitude = request.json['altitude']

        controller.moveto(drone, latitude, longitude, altitude, 0, 0)
        return jsonify({
            'message': f'Flying to lat: {latitude}, long: {longitude}, alt: {altitude}'
        }), 200
    except:
        drone(Landing()).wait()
        return jsonify({
            'message': 'Failed when trying to fly to GPS coordinates. Landing...',
            'error': sys.exc_info()[0]
        }), 500

@app.route('/moveBy', methods=['POST'])
def move_by():
    try:
        # Needs translation because of different labels between drone api and unity 
        x_movement = request.json['z_movement']
        y_movement = request.json['x_movement']
        z_movement = -request.json['y_movement']

        controller.moveby(drone, x_movement, y_movement, z_movement)
        return jsonify({
            'message': f'Flying {x_movement} in x direction, {y_movement} in y direction, {z_movement} in z direction'
        }), 200
    except:
        drone(Landing()).wait()
        return jsonify({
            'message': 'Failed when trying to fly to move drone. Landing...',
            'error': sys.exc_info()[0]
        }), 500
    

@app.route('/flyBackward', methods=['POST'])
def flyBackwards():
    controller.moveby(drone,-1,0,0,0)
    return 'flying 1 meter backwards'

@app.route('/flyForward', methods=['POST'])
def flyForwards():
    controller.moveby(drone,1,0,0,0)
    return 'flying 1 meter forwards'

@app.route('/land', methods=['POST'])
def land():
    try:
        controller.land(drone)
        return jsonify({
            'message': 'Landing drone.'
        }), 200
    except:
        return jsonify({
            'message': 'Failed when trying to land drone.',
            'error': sys.exc_info()[0]
        }), 500
    

@app.route('/disconnect', methods=['POST'])
def disconnect():
    try:
        controller.disconnect(drone)
        return jsonify({
            'message': 'Disconnected from drone.'
        }), 200
    except:
        return jsonify({
            'message': 'Failed when trying to disconnect from drone.',
            'error': sys.exc_info()[0]
        }), 500
    