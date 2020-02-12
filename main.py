from __future__ import print_function
from controller import get_drone, set_gimbal
import time
from olympe.messages.ardrone3.PilotingState import PositionChanged
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged
from olympe.messages.ardrone3.Piloting import TakeOff
from olympe.messages.ardrone3.GPSSettingsState import HomeChanged

print('Creating drone')
drone = get_drone('192.168.42.1')
drone.connection()
print('Drone created \n')

drone(GPSFixStateChanged(_policy = 'wait'))

print("GPS position before take-off :", drone.get_state(HomeChanged))

print('Setting gimbal')
set_gimbal(drone, "position", 0.0, 0.0, 0.0)
print('Gimbal set')

time.sleep(3)

print('Setting gimbal')
set_gimbal(drone, "velocity", 10.0, 0.0, 0.0)
print('Gimbal set')

time.sleep(1)

print('Setting gimbal')
set_gimbal(drone, "position", 0.0, 0.0, 0.0)
print('Gimbal set')

