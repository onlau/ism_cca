import cupy as cp
from src.mappings.mappings import param_map
import src.solvers.radiation_solver as rs
from src.utils.setuputils import setup_params

def setup_density(a):
    a *= setup_params[param_map["hydrogen_density"]]

def setup_photoionization(a):
    a *= 0

def setup_recomb_coeff(a):
    a *= rs.recombination_coeff()

def setup_ion_fract(a):
    a *= 0