from src.models.grid import grid
from src.utils.config import config


# tässä homogeeninen vakiotiheys vedylle
class DENSITY_GRID(grid):
    def setup(self):
        self.cells *= config.HYDROGEN_DENSITY

    # oletuksena pilvi staattinen suhteessa tähteen
    def update(self):
        return self.cells