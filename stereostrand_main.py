import time
import numpy as np
from midi_connector import midi_connector

WINDOW = 100

CHANNELS = 9

INTERVAL = input('\n\nZeitintervall zwischen den Sounds, z.B. 2 heißt alle 2 sek. einen Ton\n')

try:
    INTERVAL = float(INTERVAL)
except ValueError:
    print('Muss eine Zahl sein!')

midi = midi_connector(WINDOW=WINDOW,CHANNELS=CHANNELS)

def play():
    print('\nIt`s on!')
    print('Press Ctrl+c to abort')
    while True:
        midi.send_signal()

        time.sleep(INTERVAL*np.random.rand()+INTERVAL)

if __name__=='__main__':
    play()

