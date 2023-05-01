# H54-200-S500-R Interface

Please note that the H54-200-S500-R is no longer sold. For interface with the next closest motor, 
the [ph54-200-s500-r](https://emanual.robotis.com/docs/en/dxl/p/ph54-200-s500-r/), that the registers located in 
`switchers/globals.py` must be updated accordingly

```
Help on package switcher:

NAME
    switcher

PACKAGE CONTENTS
    device
    dynamixel_sdk (package)
    globals

CLASSES
    builtins.object
        switcher.device.dxlS500R
    
    class dxlS500R(builtins.object)
     |  dxlS500R(PORT='/dev/ttyUSB0', DXL_ID=1, BAUDRATE=57600, VERBOSE=False)
     |  
     |  Device interface with the Dynamixel Pro h54-200-s500-r
     |  
     |  Methods defined here:
     |  
     |  __init__(self, PORT='/dev/ttyUSB0', DXL_ID=1, BAUDRATE=57600, VERBOSE=False)
     |      PORT expects some /dev/ttyUSB*
     |      DXL_ID can be determined with /tests/ping.py. Factory default is 1
     |      BAUDRATE is set to factory default
     |      If VERBOSE is True, prints out status updates
     |  
     |  checkCommStatus(self, dxl_comm_result, dxl_error)
     |      Takes output status from packet handler and interprets it.
     |      Raises error if unsuccessful
     |  
     |  close(self, disengage_motor=False)
     |      Disengages motor and closes communication port
     |  
     |  disable_torque(self)
     |      Disengages the motor
     |  
     |  enable_torque(self)
     |      Enables torque on motor
     |  
     |  get_control_mode(self)
     |      Returns the control mode that the motor is operating in
     |  
     |  get_current_position(self, IN_TICS=False)
     |      Returns current position [degrees] (default) or in [tics]. Note: Never returns a negative value
     |  
     |  get_current_velocity(self)
     |      Returns current velocity [deg/sec] (This is "Before reduction gears" whatever that means)
     |  
     |  get_goal_torque(self)
     |      set goal torque on motor
     |  
     |  get_goal_velocity(self)
     |      Returns goal velocity [deg/sec] (This is "Before reduction gears" whatever that means)
     |  
     |  get_id(self)
     |      Returns ID of connected motor
     |  
     |  is_moving(self)
     |      Returns 1 if motor is in motion
     |  
     |  one_way_turn_to(self, pos, IN_TICS=False)
     |      Forces the switcher to turn in the positive direction only to reach a new position
     |  
     |  ping(self)
     |      Pings communication port and retrieves model number
     |  
     |  pprint(self, msg)
     |      Prints motor status updates if VERBOSE = True
     |  
     |  reboot(self)
     |      Reboots motor. Dynamixel LED will flicker
     |  
     |  set_control_mode(self, mode)
     |      Set to "TorqueControl", "VelocityControl", "PositionControl" (default), or "ExtendedPositionControl" (multi-turn enabled) mode
     |  
     |  set_goal_torque(self, goal_torque)
     |      set goal torque on motor
     |  
     |  set_id(self, newID)
     |      Sets ID of connected motor to a value
     |  
     |  set_position(self, pos, IN_TICS=False)
     |      Sets current position in [degrees] (default) or in [tics]
     |  
     |  set_velocity(self, deg_per_sec)
     |      Sets goal velocity [deg/sec] (This is "Before reduction gears" whatever that means)
     |      Note that a value of 0 [default] sets velocity to the max
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  PROTOCOL_VERSION = 2.0

DATA
    __all__ = ['dxlS500R']

FILE
    /home/daq/switcherControl/switcher/__init__.py
```


