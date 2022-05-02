import array

import numpy as np

from cam import Cam
from object import Sphere, Plane

def main():
    with open('input.txt', 'r') as f:
        v_res, h_res = [int(n) for n in f.readline().split(' ')]
        s, d = [float(n) for n in f.readline().split(' ')]
        e = np.array([float(n) for n in f.readline().split(' ')])
        l = np.array([float(n) for n in f.readline().split(' ')])
        up = np.array([float(n) for n in f.readline().split(' ')])
        background_color = np.array([float(n) for n in f.readline().split(' ')])

        k_objs = int(f.readline())

        objects = []
        for k in range(k_objs):
            line = f.readline()
            split = line.split(' ')
            element = split[7]

            color = np.array([float(n) for n in split[:3]])
            ka = float(split[3])
            kd = float(split[4])
            ks = float(split[5])
            eta = float(split[6])
            if element == '*':
                center = np.array([float(n) for n in split[8:11]])
                radius = float(split[11])

                sphere = Sphere(color, ka, kd, ks, eta, center, radius)
                objects.append(sphere)
            
            if element == '/':
                point = np.array([float(n) for n in split[8:11]])
                normal = np.array([float(n) for n in split[11:]])

                plane = Plane(color, ka, kd, ks, eta, point, normal)
                objects.append(plane)
        
        ca = np.array([float(n) for n in f.readline().split(' ')])
        k_lights = int(f.readline())

        lights = []
        for k in range(k_lights):
            line = f.readline()
            split = line.split(' ')
            i = np.array([float(n) for n in split[:3]])
            p = np.array([float(n) for n in split[3:]])
            _t = (i, p)
            lights.append(_t)

    cam = Cam(v_res, h_res, s, d, e, l, up, background_color, objects, lights, ca)
    
    img = cam.render()
    with open('output.ppm', 'wb') as f:
        f.write(bytearray(f'P6 {h_res} {v_res} 255\n', 'ascii'))
        byteimg = array.array('B', list(img.flatten()))
        byteimg.tofile(f)

if __name__ == '__main__':
    main()