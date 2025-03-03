import scipy.integrate as integrate
import numpy as np
from src.utils.config import config
from src.utils.constants import constants

def PLANCK_FUNCTION(f, T):
    return 2 * constants.h * f**3 * constants.c**-2 / (np.exp(constants.h * f / (constants.k * T)) - 1)

def BOUND_FREE_ABSORPTION_COEFFICIENT(f, N0):
    return 2.81e29 * N0 * constants.GAUNT_FACTOR * f**-3

def OPTICAL_DEPTH(f, N0, paths):
    bf = BOUND_FREE_ABSORPTION_COEFFICIENT(f, N0)
    od = np.zeros_like(bf)

    for i in range(config.GRID_EDGE_LENGTH):
        for j in range(config.GRID_EDGE_LENGTH):
            cumulative_abs = 0
            for coordinates in paths[(i, j)][0]:
                coord_y = coordinates[0]
                coord_x = coordinates[1]
                cumulative_abs += bf[coord_y][coord_x]
            if paths[(i, j)][0]:
                od[i][j] = cumulative_abs / len(paths[(i, j)][0])
            else:
                od[i][j] = 0
    return od * constants.DISTANCE_KERNEL


def INTENSITY(f, T, N0, paths):
    base_intensity = PLANCK_FUNCTION(f, T) * np.pi
    distance_decay = np.where(constants.DISTANCE_KERNEL != 0, constants.DILUTION_FACTOR, 0)
    extinction_decay = np.exp(-OPTICAL_DEPTH(f, N0, paths))

    return base_intensity * distance_decay * extinction_decay

def PHOTOIONIZATION_PER_FREQUENCY(f, T, N0, paths):
    bound_free_coefficient = BOUND_FREE_ABSORPTION_COEFFICIENT(f, N0) 

    ionization_rate =  bound_free_coefficient * INTENSITY(f, T, N0, paths) / (constants.h * f) * 4 * np.pi
    return ionization_rate

def PHOTOIONIZATION(T, N0, paths):
    upper_bound = constants.LYMAN_LIMIT * 10

    total = integrate.quad_vec(PHOTOIONIZATION_PER_FREQUENCY, constants.LYMAN_LIMIT, upper_bound, args = (T, N0, paths))[0]
    return total

def HYDROGEN_RECOMBINATION():
    return config.RECOMB_COEFFICIENT