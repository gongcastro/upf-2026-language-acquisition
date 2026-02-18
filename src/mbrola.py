from pathlib import Path

import mbrola

# Create an MBROLA object
house = mbrola.MBROLA(
    word="house",
    phon=["h", "a", "U", "s"],
    durations=100,  # or [100, 120, 100, 110]
    pitch=[200, [200, 50, 200], 200, 100],
)
