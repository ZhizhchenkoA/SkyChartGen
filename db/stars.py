import numpy as np


class Star:
    "star in equatorial coordinates system"

    def __init__(self, ra: float, dec: float, magnitude: float):
        self.ra = ra
        self.dec = dec
        self.magnitude = magnitude

    def get_cords(self):
        return self.ra, self.dec


