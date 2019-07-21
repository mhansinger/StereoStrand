# zum Ausprobieren

import time
import numpy as np

from midi_connector import midi_connector_test

test_midi = midi_connector_test(WINDOW=100,CHANNELS=9)

while True:
    sleep = np.random.rand()
    test_midi.send_signal()
    time.sleep(1+sleep)
