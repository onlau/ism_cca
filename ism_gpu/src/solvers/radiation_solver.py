import cupy as cp
from src.mappings.mappings import param_map as pm
from src.utils.setuputils import setup_params as p
from src.solvers.pathsolver import paths
from src.solvers.distsolver import dist
from src.solvers.integrator import integrator

def photoionization(T, N0):
    h = p[pm["h"]].item()
    c = p[pm["c"]].item()
    k = p[pm["k_B"]].item()
    ll = p[pm["lyman_limit"]].item()
    g = p[pm["gaunt_factor"]].item()
    ce = p[pm["cell_edge"]].item()
    sr = p[pm["stellar_radius"]].item()      

    def find_od(f): 
        bf = 6e-18 * (ll/f)**3 * N0 * g * paths
        cumulative_bf = cp.sum(bf, axis = (-1, -2))
        valid_count = cp.sum(paths, axis = (-1, -2))
        avg_bf = cp.where(valid_count > 0, cumulative_bf / valid_count, 0)

        return avg_bf * dist
    
    def const():
        num = 6e-18 * 2 * cp.pi**2 * ll**3 * N0 * g
        den = c**2
        W = cp.where(dist == 0, 4 * cp.pi, (sr / dist)**2)
        return W * num / den

    def photoionization_per_freq(f):
        i = 1 / (f * cp.exp(h * f / (T * k)) - f)
        return i
    
    def integrand(f):
        return cp.exp(-find_od(f)) * photoionization_per_freq(f)

    res = const() * integrator(integrand, ll, ll*10)
    return cp.where(res == cp.inf, 0, res)


def recombination_coeff(): 
    return 4e-13