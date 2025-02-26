from src.models.automaton import automaton
from src.visualizations.plot2 import draw
from src.visualizations.plotter import plot_ion_fraction



def main():
    a = automaton()
    plot_ion_fraction(a)
    #draw(a)

if __name__ == "__main__":
    main()