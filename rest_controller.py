from flask import Flask
import controller

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
    return 'Connecting to drone'


@app.route('/getPosition')
def get_position():
    return controller.position(drone)

@app.route('/takeOff')
def take_off():
    controller.takeoff(drone)
    return 'taking off'

@app.route('/land')
def land():
    controller.land(drone)
    return 'landing'