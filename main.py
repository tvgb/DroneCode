# -*- coding: UTF-8 -*-

import olympe
from olympe.messages.camera import start_recording, stop_recording
from olympe.messages import gimbal

with olympe.Drone("192.168.42.1") as drone:
    drone.connection()

    # Start video recording while the drone is flying
    if not drone(start_recording(cam_id=0)).wait().success():
        raise RuntimeError("Cannot start video recording")
    else:
        print('STARTED RECORDING!')

    # Send a gimbal pitch velocity target while the drone is flying
    cameraAction = drone(gimbal.set_target(
        gimbal_id=0,
        control_mode="position",
        yaw_frame_of_reference="none",
        yaw=0.0,
        pitch_frame_of_reference="none",
        pitch=-90,
        roll_frame_of_reference="none",
        roll=0.0,
    )).wait()

    if not cameraAction.success():
        raise RuntimeError("Cannot set gimbal velocity target")
    else:
        print('ROTATED GIMBAL!')

    # Stop video recording while the drone is flying
    if not drone(stop_recording(cam_id=0)).wait().success():
        raise RuntimeError("Cannot stop video recording")
    else:
        print('STOPPED RECORDING')

    # Leaving the with statement scope: implicit drone.disconnection()
