import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from src.solvers.radiationsolvers import PLANCK_FUNCTION
from src.models.automaton import automaton
from src.utils.config import config
from src.utils.constants import constants
from matplotlib.ticker import FuncFormatter

def ionizing_photons(f, T):
    return np.pi * PLANCK_FUNCTION(f, T) / (f * constants.h)

def stromgren():
    ll = constants.LYMAN_LIMIT
    int = quad(ionizing_photons, ll, ll * 10, args = (config.STAR_SURFACE_TEMP))[0]
    luminosity = config.STELLAR_RADIUS**2 * np.pi * 4 * int
    return np.cbrt(3 * luminosity / (4 * np.pi * config.HYDROGEN_DENSITY ** 2 * config.RECOMB_COEFFICIENT)) * 3.24076e-19

def cells_to_pc(c, pos):
    return f"{c * config.CELL_EDGE_PC:.2f}"

def plot_ion_fraction(a: automaton):
    for _ in range(config.TIMESTEP_NUMBER):
        print(_)
        a.update()


    center = config.GRID_EDGE_LENGTH // 2
    ion_fract = a.grids[4].cells

    y = ion_fract[center, center + 1:]
    x = np.linspace(0, center, center)

    fig, ax = plt.subplots()

    plt.xlabel("r (pc)")
    plt.ylabel("ionisaatioaste")
    plt.title(f"T = {config.STAR_SURFACE_TEMP} K")

    # teoreettisen ratkaisun mukainen raja
    s = stromgren()
    s /= config.CELL_EDGE_PC
    plt.axvline(s, color='red', linestyle='-')

    ax.xaxis.set_major_formatter(FuncFormatter(cells_to_pc))

    ax.plot(x, y)
    ax.set_xlim(0, s * 1.5)
    plt.show()