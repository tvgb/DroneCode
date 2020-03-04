from flask import Flask, jsonify, request, render_template, Response
from flask_cors import CORS, cross_origin
import controller
import sys
from PIL import Image
from olympe.messages.ardrone3.Piloting import Landing
from haversine import haversine, Unit

app = Flask(__name__)
CORS(app)

drone = None # Global drone vriable

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


def gen():
    while True:
        frame = Image.open('static/images/random.jpg')
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed', methods=['GET'])
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


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
            'message': f'Drone is at position: {position}',
            'position': position 
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
    
    maxDistanceMoved = 5

    try:
        dronePos = controller.position(drone)
        drone_latitude = dronePos['latitude']
        drone_longitude = dronePos['longitude']
        drone_altitude = dronePos['altitude']

        print(drone_latitude, drone_longitude, drone_altitude)

        destination_latitude = float(request.json['latitude'].replace(',', '.'))
        destination_longitude = float(request.json['longitude'].replace(',', '.'))
        destination_altitude = float(request.json['altitude'].replace(',', '.'))

        startPos = (drone_latitude, drone_longitude)
        endPos = (destination_latitude, destination_longitude)

        print(type(destination_latitude))
        print(type(drone_latitude))

        if (haversine(startPos, endPos, unit=Unit.METERS) < maxDistanceMoved):
            print(haversine(startPos, endPos, unit=Unit.METERS))
            #controller.moveto(drone, drone_latitude, drone_longitude, altitude, 0, 0)
            #controller.moveto(drone, latitude, longitude, drone_altitude, 0, 0)
            return jsonify({
                'message': f'Position before flight: {drone_latitude}, long: {drone_longitude}, alt: {drone_altitude}',
                'message2': f'Flying {round(haversine(startPos, endPos, unit=Unit.METERS),3)} meters',
            }), 200
        else:
            return jsonify({
                'message': f'Distance is {round(haversine(startPos, endPos, unit=Unit.METERS),3)} meters, please choose a distance shorter than {maxDistanceMoved} meters.'
            })
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
        rotation = request.json['rotation']

        controller.moveby(drone, x_movement, y_movement, z_movement, rotation)
        return jsonify({
            'message': f'Moving x dir: {x_movement}, y dir: {y_movement}, z dir: {z_movement}, rotation: {rotation}'
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
    
