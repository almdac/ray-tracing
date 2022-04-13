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

        f.readline()

        objects = []
        for line in f:
            split = line.split(' ')
            element = split[3]

            color = np.array([float(n) for n in split[:3]])
            if element == '*':
                center = np.array([float(n) for n in split[4:7]])
                radius = split[7]

                sphere = Sphere(color, center, radius)
                objects.append(sphere)
            
            if element == '/':
                point = np.array([float(n) for n in split[4:7]])
                normal = np.array([float(n) for n in split[7:]])

                plane = Plane(color, point, normal)
                objects.append(plane)

    cam = Cam(v_res, h_res, s, d, e, l, up, background_color, objects)
    
    img = cam.render()
    with open('output.ppm', 'wb') as f:
        f.write(bytearray(f'P6 {h_res} {v_res} 255\n', 'ascii'))
        byteimg = array.array('B', list(img.flatten()))
        byteimg.tofile(f)

if __name__ == '__main__':
    main()