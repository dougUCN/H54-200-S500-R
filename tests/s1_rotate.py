#!/usr/bin/env python
'''Rotates Switcher 1 +360 from current direction'''
import sys, time
import numpy as np
sys.path.append('../')
from switcher import dxlS500R
from globals import *

switcher1 = dxlS500R(PORT=SWITCHER1_COMM_PORT) 
switcher1.set_velocity(10)
switcher1.enable_torque()
print(switcher1.get_current_position(), switcher1.get_current_position(IN_TICS=True))
print('moving switcher')
switcher1.set_position(switcher1.get_current_position() + 400)
time.sleep(2)
while switcher1.is_moving():
    time.sleep(0.1)
    print(switcher1.get_current_position(), switcher1.get_current_position(IN_TICS=True))
