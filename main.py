from controller import get_drone, set_gimbal


print('Creating drone')
drone = get_drone('192.168.42.1')
print('Drone created \n')

print('Setting gimbal')
set_gimbal(drone, 45, 45, 45)
print('Gimbal set')
