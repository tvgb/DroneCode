# -*- coding: UTF-8 -*-

import olympe
import os
import csv
import time
import tempfile
from olympe.messages import gimbal
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged, HomeChanged
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing, moveTo


def get_drone(ip):
    drone = olympe.Drone(ip, loglevel=1) # loglevel 1 is only errors
    return drone

def position(drone):
    drone(GPSFixStateChanged(_policy = 'wait'))
    return drone.get_state(HomeChanged)

def takeoff(drone):
    drone(TakeOff()).wait()


def moveby(drone,x,y,z,psi=0.0):
    drone(moveBy(x, y, z, psi)).wait()
    

def land(drone):
    drone(Landing()).wait()

def moveto(drone, latitude, longitude, altitude, orientation_mode, heading):
    drone(moveTo(
        latitude,
        longitude,
        altitude,
        orientation_mode,
        heading
    )).wait

def disconnect(drone):
    drone.disconnection()

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
    drone.tempd = tempfile.mkdtemp(prefix="olympe_streaming_test_")
    print("Olympe streaming example output dir: {}".format(drone.tempd))
    drone.h264_frame_stats = []
    drone.h264_stats_file = open(
        os.path.join(drone.tempd, 'h264_stats.csv'), 'w+')
    drone.h264_stats_writer = csv.DictWriter(
        drone.h264_stats_file, ['fps', 'bitrate'])
    drone.h264_stats_writer.writeheader()


'''
def stream(drone):
    drone.start_video_streaming()
    time.sleep(10)
    drone.h264_frame_stats = []
    drone.h264_stats_file = open('h264_stats.csv', 'w+')
    drone.h264_stats_writer = csv.DictWriter(drone.h264_stats_file, ['fps', 'bitrate'])
    drone.h264_stats_writer.writeheader()
    drone.stop_video_streaming()




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