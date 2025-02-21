from src.models.grid import grid
from src.solvers.ionizationsolver import solve
from src.utils.config import config
import numpy as np

class ION_FRACT_GRID(grid):
    def setup(self):
        self.cells *= np.zeros_like(self.cells)
        
    def update(self):
        photoionizations = self.automaton.grids[2].cells
        recombs = self.automaton.grids[3].cells * self.automaton.grids[1].cells ** 2
        eq = solve(photoionizations, recombs)
        dfract = eq - self.cells
        change = np.where(dfract > 0, abs(photoionizations - recombs * self.cells**2), -abs(photoionizations - recombs * self.cells**2))
        new = self.cells + change * config.TIMESTEP * config.HYDROGEN_DENSITY

        # Lähde https://casper.berkeley.edu/astrobaki/index.php/Recombination_Coefficients
        dp = 1 / (self.automaton.grids[3].cells * self.cells * self.automaton.grids[1].cells)

        damped = new + (self.cells - new) * np.exp(-dp * config.TIMESTEP)
        return np.clip(damped, 0, 1)