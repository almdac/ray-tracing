import numpy as np

class Object:
    def __init__(self,
                 color: np.ndarray,
                 ka: int, 
                 kd: int,
                 ks: int,
                 eta: int) -> None:
        self.color = color
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.eta = eta
    
    def intersection(self, o: np.ndarray, d: np.ndarray) -> float:
        raise NotImplementedError

class Sphere(Object):
    def __init__(self,
                 color: np.ndarray,
                 ka: int, 
                 kd: int,
                 ks: int,
                 eta: int,
                 center: np.ndarray,
                 radius: float) -> None:
        super().__init__(color, ka, kd, ks, eta)

        self.c = center
        self.r = radius
    
    def intersection(self, o: np.ndarray, d: np.ndarray) -> float:
        # Forma-se um triângulo retângulo entre o vetor diretor d que sai da câmera, e o vetor l de deslocamento entre a câmera e o centro da esfera.
        l = self.c-o # Vetor de deslocamento entre a câmera e o centro da esfera forma a hipotenusa 
        ca = np.dot(l, d) # Projeção de l em d forma o cateto adjascente
        co = (np.dot(l, l)-(ca**2))**0.5 # O cateto oposto é obtido por pitágoras

        if co <= self.r: # Se o cateto oposto for maior que o raio, não há intersecção com a esfera
            t_ca = ((self.r**2)-(co**2))**0.5 # O cateto adjascente da intersecção é obtido através de pitágoras, onde o raio é a hipotenusa
            if ca - t_ca < 0: return None
            t = ca - t_ca
            n = o + t*d - self.c
            n /= np.linalg.norm(n)
            return t, n, o+t*d, -1*d, self.ka, self.kd, self.ks, self.eta

class Plane(Object):
    def __init__(self,
                 color: np.ndarray,
                 ka: int, 
                 kd: int,
                 ks: int,
                 eta: int,
                 point: np.ndarray,
                 normal: np.ndarray) -> None:
        super().__init__(color, ka, kd, ks, eta)

        self.p = point
        self.n = normal

    def intersection(self, o: np.ndarray, d: np.ndarray) -> float:
        den = np.dot(d, self.n)
        if np.linalg.norm(den) > 10e-6:
            t = np.dot((self.p-o), self.n)/den
            if t >= 0:
                return t, self.n, o+t*d, -1*d, self.ka, self.kd, self.ks, self.eta