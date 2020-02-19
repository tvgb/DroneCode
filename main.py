from __future__ import print_function
from controller import get_drone, set_gimbal, position, takeoff, land
import time
from olympe.messages.ardrone3.PilotingState import PositionChanged

print('Creating drone')
drone = get_drone('192.168.42.1')
drone.connection()
print('Drone created \n')

position(drone)

time.sleep(3)

takeoff(drone)

time.sleep(3)

land(drone)

time.sleep(10)

drone.disconnection()
