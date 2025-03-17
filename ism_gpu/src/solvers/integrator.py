import cupy as cp

def integrator(f, lower, upper, n = 301):
    points = cp.linspace(lower, upper, n)

    res = cp.stack([f(v) for v in points], axis = 0)

    h = (upper - lower) / (n - 1)

    oddsum = cp.sum(res[1:-1:2], axis = 0)
    evensum = cp.sum(res[2:-1:2], axis = 0)
    return h / 3 * (res[0] + res[-1] + 4 * oddsum + 2 * evensum)
