import time
import numpy as np
from midi_connector import midi_connector

WINDOW = 1000

CHANNELS = 9

INTERVAL = input('Zeitintervall zwischen den Sounds, z.B. 2 heißt alle 2 sek. einen Ton\n')

try:
    INTERVAL = float(INTERVAL)
except ValueError:
    print('Muss eine Zahl sein!')

midi = midi_connector(WINDOW=WINDOW,CHANNELS=CHANNELS)

def play():
    while True:
        midi.send_signal()
        time.sleep(INTERVAL)

if __name__=='__main__':
    play()

