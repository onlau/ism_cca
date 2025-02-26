from src.models.automaton import automaton
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
from src.utils.config import config

def cells_to_pc(c, pos):
    return f"{c * config.CELL_EDGE_PC:.2f}"

def draw(a: automaton):
    cells = a.grids[4].cells

    fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(cells_to_pc))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(cells_to_pc))

    img = ax.imshow(cells, cmap="viridis", interpolation="nearest", vmin=0, vmax=1)

    def update(frame):
        cells = a.grids[4].cells
        a.update()      
        img.set_data(cells)

        return [img]

    ani = animation.FuncAnimation(fig, update, interval=100, frames=20, blit=False)

    plt.title(f"T = {config.STAR_SURFACE_TEMP} K")
    plt.xlabel("r (pc)")
    plt.ylabel("r (pc)")
    plt.show()