# example from pygame

import sys
import os

import pygame
import pygame.midi
from pygame.locals import *

def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()

def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
               (i, interf, name, opened, in_out))
        

# MIDI OUTPUT
CHURCH_ORGAN = 19

instrument = CHURCH_ORGAN
#instrument = GRAND_PIANO
start_note = 53  # F3 (white key note), start_note != 0
n_notes = 24  # Two octaves (14 white keys)
    
def make_key_mapping(key_list, start_note):
    """Return a dictionary of (note, velocity) by computer keyboard key code"""
    
    mapping = {}
    for i in range(len(key_list)):
        mapping[key_list[i]] = (start_note + i, 127)
    return mapping


pygame.init()
pygame.midi.init()

_print_device_info()

#TODO
# unclear if device_id (=port) 0 or 2!
port = 2
midi_out = pygame.midi.Output(port, 0)

midi_out.set_instrument(instrument)

midi_out.note_on(1,120)



