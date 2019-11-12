import enum
import numpy as np

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

LOW_THRESHOLD = {}
HIGH_THRESHOLD = {}

# Adjust these
LOW_THRESHOLD[Color.RED] = np.array([150 - 30, 100, 100])
LOW_THRESHOLD[Color.GREEN] = np.array([60 - 30, 100, 100])
LOW_THRESHOLD[Color.BLUE] = np.array([80, 70, 70])

HIGH_THRESHOLD[Color.RED] = np.array([150 + 30, 255, 255])
HIGH_THRESHOLD[Color.GREEN] = np.array([60 + 30, 255, 255])
HIGH_THRESHOLD[Color.BLUE] = np.array([140, 255, 255])

