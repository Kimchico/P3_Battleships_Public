import enum
import numpy as np

class Color(enum.Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"

    """
    LOW_THRESHOLD = {}
    HIGH_THRESHOLD = {}

    LOW_THRESHOLD["RED"] = np.array([150 - 30, 100, 100])
    LOW_THRESHOLD["GREEN"] = np.array([60 - 30, 100, 100])
    LOW_THRESHOLD["BLUE"] = np.array([80, 70, 70])

    HIGH_THRESHOLD["RED"] = np.array([150 + 30, 255, 255])
    HIGH_THRESHOLD["GREEN"] = np.array([60 + 30, 255, 255])
    HIGH_THRESHOLD["BLUE"] = np.array([140, 255, 255])
    """