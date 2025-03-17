from bidict import bidict


grid_map = bidict({
        "density": 0,
        "photoionization": 1,
        "recomb": 2,
        "ion_fract": 3,
})

param_map = bidict({
        "lyman_limit": 0,
        "gaunt_factor": 1,
        "c": 2,
        "h": 3,
        "k_B": 4,
        "timestep": 5,
        "stellar_radius": 6,
        "stellar_surf_temp": 7,
        "hydrogen_density": 8,
        "cell_edge": 9,
        "grid_edge": 10,
        "hydrogen_temperature": 11,
        "n": 12
})