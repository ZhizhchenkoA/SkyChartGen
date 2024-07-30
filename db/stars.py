import numpy as np


class Star:
    "star in equatorial coordinates system"

    def __init__(self, ra: float, dec: float, magnitude: float):
        self.ra = ra
        self.dec = dec
        self.magnitude = magnitude

        self.x = np.cos(dec) * np.cos(ra)
        self.y = np.cos(dec) * np.sin(ra)
        self.z = np.sin(dec)

    def vector(self):
        return self.x, self.y, self.z


