import time
import numpy as np
from midi_connector import midi_connector

from pygame import mixer # Load the required library

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

# CHANNELS = 6

PATH_TO_MP3 = ''

INTERVAL = int(input('\n\nZeitintervall zwischen den Sounds, z.B. 30 heißt alle 30 min spielts (nur ganze Zahlen, kein Komma!)\n'))

PLAY_TIME = int(input('\n\nWie lange solls spielen (Minuten)?\n'))

MIN_SAMPLE_INTERVAL = float(input('\n\nWie lang soll der MINIMALE Zeitabstand der samples sein? zB 0.2 für 0.2 sek\n'))

MAX_SAMPLE_INTERVAL = float(input('\n\nWie lang soll der MAXIMALE Zeitabstand der samples sein? zB 1 für 1 sek\n'))

SAMPLE_INTERVAL_RATIO = int(MAX_SAMPLE_INTERVAL/MIN_SAMPLE_INTERVAL)

CHANNELS = int(input('\n\nWie viele Midi Kanäle gibts? (8 heißt 8 Kanäle!)\n'))

# BEATS_INTERVAL in sec
INTERVAL=INTERVAL*60

PLAY_TIME = PLAY_TIME*60/MIN_SAMPLE_INTERVAL

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

print('\nIt`s on!')
print('Press Ctrl+c to abort')



def play():

    counter = 0

    # StartZeit
    time_start = time.time()

    # initialize midi
    midi.init_midi()

    # load the mp3 sound file
    # initialze the mixer for mp3
    mixer.init()
    mixer.music.load(PATH_TO_MP3)
    # mixer.music.play()
    try:
        while counter<PLAY_TIME:

            # Das Signal soll random zwischen MIN und MAX gesendet werden
            my_rand_int = np.random.randint(SAMPLE_INTERVAL_RATIO)
            if my_rand_int == 0:
                midi.send_signal()

            time.sleep(MIN_SAMPLE_INTERVAL)
            counter +=1

            # aktuelle Zeit
            jetzt_zeit=time.time()
            diff_time = jetzt_zeit - time_start

        # close midi connection
        midi.quit_midi()

    except KeyboardInterrupt:
        midi.quit_midi()


#TODO
# hier brauchts noch ein scheduler der alle 30 min play macht

# if __name__=='__main__':
#     play()
#     midi.quit_midi()

