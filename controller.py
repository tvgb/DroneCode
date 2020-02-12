# -*- coding: UTF-8 -*-

import olympe
from olympe.messages import gimbal
from olympe.messages.ardrone3.Piloting import TakeOff, Landing

def get_drone(ip):
    drone = olympe.Drone(ip, loglevel=1) # loglevel 1 is only errors
    print('Created drone')
    return drone

def set_gimbal(drone,set_mode,set_yaw,set_pitch,set_roll):
    drone(gimbal.set_target(
        gimbal_id=0,
        control_mode=set_mode,
        yaw_frame_of_reference="absolute",
        yaw=set_yaw,
        pitch_frame_of_reference="absolute",
        pitch=set_pitch,
        roll_frame_of_reference="absolute",
        roll=set_roll,  
    )).wait()





'''

drone.connection()
drone(TakeOff()).wait()
drone(Landing()).wait()
drone.disconnection()



def camera_straight(drone):
    drone(gimbal.set_target(
        gimbal_id=0,
        control_mode="position",
        yaw_frame_of_reference="none",
        yaw=0.0,
        pitch_frame_of_reference="absolute",
        pitch=0.0,
        roll_frame_of_reference="none",
        roll=0.0,
    )).wait() 

'''