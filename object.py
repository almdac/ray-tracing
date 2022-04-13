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