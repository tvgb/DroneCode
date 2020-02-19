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

