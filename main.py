# -*- coding: UTF-8 -*-

import olympe
from olympe.messages import gimbal

with olympe.Drone("192.168.42.1", loglevel=1) as drone:
    drone.connection()

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
        raise RuntimeError("Cannot set gimbal position target")
    else:
        print('ROTATED GIMBAL!')
