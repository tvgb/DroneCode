# -*- coding: UTF-8 -*-

import olympe
import os, csv, time, tempfile
from olympe.messages import gimbal
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged, HomeChanged
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing, moveTo
from stream import Stream


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
    )).wait()


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


def start_stream(drone):
    stream = Stream(drone)

