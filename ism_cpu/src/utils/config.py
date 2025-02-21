from dataclasses import dataclass
import src.utils.kernel_generator as kg

# kaikki alustusparametrit annettava cgs-yksiköissä
#--------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class config:          
    TIMESTEP = 31556995200e0        
    CELL_EDGE = 3.0857e18
    CELL_EDGE_PC = CELL_EDGE * 3.24076e-19
    CELL_VOLUME = CELL_EDGE ** 3

    STAR_SURFACE_TEMP = 2.8e4
    STELLAR_RADIUS = 6.957e10   # = 1 R_sun
    GRID_EDGE_LENGTH = 55       # ruudukon sivun kokonaispituus soluina
    HYDROGEN_DENSITY = 1e0
    RECOMB_COEFFICIENT = 2.6e-13

# tarpeellisia vakioita
@dataclass(frozen=True)
class constants:          
    LYMAN_LIMIT = 3.29e15
    GAUNT_FACTOR = 0.8
    DISTANCE_KERNEL = kg.GENERATE_DISTANCE_KERNEL(config.GRID_EDGE_LENGTH, config.CELL_EDGE)
    DILUTION_FACTOR = (config.STELLAR_RADIUS / DISTANCE_KERNEL)**2 * 0.25      # ohennuskerroin
    
# vakiot
#--------------------------------------------------------------------------------------------------
    LYMAN_LIMIT = 3.29e15
    GAUNT_FACTOR = 0.8
    c =  2.99792458e10  # valonnopeus
    h = 6.6261e-27      # planck
    k = 1.3807e-16      # boltzmann