import numpy as np
#--------------------------------------------------------------------------------------------------
def GENERATE_DISTANCE_KERNEL(grid_edge, cell_edge):
    center = grid_edge // 2

    dist_x = dist_y = (np.arange(grid_edge) - center) * cell_edge
    x, y = np.meshgrid(dist_x, dist_y, indexing = "ij")

    dist = np.sqrt(x**2 + y**2)

    return dist
#--------------------------------------------------------------------------------------------------