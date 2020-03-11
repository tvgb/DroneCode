from __future__ import print_function
from controller import get_drone, set_gimbal, position, takeoff, land
import time
from olympe.messages.ardrone3.PilotingState import PositionChanged
from stream import Stream

if __name__ == '__main__':

    try:
        print('Creating drone')
        drone = get_drone('192.168.42.1')
        time.sleep(2)


        drone.connection()
        print('Established connection')
        time.sleep(2)


        print('Creating stream')
        stream = Stream(drone)
        time.sleep(10)

        print('Starting stream')
        stream.start()
        time.sleep(5)
        
        print('Stopping stream')
        stream.stop()



    finally:

        time.sleep(10)

        drone.disconnection()
    