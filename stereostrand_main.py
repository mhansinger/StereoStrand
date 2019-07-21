import time
import numpy as np
from midi_connector import midi_connector

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

# Startbildschirm
def ascii_greeter(screen):
    effects = [
        Cycle(
            screen,
            FigletText("StereoStrand", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("ROCKS!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 100)],repeat=False)


WINDOW = 100

CHANNELS = 9

INTERVAL = int(input('\n\nZeitintervall zwischen den Sounds, z.B. 2 heißt alle 2 sek. einen Ton\n'))

BEATS_INTERVAL = int(input('\n\nWieviele Minuten zwischen den Beats?\n'))

# BEATS_INTERVAL in sec
BEATS_INTERVAL=BEATS_INTERVAL*60

LIEBLINGS_ZAHL = int(input('\n\nWas ist deine Lieblingszahl (1-1000)?\n'))

COUNTER = 0
#
#
# try:
#     INTERVAL = float(INTERVAL)
# except ValueError:
#     print('Muss eine Zahl sein!')

# ASCII bild
try:
    Screen.wrapper(ascii_greeter)
    # klappt nie beim ersten mal???
except:
    pass

try:
    Screen.wrapper(ascii_greeter)
except:
    pass

midi = midi_connector(WINDOW=WINDOW,CHANNELS=CHANNELS)

def play():

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
                print('\nTHE BEAT IS ON!\n')
                midi.test_send(9)       # schick signal an Kanal 10 (ist in python die nr 9)
                time_start = jetzt_zeit

    except KeyboardInterrupt:
        midi.quit_midi()

if __name__=='__main__':
    play()
    midi.quit_midi()

