import cupy as cp
from src.solvers.distsolver import dist

def isotropic_from_center(a):
    ma = 100

    dm = cp.where(dist / cp.max(dist) != 0, (1 - dist/ cp.max(dist) + 1e-20) * ma, 1)
    a *= dm

def filament(a):
    mi = 10
    ma = 100

    n = cp.ones_like(a) * mi
    s = n.shape[0]
    center = s//2
    n[center - s//10:center+s//10+1] = ma
    a *= n