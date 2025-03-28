from src.mappings.mappings import param_map, grid_map
from src.utils.setuputils import setup_params as params
import cupy as cp
import src.solvers.radiation_solver as rs

def update_density(a):
    d = a[grid_map["density"]]
    return d

def update_photoionization(a):
    unionized = (1 - a[grid_map["ion_fract"]]) * a[grid_map["density"]]
    p = rs.photoionization(params[param_map["stellar_surf_temp"]].item(), unionized)
    return p

def update_recomb(a):
    r = a[grid_map["recomb"]]
    return r


def update_ion_fract(a):
    p = a[grid_map["photoionization"]]
    r = a[grid_map["recomb"]] * (a[grid_map["density"]] * a[grid_map["ion_fract"]])**2
    d = p - r

    n = a[grid_map["ion_fract"]] + d * params[[param_map["timestep"]]] / a[grid_map["density"]]
    return cp.clip(n, 0, 1)