#!/usr/bin/env python
'''Moves switcher 1 to dump position'''
import sys, time
sys.path.append('../')
from switcher import dxlS500R
from globals import *

switcher1 = dxlS500R(PORT=SWITCHER1_COMM_PORT)
switcher1.set_velocity(MOTOR_VELOCITY)
switcher1.enable_torque()
switcher1.set_position(170000, IN_TICS=True)
# switcher1.set_position(421500, IN_TICS=True)
print('moving switcher')
time.sleep(2)
while switcher1.is_moving():
    time.sleep(0.1)
print(switcher1.get_current_position(IN_TICS=True))
