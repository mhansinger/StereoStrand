import time
import numpy as np
from midi_connector import midi_connector
from myASCII import ascii_greeter
from asciimatics.screen import Screen


WINDOW = 100

CHANNELS = 9

INTERVAL = input('\n\nZeitintervall zwischen den Sounds, z.B. 2 heißt alle 2 sek. einen Ton\n')

BEATS_INTERVAL = input('\n\nWieviele Minuten zwischen den Beats?\n')

# BEATS_INTERVAL in sec
BEATS_INTERVAL=BEATS_INTERVAL*60

LIEBLINGS_ZAHL = input('\n\nWas ist deine Lieblingszahl (1-1000)?\n')

COUNTER = 0


try:
    INTERVAL = float(INTERVAL)
except ValueError:
    print('Muss eine Zahl sein!')

midi = midi_connector(WINDOW=WINDOW,CHANNELS=CHANNELS)

def play():

    # ASCII bild
    Screen.wrapper(ascii_greeter)

    print('\nIt`s on!')
    print('Press Ctrl+c to abort')

    # StartZeit
    time_start = time.time()
    try:
        while True:
            midi.send_signal()

            time.sleep(INTERVAL * np.random.rand() + INTERVAL)

            RANDINT = np.random.randint(1000)

            #
            if RANDINT == LIEBLINGS_ZAHL:
                print('Checkpot!')
                for i in range(9):
                    midi.test_send(i)
                    time.sleep(0.1)

            # aktuelle Zeit
            jetzt_zeit=time.time()
            diff_time = jetzt_zeit - time_start

            if diff_time > BEATS_INTERVAL:
                midi.test_send(9)       # schick signal an Kanal 10 (ist in python die nr 9)

    except KeyboardInterrupt:
        midi.quit_midi()

if __name__=='__main__':
    play()

