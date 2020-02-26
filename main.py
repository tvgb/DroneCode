from __future__ import print_function
from controller import get_drone, set_gimbal, position, takeoff, land
import time
from olympe.messages.ardrone3.PilotingState import PositionChanged

if __name__ == '__main__':

    try:
        print('Creating drone')
        drone = get_drone('192.168.42.1')

        drone.connection()
        print('Established connection')

        controller.stream(drone)


    finally:

        time.sleep(10)

        drone.disconnection()
    

