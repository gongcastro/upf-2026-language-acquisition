from matplotlib.pylab import tight_layout, plot
from pathlib import Path

import soundfile as sf
import numpy as np
from matplotlib import pyplot as plt

IMG_PATH: Path = Path("img")


def plot_oscillogram(file: Path | str):
    file = Path(file)
    y, sr = sf.read(file)
    n = len(y)
    time = np.arange(n) / sr

    fig, ax = plt.subplots(1, 1, figsize=(6, 2), tight_layout=True)
    ax.plot(time, y, color="k")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[["left", "right", "top", "bottom"]].set_visible(False)

    fig.savefig(IMG_PATH / file.with_suffix(".png").name, dpi=1_200)


if __name__ == "__main__":
    plot_oscillogram(Path("sounds/pretty-baby.wav"))
