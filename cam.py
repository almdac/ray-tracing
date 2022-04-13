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
        img = np.array([[np.array([0, 0, 0])]*self.h_res]*self.v_res)

        w = self.e-self.l
        w = w/np.linalg.norm(w)

        u = np.cross(self.up, w)
        u = u/np.linalg.norm(u)

        v = np.cross(w, u)

        for (i, j) in itertools.product(range(self.v_res), range(self.h_res)):
            x = self.s*(j-(self.h_res/2)+0.5)
            y = self.s*(i-(self.v_res/2)+0.5)

            q = self.e+(x*u)+(y*v)-(self.d*self.w)
            q = q/np.linalg.norm(q)
            