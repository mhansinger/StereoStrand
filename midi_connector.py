# this is to connect with the MIDI intervace

import numpy as np
from voltage import voltage
import time
import sys
import os

import pygame
import pygame.midi
from pygame.locals import *

class midi_connector(object):
    def __init__(self,WINDOW,SAMPLE_RATE,CHANNELS,OUTPUT_FREQ):
        '''

        :param WINDOW: Fenster des Sliding mean
        :param SAMPLE_RATE: FREQUENZ mit der das Fluss Signal gesampelt wird
        :param CHANNELS: Anzahl der Midi Kanäle die Basti hat
        :param OUTPUT_FREQ: Frequenz mit der das Sound-Signal upgedated wird
        '''
        self.WINDOW = WINDOW
        self.SAMPLE_RATE = SAMPLE_RATE
        self.CHANNELS = CHANNELS
        self.OUTPUT_FREQ =OUTPUT_FREQ

        # setup the volotmeter
        self.voltometer = voltage(WINDOW = self.WINDOW)

        # set up midi interface
        self.mymidi = pygame.midi
        self.init_midi()

        self.port = 2  # war beim letzten mal richtig...

        self.midi_out = self.mymidi.Output(self.port, 0)

    def init_midi(self):
        self.mymidi.init()

    def quit_midi(self):
        self.mymidi.quit()






