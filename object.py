import numpy as np

class Object:
    def __init__(self, color: np.ndarray) -> None:
        self.color = color
    
    def intersection(self, o: np.ndarray, d: np.ndarray) -> float:
        raise NotImplementedError

class Sphere(Object):
    def __init__(self, color: np.ndarray, center: np.ndarray, radius: float) -> None:
        super().__init__(color)

        self.c = center
        self.r = radius

class Plane(Object):
    def __init__(self, color: np.ndarray, point: np.ndarray, normal: np.ndarray) -> None:
        super().__init__(color)

        self.p = point
        self.n = normal

    def intersection(self, o: np.ndarray, d: np.ndarray) -> float:
        den = np.dot(d, self.n)
        if np.linalg.norm(den) > 10e-6:
            t = np.dot((self.p-o), self.n)/den
            if t >= 0:
                return t