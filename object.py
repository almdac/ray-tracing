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
    
    def intersection(self, o: np.ndarray, d: np.ndarray) -> float:
        # Forma-se um triângulo retângulo entre o vetor diretor d que sai da câmera, e o vetor l de deslocamento entre a câmera e o centro da esfera.
        l = self.c-o # Vetor de deslocamento entre a câmera e o centro da esfera forma a hipotenusa 
        ca = np.dot(l, d) # Projeção de l em d forma o cateto adjascente
        co = (np.dot(l, l)-(ca**2))**0.5 # O cateto oposto é obtido por pitágoras

        if co <= self.r: # Se o cateto oposto for maior que o raio, não há intersecção com a esfera
            t_ca = ((self.r**2)-(co**2))**0.5 # O cateto adjascente da intersecção é obtido através de pitágoras, onde o raio é a hipotenusa
            intersections = sorted([ca-t_ca, ca+t_ca]) # Haverão dois pontos de intersecção (entrada e saída da esfera)
            t = next(iter([i for i in intersections if i > 0])) # A intersecção acontece somente na frente da câmera, logo um escalar negativo muda a direção de captura e não é válido
            return t

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