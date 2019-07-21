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
        :param CHANNELS: Anzahl der Midi Kanäle die Basti hat
        :param OUTPUT_FREQ: Frequenz mit der das Sound-Signal upgedated wird
        '''
        self.WINDOW = WINDOW
        #self.SAMPLE_RATE = SAMPLE_RATE
        self.CHANNELS = CHANNELS
        self.OUTPUT_FREQ =OUTPUT_FREQ

        # list of channels: obacht! startet mit 1!
        self.channel_list = [int(c + 1) for c in range(self.CHANNELS)]

        # setup the volotmeter
        self.voltometer = voltage(WINDOW = self.WINDOW)

        # set up midi interface
        self.mymidi = pygame.midi
        self.init_midi()

        self.port = 2  # war beim letzten mal richtig...

        self.midi_out = self.mymidi.Output(self.port, 0)

        bar = progressbar.ProgressBar(maxval=100,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        print('Initial Data collection ...')
        for i in range(100):
            self.voltometer.update_shunt_voltage()
            bar.update(i + 1)
            time.sleep(0.1)
        bar.finish()

    def init_midi(self):
        self.mymidi.init()

    def quit_midi(self):
        self.mymidi.quit()

    def get_normed_signal(self):
        # update the voltage array
        self.voltometer.update_shunt_voltage()

        # get the current shunt voltage
        this_shunt_voltage = self.voltometer.get_shunt_voltage()

        this_voltage_array = self.voltometer.get_voltage_array()

        # get MAX and MIN values of the voltage array for normalization
        this_max_volt = np.max(this_voltage_array)
        this_min_volt = np.min(this_voltage_array)

        normed_voltage_array = (this_voltage_array - this_min_volt) / (this_max_volt - this_min_volt)

        return normed_voltage_array


    def get_channel_number(self):
        # get the normalized signal
        normed_voltage_array = self.get_normed_signal()

        # latest shunt voltage
        this_normed_voltage = normed_voltage_array[0]

        this_channel_number = np.digitize(this_normed_voltage, np.linspace(0,1,self.CHANNELS))

        return int(this_channel_number)

    def send_signal(self):

        this_channel_number  = self.get_channel_number()

        self.midi_out.note_on(this_channel_number,127,1)

    def test_send(self,channel):
        self.midi_out.note_on(channel, 127, 1)









