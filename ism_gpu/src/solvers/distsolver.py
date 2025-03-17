from src.controllers.mappings import param_map
from src.utils.setuputils import setup_params
import cupy as cp

def find_dist():
    g = setup_params[param_map["grid_edge"]]
    c = setup_params[param_map["cell_edge"]]
    center = g // 2

    dist_x = dist_y = (cp.arange(g) - center)
    x, y = cp.meshgrid(dist_x, dist_y, indexing = "ij")
    dist = cp.sqrt(x**2 + y**2)

    return dist * c

dist = find_dist()