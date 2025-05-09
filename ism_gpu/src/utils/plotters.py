import cupy as cp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
from scipy.integrate import quad
from src.mappings.mappings import param_map as pm
from src.utils.setuputils import setup_params as p
from matplotlib.ticker import FuncFormatter


h = p[pm["h"]].item()
c = p[pm["c"]].item()
k = p[pm["k_B"]].item()
ll = p[pm["lyman_limit"]].item()
g = p[pm["gaunt_factor"]].item()
ce = p[pm["cell_edge"]].item()
e = p[pm["grid_edge"]].item()
sr = p[pm["stellar_radius"]].item()
st = p[pm["stellar_surf_temp"]].item()
dens = p[pm["hydrogen_density"]].item()
n = int(p[pm["n"]].item())

def ionizing_photons(f, T):
    return np.pi * 2 * h * f**3 * c**-2 / (np.exp(h * f / (k * T)) - 1) / (f * h)

def stromgren():
    int = quad(ionizing_photons, ll, ll * 10, args = (st))[0]
    luminosity = sr**2 * np.pi * 4 * int
    return np.cbrt(3 * luminosity / (4 * np.pi * dens ** 2 * 2.6e-13)) * 3.24076e-19

def cells_to_pc(c, pos):
    return f"{c * 3.240756e-19 * ce:.2f}"

def plot_ion_fraction(a, update_func):
    ts = p[pm["timestep"]].item()
    for _ in range(n):
        print(_)
        update_func(a)

    center = int(e // 2)
    ion_fract = a[3]

    y = cp.asnumpy(ion_fract[center, center + 1:])
    x = np.linspace(0, center, center)

    fig, ax = plt.subplots()

    plt.xlabel("r (pc)")
    plt.ylabel("ionisaatioaste")
    plt.title(f"T = {st} K, t = {n * ts / 31556995.2:.2f} a, Nₕ = {dens} cm⁻³")

    # teoreettisen ratkaisun mukainen raja
    s = stromgren()
    s /= 3.240756e-19 * ce
    plt.axvline(s, color='red', linestyle='-')

    ax.xaxis.set_major_formatter(FuncFormatter(cells_to_pc))
    print(f"strömgren: {stromgren():.2f} pc")
    ax.plot(x, y)
    ax.set_xlim(0, s * 1.4)
    ax.set_ylim(0, 1.2)
    plt.show()

def draw_animation(array, update_func, frames=100, interval=50):
    array = cp.asarray(array)
    fig, ax = plt.subplots()
    
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(cells_to_pc))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(cells_to_pc))
    
    img = ax.imshow(cp.asnumpy(array[3]), cmap='viridis', animated=True, vmin = 0, vmax = 1)
    
    def update(frame):
        update_func(array)
        img.set_array(cp.asnumpy(array[3]))
        return img,
    
    ax.set_title(f"T = {st} K, Nₕ = {dens} cm⁻³")
    cb = fig.colorbar(img, ax=ax)
    cb.set_label("Ionisaatioaste")

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)
    plt.show()
    
    return ani

def update_then_draw(a, update_func):
    ts = p[pm["timestep"]].item()
    
    for _ in range(n):
        print(_)
        update_func(a)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    titles = ["Hiukkastiheys (cm⁻³)", "Ionisaatioaste"]
    indices = [0, 3]
    mins = [0, 0]
    maxes = [1e2, 1]
    maps = ["inferno", "viridis"]

    for ax, title, idx, mi, ma, map in zip(axes, titles, indices, mins, maxes, maps):
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(cells_to_pc))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(cells_to_pc))
        
        ax.set_title(title)
        img = ax.imshow(cp.asnumpy(a[idx]), cmap=map, animated=True, vmin=mi, vmax=ma)
        cb = fig.colorbar(img, ax=ax)
        
    fig.suptitle(f"{title}, T = {st} K, t = {n * ts / 31556995.2:.2f} a")

    plt.show()