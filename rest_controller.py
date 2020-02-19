from flask import Flask
import controller
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing, moveTo

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
    print('gimbal state: ',olympe.enums.gimbal.state)
    return 'Connecting to drone'

@app.route('/getPosition')
def get_position():
    return controller.position(drone)

@app.route('/takeOff')
def take_off():
    controller.takeoff(drone)
    return 'taking off'

@app.route('/flyBack')
def flyBackwards():
    drone.moveby(drone,-1,0,0,0)
    return 'flying 1 meter backwards'

@app.route('/flyForward')
def flyForwards():
    drone.moveby(drone,1,0,0,0)
    return 'flying 1 meter forwards'

@app.route('/land')
def land():
    controller.land(drone)
    return 'landing'