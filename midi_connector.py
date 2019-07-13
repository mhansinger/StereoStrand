# this is to connect with the MIDI intervace

import numpy as np
from voltage import voltage
import time
import sys
import os

import pygame
import pygame.midi
from pygame.locals import *
import progressbar

class midi_connector(object):
    def __init__(self,WINDOW,CHANNELS,OUTPUT_FREQ):
        '''

        :param WINDOW: Fenster des Sliding mean
        :param SAMPLE_RATE: FREQUENZ mit der das Fluss Signal gesampelt wird
        :param CHANNELS: Anzahl der Midi Kanäle die Basti hat
        :param OUTPUT_FREQ: Frequenz mit der das Sound-Signal upgedated wird
        '''
        self.WINDOW = WINDOW
        #self.SAMPLE_RATE = SAMPLE_RATE
        self.CHANNELS = CHANNELS
        self.OUTPUT_FREQ =OUTPUT_FREQ

        # setup the volotmeter
        self.voltometer = voltage(WINDOW = self.WINDOW)

        # set up midi interface
        self.mymidi = pygame.midi
        self.init_midi()

        self.port = 2  # war beim letzten mal richtig...

        self.midi_out = self.mymidi.Output(self.port, 0)

        #TODO
        # Das Array zuerst mit Daten füllen?
        bar = progressbar.ProgressBar(maxval=20,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        print('Initial Data collection ...')
        for i in range(100):
            self.voltometer.update_shunt_voltage()
            time.sleep()
            bar.update(i + 1)
            time.sleep(0.1)
        bar.finish()

    def init_midi(self):
        self.mymidi.init()

    def quit_midi(self):
        self.mymidi.quit()

    def send_signal(self):

        # update the voltage array
        self.voltometer.update_shunt_voltage()

        # get the current shunt voltage
        this_shunt_voltage = self.voltometer.get_shunt_voltage()

        this_voltage_array = self.voltometer.get_voltage_array()

        # get MAX and MIN values of the voltage array for normalization
        this_max_volt = max(this_voltage_array)
        this_min_volt = min(this_voltage_array)

        #TODO
        # hier muss soetwas wie Binning gemacht werden um den richtig Kanal zu finden...







