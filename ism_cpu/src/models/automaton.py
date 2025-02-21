import src.solvers.pathsolver as rp
from src.models.subgrids.density_grid import DENSITY_GRID
from src.models.subgrids.photoionization_grid import PHOTOIONIZATION_GRID
from src.models.subgrids.ion_fract_grid import ION_FRACT_GRID
from src.models.subgrids.recombination_grid import RECOMBINATION_GRID

class automaton():
    def __init__(self):
        self.shortest_paths = rp.find_paths()

        self.grids = {
            1 : DENSITY_GRID(self),                 
            2 : PHOTOIONIZATION_GRID(self),         
            3 : RECOMBINATION_GRID(self),           
            4 : ION_FRACT_GRID(self),               
        }
        for grid in self.grids:
            self.grids[grid].setup()

    def access_grid(self, id):
        return self.grids[id]

    def update(self):
        new_grids = {}
        for i in self.grids:
            new_grids[i] = self.grids[i].update()
        for i in new_grids:
            self.grids[i].cells = new_grids[i]