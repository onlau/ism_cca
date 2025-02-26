from dataclasses import dataclass
from pathlib import Path
import json

# kaikki alustusparametrit annettava cgs-yksiköissä
#--------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class config:
    @classmethod
    def load_params(cls):
        lib_dir = Path(__file__).resolve().parent
        path_to_config = lib_dir / "../../config.json"

        with path_to_config.resolve().open() as f:
            params = json.load(f)
        if  params["grid_edge"] % 2 == 0:
            raise ValueError("Sivun pituuden oltava pariton")
        cls.TIMESTEP = params["timestep"]
        cls.CELL_EDGE = params["cell_edge"]
        cls.STAR_SURFACE_TEMP = params["stellar_surf_temp"]
        cls.STELLAR_RADIUS = params["stellar_radius"]
        cls.HYDROGEN_DENSITY = params["hydrogen_density"]
        cls.GRID_EDGE_LENGTH = params["grid_edge"]
        cls.TIMESTEP_NUMBER = params["n"]
        cls.CELL_EDGE_PC = cls.CELL_EDGE * 3.240756e-19
        cls.CELL_VOLUME = cls.CELL_EDGE**3

    RECOMB_COEFFICIENT = 2.6e-13

config.load_params()