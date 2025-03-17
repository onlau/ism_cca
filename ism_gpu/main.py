import argparse
from src.models.cuda_automaton import automaton, update_automaton
from src.utils.plotters import plot_ion_fraction, animate_cupy_array

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--animate", action="store_true", help="Piirrä animaatio")
    parser.add_argument("-d", "--plot", action="store_true", help="Piirrä kuvaaja")
    args = parser.parse_args()
    
    if args.animate:
        animate_cupy_array(automaton, update_automaton)
    elif args.plot:
        plot_ion_fraction(automaton, update_automaton)
    else:
        return 0


if __name__ == "__main__":
    main()

