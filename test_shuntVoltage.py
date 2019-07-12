# nur zum testen ob shunt voltage gemessen wird

import numpy as np
from ina219 import INA219
from ina219 import DeviceRangeError
import time

#TEST

SHUNT_OHMS = 1

def read():
    ina = INA219(SHUNT_OHMS)
    ina.configure()

    print("Bus Voltage: %.3f V" % ina.voltage())
    try:

        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resister
        print(e)


for i in range(1000):
    read()
    time.sleep(1) #pause 1 sec