import argparse
from src.automaton.automaton import automaton, update_automaton
from src.utils.plotters import plot_ion_fraction, draw_animation, update_then_draw

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--animate", action="store_true", help="Piirrä animaatio")
    parser.add_argument("-p", "--plot", action="store_true", help="Piirrä kuvaaja")
    parser.add_argument("-d", "--draw", action="store_true", help="Piirrä kuva")
    args = parser.parse_args()
    
    if args.animate:
        draw_animation(automaton, update_automaton)
    elif args.plot:
        plot_ion_fraction(automaton, update_automaton)
    elif args.draw:
        update_then_draw(automaton, update_automaton)
    else:
        return 0


if __name__ == "__main__":
    main()

