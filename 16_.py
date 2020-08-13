import numpy as np
from PIL import Image


image = Image.open('mozart.gif')
shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
Image.frombytes(image.mode, image.size, b"".join(shifted)).show()
