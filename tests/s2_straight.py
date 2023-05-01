#!/usr/bin/env python
'''Moves switcher 2 to straight through position'''
import sys
sys.path.append('../')
from switcher import dxlS500R
from globals import *
import time

switcher2 = dxlS500R(PORT=SWITCHER2_COMM_PORT) # switcher 2 is lower on the stand
switcher2.set_velocity(MOTOR_VELOCITY)
switcher2.enable_torque()
switcher2.set_position(342000, IN_TICS=True)
print('moving switcher')
time.sleep(2)
while switcher2.is_moving():
    time.sleep(0.1)
print(switcher2.get_current_position(IN_TICS=True))
