import numpy as np
from configparser import ConfigParser

def load_element_file(filename):
    config = ConfigParser()
    with open(filename) as inF:
        config.read_string("[top]\n" + inF.read())
    data = config.items('elements')[2:]
    data = [line[1] for line in data]
    coords = []
    angles = []
    focalpoint = np.array([0,0,0])

    for line in data:
        numbers = line.split('|')
        x = [float(num) for num in numbers]
        coords.append(x)
        angles.append(calc_angle(focalpoint, x))
    coords = np.array(coords)
    #       the angle       the length correction factor
    return np.mean(angles), 1/np.cos(np.mean(angles))


def calc_angle(focalpoint, x):
    return np.arcsin(np.sqrt(x[0]**2+x[1]**2)/np.linalg.norm(focalpoint - x, ord=2))