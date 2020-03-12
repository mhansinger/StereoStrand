# soll den Strom/Spannung was auch immer vom Rotor messen.
# am besten wäre Moving average mit verstellbarer Fensterweite

import numpy as np
from ina219 import INA219
from ina219 import DeviceRangeError
import time



class voltage(object):
    def __init__(self,WINDOW):
        '''

        :param SHUNT_OHMS: shunt OHM, für was auch immer ...
        :param SAMPLE_RATE: legt fest wie oft pro Sekunde ein Signal gemessen wird; wird evtl auch ned gebraucht
        :param WINDOW: Fenster für moving average
        '''

        self.SHUNT_OHMS = 0.1
        #self.SAMPLE_RATE = SAMPLE_RATE  # das wird vermutlich über die Aufrufe von 'update_shunt_voltage' implizit gesteuert??
        self.WINDOW = WINDOW

        self.counter = 0
        self.ina = INA219(self.SHUNT_OHMS)
        self.ina.configure()

        print('Setting up Voltage measurement ...')
        print("Bus Voltage: %.3f V" % self.ina.voltage())
        print("Shunt voltage: %.3f mV" % self.ina.shunt_voltage())

        # Dummy array wo die shunt voltage werte gespeichert werden und updates angehängt
        self._voltage_array = np.zeros(1)

    def get_shunt_voltage(self):
        return self.ina.shunt_voltage()

    def update_shunt_voltage(self):

        this_shunt_volage = self.get_shunt_voltage()

        # ensure all values are positive
        for i in range(len(self._voltage_array)):
            if self._voltage_array[i] < 0:
                self._voltage_array[i] = 0

        #update the array: neuer wert an erste Stelle
        self._voltage_array = np.append(this_shunt_volage,self._voltage_array)

        # maximale array size: zB 20 Mal die Window size, schneide es ab:
        # Grund: Speicher??
        if len(self._voltage_array) > self.WINDOW:
            self._voltage_array = self._voltage_array[0:self.WINDOW]

        # update counter
        self.counter += 1

    def get_voltage_array(self):
        # returns the self._voltage_array
        return self._voltage_array



