from src.utils.config import config
from src.models.grid import grid
import src.solvers.radiationsolvers as rad_func
import numpy as np


class PHOTOIONIZATION_GRID(grid):
    def setup(self):
        self.cells = np.zeros_like(self.cells)
    
    def update(self):
        unionized = self.automaton.grids[1].cells * (1 - self.automaton.grids[4].cells)     # ionisoitumattomat atomit = vedyn tiheys-(1-ionisaatioaste)
        new_cells = rad_func.PHOTOIONIZATION(config.STAR_SURFACE_TEMP, unionized, self.automaton.shortest_paths)
        return new_cells