from controller import get_drone, set_gimbal
import time


print('Creating drone')
drone = get_drone('192.168.42.1')
drone.connection()
print('Drone created \n')

print('Setting gimbal')
set_gimbal(drone, 0.0, 0.0, 0.0)
print('Gimbal set')

time.sleep(1)

print('Setting gimbal')
set_gimbal(drone, 45.0, 45.0, 45.0)
print('Gimbal set')

