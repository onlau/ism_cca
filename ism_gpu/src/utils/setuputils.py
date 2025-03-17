import json
import cupy as cp
from pathlib import Path
from src.controllers.mappings import param_map as pm
from scipy.integrate import quad
import numpy as np


def load_params():
    config_dir = Path(__file__).resolve().parent
    const_dir = Path(__file__).resolve().parent

    path_to_config = config_dir / "../../config.json"

    with path_to_config.resolve().open() as f:
        config = json.load(f)

    const = {
    "lyman_limit": 3.29e15,
    "gaunt_factor": 0.9,
    "c": 2.99792458e10,
    "h": 6.6261e-27,
    "k_B": 1.3807e-16
    }

    u = {**const, **config}

    def ionizing_photons(f, T):
        return np.pi * 2 * u["h"] * f**3 * u["c"]**-2 / (np.exp(u["h"] * f / (u["k_B"] * T)) - 1) / (f * u["h"])

    def stromgren():
        int = quad(ionizing_photons, u["lyman_limit"], u["lyman_limit"] * 10, args = (u["stellar_surf_temp"]))[0]
        luminosity = u["stellar_radius"]**2 * np.pi * 4 * int
        return np.cbrt(3 * luminosity / (4 * np.pi * u["hydrogen_density"] ** 2 * 2.6e-13))

    total_diameter = 1.5 * 2 * stromgren() * 1.4

    u["cell_edge"] = total_diameter / u["grid_edge"]
    default_timestep = 31556995200e0
    u["timestep"] = default_timestep / u["hydrogen_density"]

    sorted_u = dict(sorted(u.items(), key = lambda i:pm[i[0]]))

    parameters = cp.asarray([i[1] for i in sorted_u.items()])

    return parameters

setup_params = load_params()