import numpy as np
from db.stars import Star


class Point:
    def __init__(self, star: Star, time: float, phi: float):
        self._star = star
        self.time = time
        self.t = time - self._star.ra
        self.phi = phi * np.pi / 180
        self.dec = self._star.dec

    def cords_eq(self):
        "second equatorial system's coordinates"
        self.__x = np.cos(self.dec) * np.cos(self.t)
        self.__y = np.cos(self.dec) * np.sin(self.t)
        self.__z = np.sin(self.dec)
        return self.__x, self.__y, self.__z

    def vector_in_horizontal(self):
        "Coordinates in Horizontal System"
        xyz = self.cords_eq()
        vect = np.array(xyz)
        rotation_matrix = np.array([
            [np.sin(self.phi), 0, -np.cos(self.phi)],
            [0, 1, 0],
            [np.cos(self.phi), 0, np.sin(self.phi)]
        ])
        self.__vect = rotation_matrix @ vect

    def stereographic_projection(self):
        "changes coordinates to stereographic projection"
        self.vector_in_horizontal()
        x, y, z = self.__vect
        if z <= 0:
            return np.inf, np.inf

        r = 2 * np.pi * np.sqrt(1 - z**2) / (z + np.pi)
        psi = np.arctan(y/ x)
        self._x_st = r * np.cos(psi)
        self._y_st = r * np.sin(psi)




