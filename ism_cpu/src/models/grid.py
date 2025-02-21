import numpy as np
from src.utils.config import config


# Tämä luokka on prototyyppi aliluokille
class grid:
    def __init__(self, automaton):
        self.automaton = automaton
        self.cells = np.ones((config.GRID_EDGE_LENGTH, config.GRID_EDGE_LENGTH), dtype=np.float64)


    def setup(self):
        pass

    def update(self):
        pass    
