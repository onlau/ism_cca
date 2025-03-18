from src.mappings.mappings import grid_map, param_map
from src.mappings.func_mappings import setup_map, update_map
from src.utils.setuputils import setup_params as params
from src.controllers.setup import *
from src.controllers.update import *
import cupy as cp

def automaton_setup():
    l = len(grid_map)
    e = int(params[param_map["grid_edge"]].item())

    gridstack = cp.ones((l, e, e), dtype = cp.float64, order = "C")

    for i in range(0, l):
        setup_func = setup_map[grid_map.inverse[i]]
        setup_func((gridstack[i]))
    return gridstack

def update_automaton(a: cp.array):
    l = len(grid_map)
    new_stack = cp.ones_like(a)
    
    for i in range(l):
        update_func = update_map[grid_map.inverse[i]]
        new_stack[i] = update_func(a)
    
    for i in range(l):
        a[i] = new_stack[i]

automaton = automaton_setup()