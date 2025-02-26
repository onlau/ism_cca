from dataclasses import dataclass
from src.utils.config import config
import src.utils.kernel_generator as kg

# tarpeellisia vakioita
@dataclass(frozen=True)
class constants:       
    config.load_params()   
    LYMAN_LIMIT = 3.29e15
    GAUNT_FACTOR = 0.8
    DISTANCE_KERNEL = kg.GENERATE_DISTANCE_KERNEL(config.GRID_EDGE_LENGTH, config.CELL_EDGE)
    DILUTION_FACTOR = (config.STELLAR_RADIUS / DISTANCE_KERNEL)**2 * 0.25    # ohennuskerroin
    
# vakiot
#--------------------------------------------------------------------------------------------------
    LYMAN_LIMIT = 3.29e15   # Hz
    GAUNT_FACTOR = 0.8
    c =  2.99792458e10  # valonnopeus
    h = 6.6261e-27      # planck
    k = 1.3807e-16      # boltzmann