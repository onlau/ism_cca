import src.solvers.radiationsolvers as rad_func
from src.models.grid import grid
import numpy as np
from src.utils.config import config

class RECOMBINATION_GRID(grid):
    def setup(self):
        self.cells *= rad_func.HYDROGEN_RECOMBINATION()

    def update(self):
        return self.cells