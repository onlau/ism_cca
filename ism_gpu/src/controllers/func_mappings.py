from bidict import bidict
import src.controllers.setup as s
import src.controllers.update as u

setup_map = bidict({
        "density": s.setup_density,
        "photoionization": s.setup_photoionization,
        "recomb": s.setup_recomb_coeff,
        "ion_fract": s.setup_ion_fract
})

update_map = bidict({
        "density": u.update_density,
        "photoionization": u.update_photoionization,
        "recomb": u.update_recomb,
        "ion_fract": u.update_ion_fract
})