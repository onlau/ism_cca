import numpy as np

# ionisaatioiden tasapainoyhtälö
def solve(ion, recomb):
    return np.sqrt(ion/recomb)