from flask import Flask, jsonify
import controller
#from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing, moveTo


app = Flask(__name__)

drone = None # Global drone vriable

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/connectToDrone')
def connect_to_drone():
    global drone
    drone = controller.get_drone('192.168.42.1')
    drone.connection()
    # print('gimbal state: ', olympe.enums.gimbal.state)
    return 'Connecting to drone'

@app.route('/getPosition')
def get_position():
    return controller.position(drone)

@app.route('/takeOff')
def take_off():
    controller.takeoff(drone)
    return 'taking off'

@app.route('/moveTo/<float:latitude>/<float:longitude>/<float:altitude>')
def move_to(latitude, longitude, altitude):
    controller.moveto(drone, latitude, longitude, altitude, 0, 0)
    return jsonify({
        'message': f'Flying to lat: {latitude}, long: {longitude}, alt: {altitude}'
    }), 200

@app.route('/moveBy/<float:x>/<float:y>/<float:z>')
def move_by(x, y, z):
    controller.moveby(drone, x, y, z)
    return jsonify({
        'message': f'Flying {x} in x direction, {y} in y direction, {z} in z direction'
    }), 200

@app.route('/flyBackward')
def flyBackwards():
    controller.moveby(drone,-1,0,0,0)
    return 'flying 1 meter backwards'

@app.route('/flyForward')
def flyForwards():
    controller.moveby(drone,1,0,0,0)
    return 'flying 1 meter forwards'

@app.route('/land')
def land():
    controller.land(drone)
    return 'landing'

@app.route('/disconnect')
def disconnect():
    return jsonify({
        'message': 'Disconnected from drone'
    }), 200