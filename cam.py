import itertools
import numpy as np

class Cam:
    def __init__(
        self,
        v_res: int,
        h_res: int,
        s: int,
        d: int,
        e: np.ndarray,
        l: np.ndarray,
        up: np.ndarray
    ) -> None:
        self.v_res = v_res
        self.h_res = h_res
        self.s = s
        self.d = d
        self.e = e
        self.l = l
        self.up = up
    
    def render(self) -> np.ndarray:
        w = (self.e-self.l) / np.linalg.norm(self.e-self.l)
        u = np.cross(self.up, w) / np.linalg.norm(np.cross(self.up, w))
        v = np.cross(w, u)
        
        for (i, j) in itertools.product(range(self.v_res), range(self.h_res)):
            pass
