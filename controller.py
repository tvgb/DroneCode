# -*- coding: UTF-8 -*-

import olympe
import os
from olympe.messages import gimbal
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged, HomeChanged
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing, moveTo


def get_drone(ip):
    drone = olympe.Drone(ip, loglevel=1) # loglevel 1 is only errors
    print('Created drone')
    return drone

def position(drone):
    drone(GPSFixStateChanged(_policy = 'wait'))
    print("GPS position before take-off :", drone.get_state(HomeChanged))

def takeoff(drone):
    try:
        drone(TakeOff()).wait()
        print('Drone has taken off')
    except:
        print('Code failed when trying to run funciton takeoff()')
        drone(Landing()).wait()


def moveby(drone,x,y,z,psi=0.0):
    try:
        drone(moveBy(x, y, z, psi)).wait()
        print('Drone moved by ', x, y, z, ' (x,y,z) in meters')
    except:
        print('Code failed when trying to run funciton move()')
        drone(Landing()).wait()
    

def land(drone):
    try:
        drone(Landing()).wait()
        print('Drone landed')
    except:
        print('Code failed when trying to run funciton land()')

def moveto(drone, latitude, longitude, altitude, orientation_mode, heading):
    try:
        drone(moveTo(
            latitude,
            longitude,
            altitude,
            orientation_mode,
            heading
        )).wait
        print('Moving to:', 'lat:', latitude, 'long:', longitude, 'alt:', altitude)
    except:
        print('Code failed when trying to run function moveto()')
        drone(Landing()).wait()


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


def stream(drone):
    drone.start_video_streaming()
    for i in range (10):
        drone.h264_frame_stats = []
        drone.h264_stats_file = open(
            os.path.join("", 'h264_stats.csv'), 'w+')
    drone.stop_video_streaming()


'''

print('Setting gimbal')
set_gimbal(drone, "position", 0.0, 0.0, 0.0)
print('Gimbal set')

time.sleep(10)

print('Setting gimbal')
set_gimbal(drone, "position", 1.0, 0.0, 0.0)
print('Gimbal set')

time.sleep(10)

print('Setting gimbal')
set_gimbal(drone, "position", 0.0, 0.0, 0.0)
print('Gimbal set')



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